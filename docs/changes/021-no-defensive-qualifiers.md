# Change: Present completed results without defensive qualifiers

## Goal

On 2026-11-23 the user asked to remove "(unpublished experiment)" from the resume. A resume presents the candidate's strengths and should not read as an overly cautious disclosure; the qualifier can be explained in an interview.

## Changes

- `skills/resume-tailoring/references/writing-rules.md` (Research Assistant Experience in a Resume): keep only qualifiers that define what a number means, such as the baseline ("relative to native Codex/GPT"). Do not add status or hedging qualifiers such as "(unpublished experiment)", "preliminary", or "in a small study"; keep that status in LaTeX comments and review records. False claims remain forbidden (never call such a result published, peer-reviewed, or production-deployed when it is not). A checklist item was added.
- EvenUp application, revision 01: removed "(unpublished experiment)" from the agent harness bullet; the status stays in the LaTeX comment.

~~~diff
--- writing-rules.md (before)
+++ writing-rules.md (after)
@@ -136,7 +136,9 @@
 - Experiment setup or in-progress experiment details for ongoing work, such as pattern counts, mined commit counts, task counts, variant counts, run counts, or configurations. An ongoing study may be named only as a research direction.
 - "Supervised by <name>" or other supervisor names. Recruiters do not use them.
 
-When a completed result is kept, keep the qualifiers that make it accurate (for example, "relative to" or "unpublished experiment"), but drop setup numbers that do not change its meaning.
+When a completed result is kept, keep only the qualifiers that define what the number means, such as the baseline ("relative to native Codex/GPT"), and drop setup numbers that do not change its meaning.
+
+A resume presents the candidate's strengths; it is not a defensive disclosure. Do not add status or hedging qualifiers such as "(unpublished experiment)", "preliminary", or "in a small study" to completed results. Keep that status in a LaTeX comment and the review record so it can be explained in an interview. This does not permit false claims: never call such a result published, peer-reviewed, or production-deployed when it is not.
 
 ### Internship and Co-op Roles
 
@@ -452,6 +454,7 @@
 - Are cloud services named at the provider level (AWS, Amazon S3) without lightweight product names such as Lightsail, without unneeded version numbers (for example Ubuntu 24.04 LTS), and without implying services or scale that were not used?
 - Do bullets describe the general approach rather than implementation parameters (exact timeouts, retry counts, ports), while keeping outcome numbers?
 - Are little-known product names (for example Travedu) replaced with a plain description a recruiter understands?
+- Are completed results stated confidently, without defensive status qualifiers such as "(unpublished experiment)", while the status stays in comments and records?
 - Can every claim be traced to a template section or an explicit current-application authorization, without automatic historical carryover?
 - Are important keywords supported by actual experience?
 - Are the most relevant skills placed prominently?
~~~

~~~diff
--- revisions/01-before-drop-unpublished/HeYang_Yuan_Resume_EvenUp_Software_Engineer_(New_Grad),_AI_Entities.tex
+++ HeYang_Yuan_Resume_EvenUp_Software_Engineer_(New_Grad),_AI_Entities.tex
@@ -136,10 +136,11 @@
     \item Built LLM-based pipelines to identify and classify logging code
     changes, analyzing nearly 15,000 changes across 240 open-source repositories.
 
-    % User-reported experiment; 34% is a relative alignment improvement, not percentage points.
+    % User-reported unpublished experiment (status kept here, not in visible text, per writing rule 021);
+    % 34% is a relative alignment improvement, not percentage points.
     \item Prototyped a Codex/GPT agent harness that improved alignment with
     validated reference answers by 34\% with 11\% lower runtime relative to
-    native Codex/GPT (unpublished experiment).
+    native Codex/GPT.
 
     \item Trained NLP classification models on over 120,000 reviews with
     PyTorch and Hugging Face; mixed-precision GPU training cut training time
~~~

## Affected Files

- `skills/resume-tailoring/references/writing-rules.md`
- `resumes/latex/HeYang_Yuan_Resume_EvenUp_Software_Engineer_(New_Grad),_AI_Entities.tex` and its review/scoring records

## Rationale

The baseline is part of what "34%" means and stays. The publication status does not change the result and made the bullet defensive. It remains recorded for traceability.

## Validation

- EvenUp rebuilt: one page, visually inspected, extracted text no longer contains "unpublished", 53 scoring excerpts re-verified, score unchanged at 94/100.

## Known Issues

- Resolved by docs/changes/022: both templates no longer state "unpublished" in visible text. Earlier tailored resumes are unchanged.

## Next Steps

- None.
