Phase 1 
# RECITER BUILD FORENSIC REPOSITORY
 
## Role: IT Researcher / Build Historian
 
You are responsible for preserving the **actual technical history of the Reciter build**.
 
Do not act as the author of the investigation lessons.
 
Your job is to document the software as it actually exists and behaves so that a later researcher can examine the build independently.
 
The later `lesson-*.md` files will contain the human investigations and examined answers. Your repository must therefore provide the underlying technical evidence those lessons can examine.
 
***
 
# 1. PRIMARY OBJECTIVE
 
Create and maintain a forensic record of the Reciter project beginning with the **first model/build version**.
 
The repository must allow a future researcher to answer:
 
- What was actually built?
- What source code existed?
- What did the runtime actually do?
- What inputs were tested?
- What outputs were produced?
- What failed?
- What changed?
- What was known at each stage?
- Which observations came directly from execution?
- Which behaviour was implementation-defined?
- Which conclusions were discovered later through investigation?

 
Do not rewrite history to match later conclusions.
 
If a later lesson discovers that an earlier implementation had a limitation, preserve the original implementation and record the limitation as a later examination result.
 
***
 
# 2. SEPARATION OF EVIDENCE AND INTERPRETATION
 
Maintain this distinction strictly:
 
```text
BUILD
  ↓
SOURCE CODE
  ↓
RUNTIME EXECUTION
  ↓
OBSERVED RESULT
  ↓
TECHNICAL RECORD
  ↓
LATER LESSON / EXAMINATION
  ↓
INTERPRETATION OR CONCLUSION
```
 
Your responsibility ends primarily at the **technical record** layer.
 
The lesson files are responsible for examining what those records mean.
 
Do not silently insert conclusions into the source-code history.
 
***
 
# 3. PRESERVE THE FIRST MODEL
 
The first model/build is an important historical reference.
 
Do not overwrite it merely because later versions improve it.
 
Preserve:
 
```text
archive/
    reciter-baseline/
```
 
or an equivalent immutable baseline location.
 
If the original project exists as a ZIP/archive, preserve that archive separately:
 
```text
archive/
    reciter-baseline-v1.zip
```
 
Also preserve the extracted source when practical.
 
The baseline must remain identifiable as:
 
> The state of the build before later investigations changed or corrected it.

 
***
 
# 4. SOURCE CODE RECORD
 
Preserve the actual source code.
 
Recommended structure:
 
```text
source/
    ...
```
 
Do not replace source code with summaries.
 
Do not convert implementation into pseudocode when the actual source is available.
 
Do not remove apparently unnecessary code merely because later reasoning considers it irrelevant.
 
If code is changed, preserve the change through version history or an explicit change record.
 
***
 
# 5. RUNTIME RESULTS
 
Runtime behaviour is evidence.
 
Whenever practical, record actual execution results in:
 
```text
evidence/
    runtime/
```
 
For each important runtime investigation, record:
 
```text
Test ID:
Date:
Build/version:
Input:
Execution method:
Expected behaviour, if explicitly defined:
Actual output:
Errors:
Warnings:
Relevant source files:
Relevant functions:
Exit/status:
Additional observations:
```
 
Do not fabricate expected results.
 
If no expected result was previously defined, write:
 
```text
Expected behaviour: not previously specified
```
 
rather than inventing one.
 
***
 
# 6. OBSERVATION LANGUAGE
 
Use evidence-oriented language.
 
Prefer:
 
```text
Observed:
The function returned X.

Observed:
Arabic characters were removed by the cleaning expression.

Observed:
The detector returned English as the final result.

Observed:
The runtime produced confidence = 35.
```
 
Avoid turning observations into conclusions prematurely:
 
```text
Bad:
The system understands English.

Better:
The runtime returned English as the selected language.
```
 
```text
Bad:
The detector cannot support multilingual text.
```
 
unless an actual test establishes that claim.
 
Instead:
 
```text
Observed:
The tested implementation returned one final language result for the supplied multilingual input.
```
 
The later lesson can determine what that observation implies.
 
***
 
# 7. RECORD EXACT RUNTIME OUTPUTS
 
When a runtime result matters, preserve the actual value.
 
For example:
 
```text
Input:
Hello my friend.
مرحبا يا صديقي.
Bonjour mon ami.

Observed:
Unicode stage:
script = latin
confidence = 63

Observed:
N-gram stage:
winner = English
score = 0.2312863959

Observed:
Final result:
language = English
confidence = 35
method = fallback
```
 
Do not replace these with:
 
```text
The system was approximately 63% Latin.
```
 
unless that interpretation is explicitly justified.
 
Raw values are more valuable than later paraphrases.
 
***
 
# 8. PRESERVE FAILURES
 
Failures are first-class research evidence.
 
Record:
 
- failed tests
- unexpected outputs
- exceptions
- malformed outputs
- missing data
- unsupported scripts
- incorrect routing
- fallback behaviour
- threshold failures
- build failures
- runtime failures
- discrepancies between expected and actual behaviour

 
Do not clean the historical record simply because the failure was later fixed.
 
Use:
 
```text
failure/
```
 
or an equivalent evidence section when useful.
 
A corrected implementation does not erase the fact that the earlier implementation failed.
 
***
 
# 9. PRESERVE IMPLEMENTATION DETAILS
 
When a runtime result depends on a particular implementation detail, record the relevant source location.
 
For example:
 
```text
Function:
extractBigrams()

Implementation:
text.toLowerCase().replace(/[^a-z]/g, '')

Observed consequence in test:
Non-ASCII characters were absent from the resulting n-gram input.
```
 
Keep the distinction:
 
```text
Implementation evidence
≠
Experimental evidence
≠
Hypothesis
≠
Final conclusion
```
 
Do not label an implementation detail as experimental evidence unless an actual experiment established it.
 
***
 
# 10. DO NOT RETROFIT HISTORY
 
Later discoveries must not rewrite earlier records.
 
Suppose Lesson 8 discovers:
 
> The representation loses information needed for multilingual localisation.

 
Do not rewrite the original runtime record as though the original developer already knew this.
 
Instead preserve:
 
```text
Original implementation
        ↓
Original runtime result
        ↓
Later investigation
        ↓
Newly identified limitation
```
 
This chronological separation is essential.
 
***
 
# 11. LESSON FILES ARE A SEPARATE LAYER
 
Do NOT automatically create or rewrite:
 
```text
lesson-01.md
lesson-02.md
...
lesson-08.md
```
 
unless explicitly instructed.
 
Those files belong to the investigation/research layer.
 
They will contain questions, examinations, reasoning, revisions, and conclusions developed outside the raw build record.
 
Your repository should make it possible for those lessons to cite or inspect the technical evidence.
 
***
 
# 12. RECOMMENDED REPOSITORY STRUCTURE
 
Use a structure approximately like:
 
```text
reciter/
│
├── README.md
│
├── source/
│   └── [actual Reciter source]
│
├── archive/
│   └── reciter-baseline-v1.zip
│
├── evidence/
│   ├── runtime/
│   ├── tests/
│   ├── failures/
│   └── implementation/
│
├── lessons/
│   └── [maintained separately by researcher]
│
├── examinations/
│   └── [maintained separately by researcher]
│
└── CHANGELOG.md
```
 
Do not create unnecessary complexity if the existing project structure already provides a better equivalent.
 
The principle matters more than the exact directory names.
 
***
 
# 13. CHANGELOG
 
Maintain a factual change history.
 
For each meaningful change:
 
```text
Version:
Date:
Changed:
Reason explicitly given by developer:
Files affected:
Observed runtime difference:
```
 
Do not invent a reason.
 
If the reason is unknown:
 
```text
Reason:
Not recorded.
```
 
This is preferable to reconstructing a reason from assumption.
 
***
 
# 14. TEST REPRODUCIBILITY
 
For important tests, preserve enough information to reproduce them:
 
```text
input
build/version
configuration
execution method
relevant source version
output
errors
```
 
If environment information matters, record it:
 
```text
runtime
browser
Node version
OS
package version
device
```
 
Only record information actually available.
 
Do not fabricate missing environment data.
 
***
 
# 15. SOURCE-TO-RUNTIME TRACEABILITY
 
Whenever possible, connect:
 
```text
Test
  ↓
Input
  ↓
Function
  ↓
Implementation
  ↓
Runtime output
```
 
For example:
 
```text
TEST-RUNTIME-001

Input:
[exact input]

Relevant function:
detectLanguage()

Relevant implementation:
[actual source reference]

Observed intermediate output:
[actual output]

Observed final output:
[actual output]
```
 
This allows later lessons to investigate the build rather than relying on memory.
 
***
 
# 16. WHAT NOT TO DO
 
Do not:
 
- invent missing runtime results
- rewrite old behaviour using current behaviour
- hide failures
- remove inconvenient evidence
- turn observations into conclusions
- claim a hypothesis is verified merely because code implements it
- claim an implementation is experimentally validated without an experiment
- create fake confidence percentages
- infer multilingual capability from a single successful test
- infer inability from a single failed test unless the test actually establishes that boundary
- write the lesson conclusions for the researcher
- modify historical source merely to make it consistent with later lessons

 
***
 
# 17. THE RESEARCH PRINCIPLE
 
Treat the repository as the **memory of the build**.
 
The later lessons are the **examination of that memory**.
 
Therefore:
 
```text
Repository:
"What happened?"

Lessons:
"What does the evidence show?"

Examinations:
"Does the proposed explanation survive testing?"

Revisions:
"What changed after examination?"
```
 
Do not collapse these layers into one document.
 
***
 
# 18. FINAL REQUIREMENT
 
At the end of the initial repository setup, provide a concise factual report containing:
 
1. Baseline preserved
2. Source files preserved
3. Runtime/test evidence preserved
4. Known failures preserved
5. Current build state
6. Version/change history
7. Any missing evidence
8. Any assumptions that could not be verified

 
Use explicit labels:
 
```text
OBSERVED
IMPLEMENTED
EXECUTED
FAILED
UNKNOWN
```
 
Do not use:
 
```text
PROVEN
VERIFIED
CORRECT
SUCCESSFUL
```
 
unless the available evidence actually justifies those terms.
 
The objective is not to make the build look successful.
 
The objective is to make the build **rememberable, inspectable, reproducible, and examinable**.

Phase 2 

# ADDENDUM — BUILD PROVENANCE AND SANDBOX FORENSICS
 
## Purpose
 
The Reciter build may have involved multiple implementation sources, including:
 
- Laya AI
- MAF
- LHE
- CFHM
- previously frozen repository sections
- copied or adapted implementation sections
- Manus Sandbox modifications
- Manus-created internal tools, wrappers, adapters, or scripts

 
The exact relationship between these components must be **investigated and recorded**, not assumed.
 
This is especially important because the final build may contain implementation behaviour whose original source is not obvious from the final source tree.
 
***
 
# 1. DO NOT ASSUME DIRECT TOOL USE
 
If the build contains references to a named system such as:
 
```text
Laya
MAF
LHE
CFHM
```
 
do not automatically conclude:
 
> Manus directly invoked that system.

 
Several possibilities must remain distinguishable:
 
```text
A. Direct external tool/model use
B. API/interface use
C. Copied implementation
D. Adapted implementation
E. Frozen repository code reused unchanged
F. Frozen repository code modified for Sandbox
G. Manus-created wrapper around another system
H. Manus-created internal replacement
I. Configuration/specification copied without implementation
J. Provenance currently unknown
```
 
Record which possibility is actually supported by evidence.
 
***
 
# 2. INVESTIGATE THE SANDBOX
 
Inspect the Manus Sandbox/project environment for evidence of:
 
- copied source directories
- duplicated repositories
- generated files
- internal scripts
- wrappers
- adapters
- configuration files
- package dependencies
- MCP/tool definitions
- API clients
- local services
- executable scripts
- renamed components
- imported modules
- cached/generated implementation
- documentation describing external systems
- build instructions referring to external models/tools

 
Do not assume that the visible final application source represents the entire implementation process.
 
***
 
# 3. TRACE NAMED COMPONENTS
 
For every named implementation or framework that appears in the build instructions or source, create a provenance record.
 
Example:
 
```text
COMPONENT:
Laya AI

FOUND IN:
[exact file/path]

REFERENCE TYPE:
[import / API / documentation / copied code / configuration / unknown]

DIRECT EXECUTION EVIDENCE:
[yes / no / not found]

LOCAL IMPLEMENTATION:
[yes / no / unclear]

ADAPTED CODE:
[yes / no / unclear]

WRAPPER/ADAPTER:
[yes / no / unclear]

SOURCE PROVENANCE:
[known / partially known / unknown]

EVIDENCE:
[exact files, commands, logs, or configuration]
```
 
Repeat for:
 
```text
MAF
LHE
CFHM
```
 
and any other named system discovered.
 
***
 
# 4. FROZEN REPOSITORY PROVENANCE
 
Some implementation sections may have originated from a previously frozen repository state.
 
Do not describe such code as newly created by Manus merely because it exists in the current Sandbox.
 
For every suspected reused section, investigate:
 
```text
original location
original version/commit
current location
copy/adaptation status
modifications
date/version if available
dependency changes
behavioural changes
```
 
Use explicit classifications:
 
```text
UNCHANGED COPY
MODIFIED COPY
ADAPTED IMPLEMENTATION
INSPIRED/DERIVED
PROVENANCE UNKNOWN
```
 
Do not use "copied" unless evidence supports copying.
 
***
 
# 5. MANUS SANDBOX MODIFICATIONS
 
If external or frozen implementation was modified for the Manus Sandbox, preserve the distinction:
 
```text
ORIGINAL IMPLEMENTATION
        ↓
SANDBOX ADAPTATION
        ↓
RECITER INTEGRATION
```
 
Record what changed.
 
For example:
 
```text
Original:
[component]

Sandbox modification:
[actual modification]

Reason:
[only if recorded]

Reciter integration:
[actual integration]
```
 
If the reason is unknown:
 
```text
Reason:
UNKNOWN
```
 
Do not reconstruct the reason from the final behaviour.
 
***
 
# 6. INTERNAL TOOLS
 
Investigate whether Manus created internal tooling that does not appear as part of the final Reciter application.
 
Possible examples include:
 
```text
tool wrappers
build scripts
conversion scripts
test harnesses
code generators
MCP servers
MCP clients
local adapters
environment helpers
model adapters
validation scripts
repository synchronisation tools
```
 
If an internal tool is discovered, record:
 
```text
Tool name:
Location:
Purpose:
Inputs:
Outputs:
Created by:
Creation evidence:
Used during Reciter build:
Yes / No / Unknown
Current status:
```
 
Do not infer that a tool existed merely because Manus produced a correct response about a tool's name.
 
That observation may justify an investigation, but it does not establish the mechanism.
 
***
 
# 7. IMPORTANT PROVENANCE QUESTION
 
If Manus was able to respond to an instruction mentioning a specific tool or component, record this only as:
 
```text
OBSERVED:
Manus produced/accepted an implementation involving the named component.
```
 
Do not automatically record:
 
```text
PROVEN:
Manus internally installed that component.
```
 
Possible mechanisms include:
 
```text
direct tool access
existing project knowledge
repository documentation
copied implementation
configuration
wrapper
internal tool
context supplied by the user
model knowledge
```
 
The provenance investigation must distinguish these possibilities.
 
***
 
# 8. SEARCH FOR TECHNICAL TRACES
 
Where permitted by the environment, inspect:
 
```text
package manifests
lock files
imports
environment variables
configuration files
MCP configuration
tool definitions
scripts
build logs
terminal history available to the project
generated files
repository metadata
Git history
commit messages
dependency trees
API endpoints
local service definitions
README/instruction files
```
 
The objective is not surveillance of Manus.
 
The objective is **technical provenance reconstruction of the build**.
 
***
 
# 9. PRESERVE THE RESULT EVEN IF PROVENANCE IS UNKNOWN
 
Unknown provenance is a valid research result.
 
For example:
 
```text
COMPONENT:
Laya

OBSERVED:
A local implementation contains functionality associated with Laya.

DIRECT TOOL INVOCATION:
No surviving evidence found.

COPIED SOURCE:
No surviving evidence found.

LOCAL WRAPPER:
Possible, but not established.

PROVENANCE:
UNKNOWN.
```
 
This is much more valuable than inventing an explanation.
 
***
 
# 10. PROVENANCE CONFIDENCE MUST NOT BECOME FALSE CERTAINTY
 
Do not convert:
 
```text
likely
possible
appears to
resembles
probably
```
 
into:
 
```text
used
created
copied
installed
implemented
```
 
unless the evidence establishes it.
 
Use:
 
```text
OBSERVED
TRACEABLE
SUPPORTED
PARTIALLY SUPPORTED
UNRESOLVED
UNKNOWN
```
 
rather than an arbitrary numerical confidence score unless an actual measurement protocol exists.
 
***
 
# 11. RELATION TO THE LESSONS
 
The provenance investigation belongs to the **build evidence layer**.
 
Later lessons may ask questions such as:
 
> What implementation was actually responsible for this behaviour?

 
or:
 
> Was this behaviour inherited from the frozen repository, introduced by an adaptation, or created during the Sandbox build?

 
The repository should contain enough evidence for those questions to be examined.
 
Do not answer those questions retrospectively inside the source history.
 
***
 
# 12. FINAL PROVENANCE MAP
 
Create a machine-readable or human-readable map when enough evidence is available:
 
```text
USER / RESEARCH INSTRUCTION
        ↓
FROZEN REPOSITORY
        ↓
EXTERNAL MODEL / TOOL / FRAMEWORK
        ↓
MANUS SANDBOX
        ↓
ADAPTATION / WRAPPER / INTERNAL TOOL
        ↓
RECITER SOURCE
        ↓
BUILD
        ↓
RUNTIME
```
 
Not every node will necessarily exist.
 
The map must represent **what the evidence establishes**, not what seems architecturally plausible.
 
For each connection, mark:
 
```text
OBSERVED
SUPPORTED
INFERRED
UNKNOWN
```
 
***
 
# 13. HISTORICAL INTEGRITY
 
If later investigation discovers that the implementation provenance was misunderstood, do not erase the earlier record.
 
Instead record:
 
```text
Earlier assumption:
[...]

Later evidence:
[...]

Revision:
[...]

Original evidence preserved:
YES
```
 
This allows the repository to remember not only what the software did, but also **how our understanding of how it was built changed over time**.
 
***
 
# 14. FINAL REPORT ADDITION
 
Add the following to the initial Manus build report:
 
### Implementation Provenance
 

|Component|Evidence of use|Local copy|Adapted|Wrapper/internal tool|Provenance|
|---|---|---|---|---|---|
|Laya|...|...|...|...|...|
|MAF|...|...|...|...|...|
|LHE|...|...|...|...|...|
|CFHM|...|...|...|...|...|
|Frozen repository sections|...|...|...|...|...|
|Other|...|...|...|...|...|
 
Use `UNKNOWN` where evidence is insufficient.
 
Never fill an unknown cell with an assumption.
 
## Core rule
 
> **Do not merely preserve what the final Reciter contains. Preserve the provenance trail showing how each significant implementation component entered the build.**

 
The repository should allow a later researcher to distinguish:
 
```text
WHAT WAS BUILT
from
WHERE IT CAME FROM
from
HOW IT WAS ADAPTED
from
WHAT MANUS ACTUALLY EXECUTED
from
WHAT WE LATER INFERRED ABOUT IT.
```

Phase  3

# RECITER PROVENANCE INVESTIGATION TOOLSET
 
## Objective
 
Create a small forensic toolset inside the Manus Sandbox for answering unresolved questions about how the Reciter build was assembled.
 
The toolset must investigate the existing build and its available project history.
 
It must NOT manufacture evidence, rewrite source history, or assume that Laya, MAF, LHE, CFHM, or any other named component was directly executed.
 
The purpose is to make the unresolved provenance questions technically testable.
 
***
 
# 1. CREATE A FORENSIC TOOL DIRECTORY
 
Create:
 
```text
tools/
    provenance/
```
 
Keep these tools separate from the Reciter production code.
 
They are research/investigation utilities, not Reciter runtime components.
 
***
 
# 2. TOOL: COMPONENT TRACE
 
Create a tool that searches the available project for references to named components.
 
Initial targets:
 
```text
Laya
MAF
LHE
CFHM
```
 
Also allow arbitrary additional component names.
 
For every match, report:
 
```text
component
file
line/location
reference type
surrounding context
import/reference relationship
```
 
Distinguish:
 
```text
import
function call
API endpoint
configuration
documentation
comment
string reference
generated file
wrapper
unknown
```
 
Do not classify a reference as actual execution merely because the name appears.
 
Output example:
 
```text
COMPONENT: Laya

FOUND:
src/adapter.js:42

REFERENCE TYPE:
import

DIRECT EXECUTION:
Not established

TRACE:
[relevant evidence]
```
 
***
 
# 3. TOOL: SOURCE PROVENANCE SCANNER
 
Create a tool that detects potentially reused or copied implementation.
 
Compare the current Reciter source against:
 
- preserved baseline source
- available frozen repository source
- previous project versions
- duplicated source directories
- available repository history

 
Report:
 
```text
exact matches
near matches
modified matches
unique current code
```
 
Do not call a near match a copy unless the evidence supports that conclusion.
 
Use classifications:
 
```text
UNCHANGED
MODIFIED
POSSIBLE DERIVATION
NO MATCH
UNKNOWN
```
 
***
 
# 4. TOOL: DEPENDENCY / IMPORT AUDITOR
 
Inspect available project metadata such as:
 
```text
package.json
lock files
imports
module references
configuration
scripts
build files
environment configuration
```
 
Produce:
 
```text
dependency
version
source
local/external
used by
```
 
Specifically investigate whether any named component is actually connected to the build.
 
A textual mention alone must not appear in the dependency list.
 
***
 
# 5. TOOL: INTERNAL TOOL DISCOVERY
 
Search the Manus Sandbox project for possible internal tools.
 
Look for:
 
```text
scripts
executables
wrappers
adapters
MCP configuration
MCP servers
MCP clients
local APIs
helper programs
code generators
test harnesses
build helpers
conversion tools
model adapters
```
 
For each discovered tool:
 
```text
name
location
type
inputs
outputs
dependencies
references
creation/version evidence
whether Reciter uses it
```
 
Do not assume that every script is a Manus-created tool.
 
***
 
# 6. TOOL: RUNTIME TRACE
 
Create a controlled runtime tracing mechanism for the Reciter where technically possible.
 
The objective is to answer:
 
> Which local components actually execute when a specified Reciter operation runs?

 
For example:
 
```text
input
  ↓
entry point
  ↓
function
  ↓
module
  ↓
adapter
  ↓
external/local dependency
  ↓
output
```
 
Record actual execution evidence.
 
If runtime tracing is not possible for a particular environment, record:
 
```text
RUNTIME TRACE:
UNAVAILABLE

Reason:
[actual technical limitation]
```
 
Never replace missing runtime evidence with inference.
 
***
 
# 7. TOOL: BUILD TRACE
 
Record what happens during a clean build.
 
Capture, where available:
 
```text
build command
files read
modules loaded
dependencies invoked
generated files
build output
errors
warnings
artifacts
```
 
The purpose is to determine whether apparently external components are actually part of the build process.
 
***
 
# 8. TOOL: SANDBOX ARTEFACT INVENTORY
 
Inventory relevant artefacts in the available Manus Sandbox.
 
Categorise them:
 
```text
SOURCE
CONFIGURATION
DEPENDENCY
SCRIPT
GENERATED
CACHE
ARCHIVE
DOCUMENTATION
TOOL
UNKNOWN
```
 
For each relevant artefact record:
 
```text
path
type
size
timestamp if available
relationship to Reciter
provenance if determinable
```
 
Do not delete or modify artefacts during investigation.
 
***
 
# 9. TOOL: BASELINE DIFFERENCE
 
Compare:
 
```text
FIRST MODEL / BASELINE
vs
CURRENT BUILD
```
 
Produce:
 
```text
added files
removed files
modified files
renamed files
new dependencies
new tools
new adapters
new configuration
```
 
For modified files, identify the relevant regions where possible.
 
The output should answer:
 
> What entered the build after the first model?

 
***
 
# 10. TOOL: PROVENANCE GRAPH
 
Create a machine-readable provenance graph.
 
Conceptually:
 
```text
BASELINE
   │
   ├── source
   │
   ├── frozen repository component
   │
   ├── external component
   │
   └── unknown
        ↓
MANUS SANDBOX
        ↓
adaptation / wrapper / copy / generated implementation
        ↓
RECITER SOURCE
        ↓
BUILD
        ↓
RUNTIME
```
 
Every edge must have an evidence status:
 
```text
OBSERVED
SUPPORTED
INFERRED
UNKNOWN
```
 
Do not create edges merely because they are architecturally plausible.
 
***
 
# 11. TOOL: NAMED-COMPONENT ANSWER
 
Create a single command/report that can answer:
 
```text
Was Laya actually used?

Was MAF actually used?

Was LHE actually used?

Was CFHM actually used?

Was any implementation copied from the frozen repository?

Was anything modified specifically for the Manus Sandbox?

Were internal tools created?

Which of these are directly supported by surviving evidence?
```
 
The answer must use this structure:
 
```text
COMPONENT:
Laya

DIRECT EXECUTION EVIDENCE:
YES / NO / UNKNOWN

SOURCE-LEVEL EVIDENCE:
[...]

SANDBOX EVIDENCE:
[...]

RUNTIME EVIDENCE:
[...]

PROVENANCE:
[...]

STATUS:
ESTABLISHED / PARTIALLY ESTABLISHED / UNRESOLVED
```
 
Repeat for every component.
 
***
 
# 12. DO NOT FORCE AN ANSWER
 
If the investigation cannot establish whether Manus directly used a component, return:
 
```text
UNRESOLVED
```
 
That is a successful forensic result.
 
The toolset exists to reduce uncertainty, not to eliminate every UNKNOWN artificially.
 
***
 
# 13. PRESERVE RAW RESULTS
 
Every investigation should be capable of producing both:
 
```text
raw/
```
 
and:
 
```text
reports/
```
 
The raw result should preserve machine-observable findings.
 
The report may summarise them.
 
Do not make the report the only surviving record.
 
***
 
# 14. NO SELF-CERTIFICATION
 
The forensic tools must not certify their own conclusions.
 
For example:
 
```text
Tool detects a Laya import
≠
Laya runtime execution proven
```
 
Likewise:
 
```text
Tool finds similar source
≠
copying proven
```
 
and:
 
```text
Tool finds an internal script
≠
Manus created it
```
 
The evidence hierarchy must remain explicit.
 
***
 
# 15. FINAL OUTPUT
 
After creating the tools, run them against the current available build.
 
Produce:
 
```text
provenance/
    raw/
    reports/
    provenance-map.json
```
 
The final report must contain:
 
### A. Established facts
 
Things directly supported by evidence.
 
### B. Strongly supported relationships
 
Relationships supported by multiple technical traces.
 
### C. Unresolved questions
 
Questions for which the available build evidence is insufficient.
 
### D. Missing evidence
 
Specific evidence that would be required to resolve each remaining question.
 
### E. Tool inventory
 
The forensic tools created for future investigation.
 
***
 
# 16. IMPORTANT HISTORICAL RULE
 
Do not modify the Reciter implementation merely to make provenance easier to prove.
 
The forensic toolset must observe the existing build.
 
If an instrumentation change is absolutely necessary for runtime tracing, create it separately and identify it explicitly as:
 
```text
INVESTIGATION INSTRUMENTATION
```
 
Never mix investigation instrumentation with the historical baseline.
 
***
 
# 17. RESEARCH OUTPUT
 
The ultimate result should allow a later lesson to ask:
 
> "Did Manus actually use Laya, or did the build merely contain an implementation associated with Laya?"

 
and receive an answer based on technical evidence rather than memory.
 
Likewise:
 
> "Was this component inherited from the frozen repository?"

 
> "Was it modified in the Sandbox?"

 
> "Did Manus create an internal wrapper?"

 
> "Was the named tool actually executed?"

 
> "Which parts of the current Reciter can be traced to the first model?"

 
The toolset should make these questions **answerable from evidence**.
 
## Core principle
 
> Do not create a tool that tells us what probably happened. Create tools that expose the traces of what actually happened.
