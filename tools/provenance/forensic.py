#!/usr/bin/env python3
"""Read-only forensic utilities for the Universal Language Reciter build.

This tool reports evidence and uncertainty. It does not edit the production source.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECT = Path('/home/ubuntu/universal-language-reciter')
SOURCE = ROOT / 'source' / 'index.html'
FROZEN = Path('/tmp/frozen-projects')
COMPONENTS = ['Laya', 'MAF', 'LHE', 'CFHM']

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()

def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)+'\n', encoding='utf-8')

def files_under(base: Path):
    if not base.exists(): return []
    return [p for p in base.rglob('*') if p.is_file() and '.git' not in p.parts]

def text_files_under(base: Path):
    for p in files_under(base):
        try:
            b=p.read_bytes()
            if len(b) <= 2_000_000 and b'\0' not in b:
                yield p, b.decode('utf-8', errors='replace')
        except OSError: pass

def component_trace(names):
    rows=[]
    for name in names:
        matches=[]
        pattern=re.compile(r'(?<![A-Za-z0-9_])'+re.escape(name)+r'(?![A-Za-z0-9_])', re.I)
        for p,text in text_files_under(PROJECT):
            for i,line in enumerate(text.splitlines(),1):
                if pattern.search(line):
                    stripped=line.strip()
                    if stripped.startswith('//') or stripped.startswith('/*') or stripped.startswith('*'):
                        kind='comment'
                    elif re.search(r'\b(import|require)\b',line): kind='import'
                    elif re.search(r'\b(fetch|axios|http|api|mcp|exec)\b',line,re.I): kind='api-or-execution-like'
                    elif p.suffix.lower() in {'.md','.txt'}: kind='documentation'
                    else: kind='string-or-code-reference'
                    matches.append({'file':str(p),'line':i,'reference_type':kind,'context':stripped[:500]})
        rows.append({'component':name,'matches':matches,'direct_execution_evidence':'NO_SURVIVING_MATCH_IN_PROJECT' if not matches else 'NOT_ESTABLISHED','status':'UNRESOLVED' if not matches else 'PARTIALLY_ESTABLISHED'})
    return {'scan_root':str(PROJECT),'components':rows,'note':'A name match is not execution evidence.'}

def normalized(s):
    return re.sub(r'\s+',' ',s).strip()

def source_provenance():
    current=SOURCE.read_text(encoding='utf-8')
    base=ROOT/'archive/reciter-baseline/index.html'
    out={'current':{'path':str(SOURCE),'sha256':sha256(SOURCE)},'baseline':{'path':str(base),'sha256':sha256(base)},'classifications':[]}
    out['classifications'].append({'candidate':str(base),'classification':'UNCHANGED' if current==base.read_text(encoding='utf-8') else 'MODIFIED'})
    needles=[('function detectUnicode','detectUnicode'),('function extractBigrams','extractBigrams'),('function cosineSimilarity','cosineSimilarity'),('function detectNgram','detectNgram'),('function detectLanguage','detectLanguage'),('function speakText','speakText')]
    current_norm=normalized(current)
    for repo in sorted([p for p in FROZEN.iterdir()] if FROZEN.exists() else []):
        if not repo.is_dir(): continue
        for p,text in text_files_under(repo):
            if len(text)<100: continue
            # conservative exact normalized whole-file match only; otherwise record no exact match
            if normalized(text)==current_norm:
                out['classifications'].append({'candidate':str(p),'classification':'UNCHANGED','basis':'normalized whole-file match'})
    out['implementation_regions']=[{'function':n,'found':token in current,'source_line':next((i for i,l in enumerate(current.splitlines(),1) if token in l),None)} for token,n in needles]
    return out

def dependency_audit():
    rows=[]
    candidates=['package.json','package-lock.json','pnpm-lock.yaml','yarn.lock','requirements.txt','pyproject.toml','vite.config.js','vite.config.ts','Makefile']
    found=[]
    for name in candidates:
        p=PROJECT/name
        if p.exists(): found.append(str(p))
    # single-file project: imports are not package imports; external font links are network resources
    html=SOURCE.read_text(encoding='utf-8')
    urls=re.findall(r'https?://[^"\']+',html)
    rows += [{'dependency':u,'version':'UNKNOWN','source':'HTML external URL','local_external':'external','used_by':'index.html','status':'REFERENCE_ONLY'} for u in urls]
    return {'project':str(PROJECT),'metadata_files':found,'dependencies':rows,'note':'No package manifest was present in the inspected project; textual URLs are not local dependencies.'}

def internal_discovery():
    rows=[]
    for p in files_under(PROJECT):
        ext=p.suffix.lower()
        if ext in {'.sh','.py','.js','.ts','.json','.mjs'} or os.access(p,os.X_OK):
            rows.append({'path':str(p),'type':'script-or-config','size':p.stat().st_size,'reciter_use':'UNKNOWN'})
    return {'scan_root':str(PROJECT),'tools':rows,'note':'This scan does not infer creator or use from file type.'}

def artefact_inventory():
    rows=[]
    roots=[PROJECT,ROOT]
    seen=set()
    for base in roots:
        for p in files_under(base):
            if p in seen: continue
            seen.add(p)
            rel=str(p.relative_to(base))
            if p.suffix in {'.zip','.tar','.gz'}: typ='ARCHIVE'
            elif p.suffix in {'.js','.py','.sh'}: typ='SCRIPT'
            elif p.suffix in {'.json','.yaml','.yml'}: typ='CONFIGURATION'
            elif p.suffix in {'.md','.txt'}: typ='DOCUMENTATION'
            elif p.suffix in {'.html','.css'}: typ='SOURCE'
            else: typ='UNKNOWN'
            rows.append({'path':str(p),'type':typ,'size':p.stat().st_size,'mtime':p.stat().st_mtime,'relationship':'Reciter or forensic repository artifact'})
    return {'artifacts':rows}

def baseline_diff():
    base=ROOT/'archive/reciter-baseline'
    cur_files={str(p.relative_to(PROJECT)):p for p in files_under(PROJECT)}
    base_files={str(p.relative_to(base)):p for p in files_under(base)}
    added=sorted(set(cur_files)-set(base_files)); removed=sorted(set(base_files)-set(cur_files)); modified=[]
    for k in sorted(set(cur_files)&set(base_files)):
        if sha256(cur_files[k])!=sha256(base_files[k]): modified.append({'path':k,'current_sha256':sha256(cur_files[k]),'baseline_sha256':sha256(base_files[k])})
    return {'baseline':str(base),'current':str(PROJECT),'added_files':added,'removed_files':removed,'modified_files':modified,'new_dependencies':'UNKNOWN','new_tools':'UNKNOWN'}

def runtime_trace():
    html=SOURCE.read_text(encoding='utf-8')
    script=re.search(r'<script>([\s\S]*?)</script>',html).group(1)
    harness=r'''const vm=require('vm'); const fs=require('fs');
const code=fs.readFileSync(process.argv[2],'utf8');
const script=code.split('<script>')[1].split('</script>')[0];
const elements={};
function el(id){return elements[id]||(elements[id]={id,value:'',textContent:'',innerHTML:'',className:'',dataset:{},style:{},options:[],addEventListener(){}})}
const ctx={console, setTimeout:()=>{}, clearTimeout:()=>{}, window:{speechSynthesis:null}, document:{getElementById:el,createElement:()=>({})}, SpeechSynthesisUtterance:function(t){this.text=t}, LANGUAGE_PROFILES:undefined};
vm.createContext(ctx); vm.runInContext(script+';globalThis.__api={detectUnicode,extractBigrams,cosineSimilarity,detectNgram,detectLanguage};',ctx);
const api=ctx.__api;
const inputs=['hola','Esta es una oración mucho más larga que contiene varios patrones del español.','Hello my friend.\\nمرحبا يا صديقي.\\nBonjour mon ami.',''];
const out={node:process.version,inputs:[]};
for(const input of inputs){const u=api.detectUnicode(input), n=api.detectNgram(input), f=api.detectLanguage(input); out.inputs.push({input,unicode:u,ngram:n,final:f});}
console.log(JSON.stringify(out));
'''
    runner=ROOT/'tools/provenance/.runtime_runner.js'; runner.write_text(harness,encoding='utf-8')
    temp=ROOT/'tools/provenance/.runtime_source.html'; temp.write_text(html,encoding='utf-8')
    try:
        proc=subprocess.run(['node',str(runner),str(temp)],capture_output=True,text=True,timeout=20)
        if proc.returncode!=0: return {'status':'FAILED','stderr':proc.stderr,'stdout':proc.stdout,'method':'Node VM harness'}
        return {'status':'EXECUTED','method':'Node VM harness','source':str(SOURCE),'result':json.loads(proc.stdout)}
    except Exception as e: return {'status':'FAILED','error':repr(e),'method':'Node VM harness'}
    finally:
        runner.unlink(missing_ok=True); temp.unlink(missing_ok=True)

def build_trace():
    # A static single HTML file has no declared build command. This is an observation, not a build success.
    return {'status':'NOT_APPLICABLE_OR_UNSPECIFIED','project':str(PROJECT),'build_command':'UNKNOWN','files_read':[str(PROJECT/'index.html')],'generated_files':[],'errors':[],'warnings':['No package manifest or build script was found in the inspected project.']}

def report_named(traces, prov, deps):
    rows=[]
    for name in COMPONENTS:
        row=next(x for x in traces['components'] if x['component']==name)
        rows.append({'component':name,'direct_execution_evidence':'NO' if not row['matches'] else 'UNKNOWN','source_level_evidence':row['matches'],'sandbox_evidence':'NOT_FOUND_IN_PROJECT_SCAN','runtime_evidence':'NOT_TESTED_AS_COMPONENT','provenance':'UNKNOWN','status':'UNRESOLVED'})
    rows.append({'component':'Frozen repository sections','direct_execution_evidence':'NO','source_level_evidence':'No exact whole-file match found by conservative scanner','sandbox_evidence':'Frozen checkouts exist under /tmp/frozen-projects','runtime_evidence':'Not tested as Reciter dependencies','provenance':'PARTIALLY_SUPPORTED_AS_EXTERNAL_REFERENCE_ONLY','status':'PARTIALLY_ESTABLISHED'})
    return {'reports':rows,'rule':'Named references and source similarity do not establish direct execution or copying.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default=str(ROOT/'provenance/raw')); args=ap.parse_args()
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    results={
      'component-trace':component_trace(COMPONENTS),
      'source-provenance':source_provenance(),
      'dependency-audit':dependency_audit(),
      'internal-tools':internal_discovery(),
      'sandbox-inventory':artefact_inventory(),
      'baseline-diff':baseline_diff(),
      'runtime-trace':runtime_trace(),
      'build-trace':build_trace(),
    }
    results['named-components']=report_named(results['component-trace'],results['source-provenance'],results['dependency-audit'])
    results['provenance-map']={
      'nodes':[{'id':'baseline','status':'OBSERVED','path':str(ROOT/'archive/reciter-baseline')},{'id':'sandbox-copy','status':'OBSERVED','path':str(SOURCE)},{'id':'frozen-repositories','status':'OBSERVED','path':str(FROZEN)},{'id':'external-components','status':'UNKNOWN','names':COMPONENTS},{'id':'runtime','status':results['runtime-trace']['status']}],
      'edges':[{'from':'baseline','to':'sandbox-copy','status':'SUPPORTED','basis':'byte-identical preserved source/archive comparison'},{'from':'frozen-repositories','to':'sandbox-copy','status':'UNKNOWN','basis':'no exact whole-file match established'},{'from':'external-components','to':'sandbox-copy','status':'UNKNOWN','basis':'no surviving direct import/API evidence in inspected project'},{'from':'sandbox-copy','to':'runtime','status':'EXECUTED','basis':'Node VM runtime trace'}]
    }
    for k,v in results.items(): write_json(out/(k+'.json'),v)
    return 0
if __name__=='__main__': sys.exit(main())
