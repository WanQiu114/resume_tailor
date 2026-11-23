# Change: Describe little-known product names (Travedu -> education services web platform)

## Goal

On 2026-11-20 the user pointed out that recruiters do not know what "Travedu" is. Resumes should describe it in general, readable terms (an education services website for a business expansion) and present it at a professional level.

## Changes

- `skills/resume-tailoring/references/writing-rules.md`: "Level of Technical Detail" now says to describe internal or little-known product names by what they are, keep a name with a descriptor only when it adds credibility (for example Snackphoria), keep the original name in a LaTeX comment, and not inflate scale. A checklist item was added.
- `template/resume_template.tex`: Travedu bullets now say "an education services web platform for a new business line" and "the education platform's tutor search filters".
- `template/CV_template.tex`: the tutor filter bullet now says "an education services platform's tutor search filters".
- Gradient application, revision 04: the same general wording.

~~~diff
--- writing-rules.md (before)
+++ writing-rules.md (after)
@@ -205,6 +205,8 @@
 
 Describe the approach, not its parameters. A recruiter needs to know what problem was handled and the general method, for example `handled AI extraction failures with timeouts, automatic retries, and clear error messages`. Leave exact values (timeout seconds, retry counts, port numbers, file names, record counts in a window) for the interview and keep them in LaTeX comments or review records. Keep numbers that show an outcome or scale, such as `15% higher user engagement` or `34% better alignment`.
 
+Describe internal or little-known product names by what they are, because recruiters do not know them. Write `an education services web platform for a new business line`, not `Travedu`. When the name helps credibility (for example a real business using the system), keep it with a short descriptor, as in `Snackphoria, a snack and vending business`. Keep the original name in a LaTeX comment for traceability. Do not inflate scale or audience when generalizing.
+
 Omitting a detail must not create a false impression. Do not name services, scale, traffic, or architecture that were not used (for example EC2, ECS, Kubernetes, multi-region, or high-traffic claims when the system ran on a single instance). Keep source-level details in LaTeX comments and review records for traceability.
 
 After every completed rewrite or revision, report a local JD match score out of 100 and grouped keyword coverage as a count and percentage. Follow `scoring-rubric.md` for fixed weights, evidence levels, OR/AND logic, denominators, eligibility gates and paired scoring records. Do not present this rubric score as an employer ATS score or a screening probability.
@@ -449,6 +451,7 @@
 - Are domain and methodology acronyms (for example ERP, TDD) spelled out as `Full Name (ACRONYM)` at their first occurrence in experience or project text?
 - Are cloud services named at the provider level (AWS, Amazon S3) without lightweight product names such as Lightsail, without unneeded version numbers (for example Ubuntu 24.04 LTS), and without implying services or scale that were not used?
 - Do bullets describe the general approach rather than implementation parameters (exact timeouts, retry counts, ports), while keeping outcome numbers?
+- Are little-known product names (for example Travedu) replaced with a plain description a recruiter understands?
 - Can every claim be traced to a template section or an explicit current-application authorization, without automatic historical carryover?
 - Are important keywords supported by actual experience?
 - Are the most relevant skills placed prominently?
~~~

~~~diff
--- template/resume_template.tex (before)
+++ template/resume_template.tex (after)
@@ -361,14 +361,14 @@
     functionality, resolve bugs, and incorporate
     evolving business and user requirements.
 
+    % Product name "Travedu" kept out of visible text (unknown to recruiters); see docs/changes/020-describe-unknown-product-names.md.
     \item Independently designed, developed, tested,
-    and deployed Travedu, a web application for
-    a separate business initiative, taking
-    ownership of the complete software
-    development lifecycle.
+    and deployed an education services web platform
+    for a new business line, owning the complete
+    software development lifecycle.
 
     \item Used sets to derive unique subject and language
-    options for Travedu tutor filters.
+    options for the education platform's tutor search filters.
 
 \end{itemize}
~~~

~~~diff
--- template/CV_template.tex (before)
+++ template/CV_template.tex (after)
@@ -182,8 +182,9 @@
 \item Designed, integrated, and tested RESTful APIs with Postman to validate endpoint functionality, request handling, and response behavior. 
 \item Collaborated with UX and Marketing teams to implement A/B-tested React UI components, contributing to a 15\% increase in user engagement metrics. 
 \item Debugged and resolved frontend and backend issues across the React, Node.js, Express, and MongoDB application stack. 
+    % Product name "Travedu" kept out of visible text; see docs/changes/020-describe-unknown-product-names.md.
     \item Used sets to derive unique subject and language
-    options for Travedu tutor filters.
+    options for an education services platform's tutor search filters.
 
 \end{itemize}
~~~

## Affected Files

- `skills/resume-tailoring/references/writing-rules.md`
- `template/resume_template.tex` (sha256 5610b55839f36a6e... -> 24427f3b7a9308d4...)
- `template/CV_template.tex` (sha256 41217ac7d259a2ac... -> ad3a4df07dc16560...)
- `resumes/latex/HeYang_Yuan_Resume_Gradient_Junior_Full_Stack_Developer.tex`, its review records, and `manifest.jsonl/md` (snapshot refresh for changes 019 and 020)

## Rationale

"A web application for a separate business initiative" told recruiters nothing. The tutor filters (subjects, languages) show it is an education services platform, and the user describes it as a business expansion, so "new business line" is accurate without claiming users, revenue, or scale.

## Validation

- Both templates compiled with tectonic in a scratchpad copy (exit 0; 3 and 4 pages); extracted text has no "Travedu" and contains the education platform wording.
- Gradient rebuilt: one page, visually inspected, 36 scoring excerpts re-verified, score 93/100.

## Known Issues

- About 37 earlier tailored resumes still mention Travedu; they are unchanged.

## Next Steps

- Apply the rule to all new applications.
