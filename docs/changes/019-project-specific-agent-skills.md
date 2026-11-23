# Change: Project-specific AI agent skills in both templates

## Goal

On 2026-11-20 the user stated that, at work and in research, they build specific agent skills for each project and iterate each skill from feedback until it meets the project or research requirements. The user explicitly authorized writing this into both templates as evidence of AI engineering ability.

## Changes

- Fintelics: the bullet "Iteratively refine skills, prompts, and tools, and compare functional test results and execution efficiency before and after each change" became "Build project-specific AI agent skills, and refine skills, prompts, and tools from user feedback and before-and-after comparisons of functional test results and execution efficiency." The before/after comparison fact is kept.
- York University Research Assistant: new bullet "Build research-specific AI agent skills for each study and iterate them as research requirements and feedback change."

~~~diff
--- template/resume_template.tex (before)
+++ template/resume_template.tex (after)
@@ -102,9 +102,11 @@
     against functional tests to verify task completion
     and identify workflow failures.
 
-    \item Iteratively refine skills, prompts, and tools,
-    and compare functional test results and execution
-    efficiency before and after each change.
+    % Project-specific skills added 2026-11-20 by explicit user authorization; see docs/changes/019-project-specific-agent-skills.md.
+    \item Build project-specific AI agent skills, and refine
+    skills, prompts, and tools from user feedback and
+    before-and-after comparisons of functional test results
+    and execution efficiency.
 
     \item Build frontend features with React,
     TypeScript, and Vite, and implement backend
@@ -220,6 +222,11 @@
 
     \item Compared task outcomes and execution costs after
     changes to methods, skills, prompts, and harnesses.
+
+    % Research-specific skills added 2026-11-20 by explicit user authorization; see docs/changes/019-project-specific-agent-skills.md.
+    \item Build research-specific AI agent skills for each
+    study and iterate them as research requirements and
+    feedback change.
 
     \item Evaluated added task context for Claude Code
     with Sonnet 4.6: reference-change alignment rose
~~~

~~~diff
--- template/CV_template.tex (before)
+++ template/CV_template.tex (after)
@@ -86,7 +86,8 @@
     \item Develop a Python ERP development agent using the OpenAI Codex SDK to create and evolve applications from natural-language requirements and reusable templates.
     % User-authorized agent evaluation experience, 2026-11-13; see docs/changes/010-agent-evaluation-harness.md.
     \item Evaluate ERP agent skills, prompts, and tools against functional tests to verify task completion and identify workflow failures.
-    \item Iteratively refine skills, prompts, and tools, and compare functional test results and execution efficiency before and after each change.
+    % Project-specific skills added 2026-11-20 by explicit user authorization; see docs/changes/019-project-specific-agent-skills.md.
+    \item Build project-specific AI agent skills, and refine skills, prompts, and tools from user feedback and before-and-after comparisons of functional test results and execution efficiency.
     % Source-verified additions authorized on 2026-11-03; see docs/changes/003-fintelics-template-evidence.md.
     % Review gates are implemented capabilities, not evidence of personal peer-review participation.
     % Database scaling is a future design path, not a completed RDS migration or load-test result.
@@ -135,6 +136,8 @@
     % User-authorized research evaluation experience, 2026-11-13.
     \item Built automated evaluation pipelines with functional tests defined before agent runs to assess task completion and preserve software functionality, following TDD principles.
     \item Analyzed execution trajectories for task adherence, out-of-scope tool calls, and redundant actions; measured token usage, tool calls, and runtime after changes to methods, skills, prompts, and harnesses.
+    % Research-specific skills added 2026-11-20 by explicit user authorization; see docs/changes/019-project-specific-agent-skills.md.
+    \item Build research-specific AI agent skills for each study and iterate them as research requirements and feedback change.
     \item Prototyped a Codex/GPT agent harness with separate tools for code reading, editing, and step logging, and required memory retrieval before edits.
     \item Implemented a 12-record memory window with summary compaction, tool call limits, bounded validation retries, and submission after successful checks once the agent was ready to submit.
     \item In an unpublished experiment across 387 logging removal tasks, improved alignment with validated reference answers by 34\% relative to native Codex/GPT, with 11\% lower runtime and approximately 20\% fewer tokens.
~~~

## Affected Files

- `template/resume_template.tex` (sha256 b807f9d38a876029... -> 5610b55839f36a6e...)
- `template/CV_template.tex` (sha256 5fc7fc9debfb4d85... -> 41217ac7d259a2ac...)

## Rationale

The new wording states the mechanism (project-specific skills, feedback, measured before/after comparisons) instead of a work habit. Tailored resumes may explain "agent skills" for non-technical readers, for example "reusable instructions and tools for AI coding agents", when space allows.

## Validation

- Both templates compiled with tectonic in a scratchpad copy (exit 0; 3 and 4 pages).
- Extracted text contains both new bullets and no longer contains "Iteratively refine".
- Scratchpad copies were deleted after validation.

## Known Issues

- Applications prepared before this change will hit the helper's template-snapshot guard if rebuilt; refresh their manifest with a recorded reason after reviewing this diff.
- Existing tailored resumes are unchanged.

## Next Steps

- Prefer these bullets for AI, agent, and "developing with AI" roles; keep at most one of them for testing or traditional development roles.
