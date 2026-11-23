# Change: Drop unneeded version details (Ubuntu 24.04 LTS -> Ubuntu)

## Goal

On 2026-11-19 the user asked that resumes omit version details such as "Ubuntu 24.04 LTS", because readers understand "Ubuntu" without the version.

## Changes

- `skills/resume-tailoring/references/writing-rules.md`: the "Level of Technical Detail" rule now also omits version numbers of operating systems, tools, and frameworks unless the JD asks for a version; the checklist item was extended.
- `template/resume_template.tex`, `template/CV_template.tex`: the Google Cloud research bullet now says "Ubuntu virtual machines".
- Motorola Solutions application: revision 02 applies the same edit. Its manifest template snapshot was refreshed (reason recorded in manifest.jsonl/md) because the helper blocks builds after a template change; `resume.cls` was unchanged.

~~~diff
--- writing-rules.md (before)
+++ writing-rules.md (after)
@@ -201,7 +201,7 @@
 
 ### Level of Technical Detail
 
-Omit low-value implementation details that make the work look smaller without making it more accurate. Name a cloud provider and the meaningful services actually used (for example `AWS`, `Amazon S3`), not lightweight hosting product names such as AWS Lightsail. Write `deployed to AWS` rather than `deployed to AWS Lightsail`.
+Omit low-value implementation details that make the work look smaller without making it more accurate. Name a cloud provider and the meaningful services actually used (for example `AWS`, `Amazon S3`), not lightweight hosting product names such as AWS Lightsail. Write `deployed to AWS` rather than `deployed to AWS Lightsail`. Omit version numbers of operating systems, tools, and frameworks (write `Ubuntu`, not `Ubuntu 24.04 LTS`) unless the JD asks for a specific version.
 
 Omitting a detail must not create a false impression. Do not name services, scale, traffic, or architecture that were not used (for example EC2, ECS, Kubernetes, multi-region, or high-traffic claims when the system ran on a single instance). Keep source-level details in LaTeX comments and review records for traceability.
 
@@ -445,7 +445,7 @@
 - Were both complete current templates read for this new application?
 - In a Resume, do research assistant entries show research direction and outcomes only, without ongoing experiment setup details or supervisor names?
 - Are domain and methodology acronyms (for example ERP, TDD) spelled out as `Full Name (ACRONYM)` at their first occurrence in experience or project text?
-- Are cloud services named at the provider level (AWS, Amazon S3) without lightweight product names such as Lightsail, and without implying services or scale that were not used?
+- Are cloud services named at the provider level (AWS, Amazon S3) without lightweight product names such as Lightsail, without unneeded version numbers (for example Ubuntu 24.04 LTS), and without implying services or scale that were not used?
 - Can every claim be traced to a template section or an explicit current-application authorization, without automatic historical carryover?
 - Are important keywords supported by actual experience?
 - Are the most relevant skills placed prominently?
~~~

~~~diff
--- template/resume_template.tex (before)
+++ template/resume_template.tex (after)
@@ -203,8 +203,9 @@
     110 variants over 10,000 runs each.
 
     % Linux environment added 2026-11-19 by explicit user statement; see docs/changes/014-linux-environment.md.
+    % OS version (Ubuntu 24.04 LTS) kept out of visible text; see docs/changes/016-drop-version-details.md.
     \item Run research code, experiments, and tests on
-    Ubuntu 24.04 LTS virtual machines on Google Cloud.
+    Ubuntu virtual machines on Google Cloud.
 
     % User-authorized research evaluation and experimental harness experience, 2026-11-13.
     \item Built automated evaluation pipelines with
~~~

~~~diff
--- template/CV_template.tex (before)
+++ template/CV_template.tex (after)
@@ -142,7 +142,7 @@
     % Separate from the paper's agent/context comparisons; raw run logs were not supplied here.
     \item Collected, analyzed, and structured real-world software engineering data from open-source repositories to support empirical studies and benchmark construction.
     % Linux environment added 2026-11-19 by explicit user statement; see docs/changes/014-linux-environment.md.
-    \item Run research code, experiments, and tests on Ubuntu 24.04 LTS virtual machines on Google Cloud.
+    \item Run research code, experiments, and tests on Ubuntu virtual machines on Google Cloud.
     \item Prepared research manuscripts on coding agents, reinforcement learning in the software development lifecycle, and LLM-based logging security analysis.
     % FSE 2026 talk added 2026-11-19 by explicit user authorization; see docs/changes/013-fse-2026-talk.md.
     \item Presented the first-author paper ``Towards Secure Logging: Characterizing and Benchmarking Logging Code Security Issues with LLMs'' at ACM FSE 2026 in Montreal, QC, Canada.
~~~

## Affected Files

- `skills/resume-tailoring/references/writing-rules.md`
- `template/resume_template.tex` (sha256 1c1e639ee30171c5... -> d356d99a0809c9a8...)
- `template/CV_template.tex` (sha256 a0c999c657cb9c3e... -> 068babc9a186f131...)
- `resumes/reviews/HeYang_Yuan_Resume_Motorola_Solutions_Software_Development_2026_Co-Op/manifest.jsonl`, `manifest.md` (template snapshot refresh)

## Rationale

The version number adds no screening value and takes space. The underlying fact (Ubuntu 24.04 LTS on Google Cloud) stays in the LaTeX comment and in this record.

## Validation

- Both templates compiled with tectonic in a scratchpad copy (exit 0; 3 and 4 pages); extracted text contains "Ubuntu virtual machines on Google Cloud" and no "24.04".
- Motorola resume rebuilt: one page, visually inspected; 44 scoring excerpts re-verified; score unchanged at 85/100.

## Known Issues

- Applications prepared before this change will hit the same helper guard if rebuilt; after reviewing the template diff, refresh their manifest snapshot with a recorded reason.

## Next Steps

- None.
