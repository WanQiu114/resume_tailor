# Change: Remove "unpublished" wording from both templates

## Goal

On 2026-11-23 the user asked to remove the "unpublished experiment" wording from the templates as well, following writing rule change 021 (no defensive status qualifiers on completed results).

## Changes

- `template/resume_template.tex` and `template/CV_template.tex`: the agent harness result now starts "Across 387 logging removal tasks, improved alignment ... by 34% relative to native Codex/GPT ...". The unpublished status moved into the LaTeX comment.

~~~diff
--- template/resume_template.tex (before)
+++ template/resume_template.tex (after)
@@ -243,12 +243,12 @@
     validation retries, and submission after successful
     checks once the agent was ready to submit.
 
-    \item In an unpublished experiment across 387 logging
-    removal tasks, improved alignment with validated
-    reference answers by 34\% relative to native
-    Codex/GPT, with 11\% lower runtime and approximately
-    20\% fewer tokens.
-    % User-reported experiment; 34% is a relative alignment improvement, not percentage points.
+    \item Across 387 logging removal tasks, improved
+    alignment with validated reference answers by 34\%
+    relative to native Codex/GPT, with 11\% lower
+    runtime and approximately 20\% fewer tokens.
+    % User-reported unpublished experiment; status kept in this comment, not visible text (docs/changes/022).
+    % 34% is a relative alignment improvement, not percentage points.
     % Separate from the paper's agent/context comparisons; raw run logs were not supplied here.
 
     \item Evaluated agentic coding workflows across
~~~

~~~diff
--- template/CV_template.tex (before)
+++ template/CV_template.tex (after)
@@ -140,8 +140,9 @@
     \item Build research-specific AI agent skills for each study and iterate them as research requirements and feedback change.
     \item Prototyped a Codex/GPT agent harness with separate tools for code reading, editing, and step logging, and required memory retrieval before edits.
     \item Implemented a 12-record memory window with summary compaction, tool call limits, bounded validation retries, and submission after successful checks once the agent was ready to submit.
-    \item In an unpublished experiment across 387 logging removal tasks, improved alignment with validated reference answers by 34\% relative to native Codex/GPT, with 11\% lower runtime and approximately 20\% fewer tokens.
-    % User-reported experiment; 34% is a relative alignment improvement, not percentage points.
+    \item Across 387 logging removal tasks, improved alignment with validated reference answers by 34\% relative to native Codex/GPT, with 11\% lower runtime and approximately 20\% fewer tokens.
+    % User-reported unpublished experiment; status kept in this comment, not visible text (docs/changes/022).
+    % 34% is a relative alignment improvement, not percentage points.
     % Separate from the paper's agent/context comparisons; raw run logs were not supplied here.
     \item Collected, analyzed, and structured real-world software engineering data from open-source repositories to support empirical studies and benchmark construction.
     % Linux environment added 2026-11-19 by explicit user statement; see docs/changes/014-linux-environment.md.
~~~

## Affected Files

- `template/resume_template.tex` (sha256 24427f3b7a9308d4... -> 9fc25c1604407159...)
- `template/CV_template.tex` (sha256 ad3a4df07dc16560... -> a1e7fa6c3413e556...)

## Rationale

The result, its baseline, and its scale are unchanged; only the defensive status label is removed from visible text. The status remains traceable in the comment and in docs/changes/021.

## Validation

- Both templates compiled with tectonic in a scratchpad copy (exit 0; 3 and 4 pages).
- Extracted text contains "Across 387 logging removal tasks" and no "unpublished".
- Scratchpad copies were deleted after validation.

## Known Issues

- Applications prepared before this change hit the helper's template-snapshot guard if rebuilt; refresh their manifest with a recorded reason after reviewing this diff.
- Earlier tailored resumes are unchanged.

## Next Steps

- None.
