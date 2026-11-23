# Change: Describe the approach, not implementation parameters

## Goal

On 2026-11-20 the user said "Handle AI extraction failures with 90-second timeouts" is too specific and reads as AI-written. A recruiter only needs to know that extraction failures were handled and the general method; exact details belong in the interview.

## Changes

- `skills/resume-tailoring/references/writing-rules.md`: the "Level of Technical Detail" rule now says to describe the approach rather than its parameters, keep exact values in LaTeX comments or review records, and keep outcome numbers (for example `15% higher user engagement`). A matching checklist item was added.
- Gradient application, revision 03: the failure-handling bullet was generalized, and the freed line was used for the Fortrip Python pipeline bullet.

~~~diff
--- writing-rules.md (before)
+++ writing-rules.md (after)
@@ -203,6 +203,8 @@
 
 Omit low-value implementation details that make the work look smaller without making it more accurate. Name a cloud provider and the meaningful services actually used (for example `AWS`, `Amazon S3`), not lightweight hosting product names such as AWS Lightsail. Write `deployed to AWS` rather than `deployed to AWS Lightsail`. Omit version numbers of operating systems, tools, and frameworks (write `Ubuntu`, not `Ubuntu 24.04 LTS`) unless the JD asks for a specific version.
 
+Describe the approach, not its parameters. A recruiter needs to know what problem was handled and the general method, for example `handled AI extraction failures with timeouts, automatic retries, and clear error messages`. Leave exact values (timeout seconds, retry counts, port numbers, file names, record counts in a window) for the interview and keep them in LaTeX comments or review records. Keep numbers that show an outcome or scale, such as `15% higher user engagement` or `34% better alignment`.
+
 Omitting a detail must not create a false impression. Do not name services, scale, traffic, or architecture that were not used (for example EC2, ECS, Kubernetes, multi-region, or high-traffic claims when the system ran on a single instance). Keep source-level details in LaTeX comments and review records for traceability.
 
 After every completed rewrite or revision, report a local JD match score out of 100 and grouped keyword coverage as a count and percentage. Follow `scoring-rubric.md` for fixed weights, evidence levels, OR/AND logic, denominators, eligibility gates and paired scoring records. Do not present this rubric score as an employer ATS score or a screening probability.
@@ -446,6 +448,7 @@
 - In a Resume, do research assistant entries show research direction and outcomes only, without ongoing experiment setup details or supervisor names?
 - Are domain and methodology acronyms (for example ERP, TDD) spelled out as `Full Name (ACRONYM)` at their first occurrence in experience or project text?
 - Are cloud services named at the provider level (AWS, Amazon S3) without lightweight product names such as Lightsail, without unneeded version numbers (for example Ubuntu 24.04 LTS), and without implying services or scale that were not used?
+- Do bullets describe the general approach rather than implementation parameters (exact timeouts, retry counts, ports), while keeping outcome numbers?
 - Can every claim be traced to a template section or an explicit current-application authorization, without automatic historical carryover?
 - Are important keywords supported by actual experience?
 - Are the most relevant skills placed prominently?
~~~

~~~diff
--- revisions/03-before-general-failure-handling/HeYang_Yuan_Resume_Gradient_Junior_Full_Stack_Developer.tex
+++ HeYang_Yuan_Resume_Gradient_Junior_Full_Stack_Developer.tex
@@ -101,8 +101,8 @@
     AI skill against a JSON schema.
 
     % S6 (standing authorization; source-verified gemini.client.ts, product-photo-import.service.ts).
-    \item Handle AI extraction failures with 90-second timeouts, retries for
-    rate-limit and server errors, and error reasons shown on the phone.
+    \item Handle AI extraction failures with timeouts, automatic retries, and
+    clear error messages for users.
 
     \item Build ERP features with Codex and Claude Code, and test agent skills
     against functional tests.
@@ -159,6 +159,9 @@
     \item Integrated RESTful APIs and used Postman to validate destination
     data and API responses.
 
+    \item Built Python pipelines to process JSON data and store structured
+    travel data in PostgreSQL.
+
     \item Built and maintained CI/CD workflows for automated testing and
     deployment.
~~~

## Affected Files

- `skills/resume-tailoring/references/writing-rules.md`
- `resumes/latex/HeYang_Yuan_Resume_Gradient_Junior_Full_Stack_Developer.tex` and its review records; `manifest.jsonl/md` (template snapshot refresh after reviewed change 017)

## Rationale

Implementation values such as timeout seconds add little for screening and make bullets look generated. Outcome numbers still show impact and stay.

## Validation

- Gradient rebuilt: one page, visually inspected, 36 scoring excerpts re-verified, score unchanged at 93/100.
- Templates did not contain the 90-second detail (checked with grep).

## Known Issues

- Earlier tailored resumes (for example Intuit) still contain "90-second" wording; they are unchanged.

## Next Steps

- Apply the rule to all new applications.
