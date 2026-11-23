# 002-Jd-Match-Scoring

## task_id

resume-scoring-002

## goal

Require auditable 100-point JD matching and fair grouped keyword reporting after every rewrite.

## changes

```json
[
  "Added scoring-rubric.md with fixed weights, explicit evidence levels, OR/AND logic, stable denominators and eligibility gates.",
  "Updated skill entrypoint, writing rules, project guidance and README; removed conflict with blanket prohibition on numeric local scoring.",
  "Added a required final-PDF scoring step and paired scoring records."
]
```

## affected_files

```json
[
  "skills/resume-tailoring/SKILL.md",
  "skills/resume-tailoring/references/writing-rules.md",
  "AGENTS.md",
  "README.md",
  "skills/resume-tailoring/references/scoring-rubric.md"
]
```

## rationale

User requests strict local scores and OR alternatives counted as one requirement; previous ad hoc keyword denominators were misleading.

## expected_behavior

Each completed rewrite/revision reports local JD score out of 100, grouped keyword M/N/percentage, item-level deductions and eligibility uncertainty in Chinese chat.

## assumptions

```json
[
  "Codex performs semantic requirement grouping/evidence assessment; existing Python utilities handle artifacts. No new service or scoring engine architecture introduced.",
  "Scores describe an explicit local rubric, not employer rules or calibrated hiring probabilities."
]
```

## validation

```json
{
  "status": "passed",
  "template_integrity": true,
  "template_hashes": {
    "CV_template.tex": "25da6b9aaa25a41c8eef336114d4b87cb4c808d7d8f82e1aee8e79847e4ed20a",
    "resume.cls": "c9e31264abeb306e3e672b0aca01ae3d80a423ca36425bdb453570cc0a09e6bf",
    "resume_template.tex": "200b090f39937b830fa8653adbc2f6db88b1f8d5eb06d1dd23b7ec25886a0c4b"
  },
  "canonical_skill_structure": "passed",
  "installed_skill_structure": "passed",
  "installed_files_identical": true,
  "workspace_binding_verified": true,
  "PRI_score_arithmetic": "76.25 raw, 76/100 rounded",
  "PRI_keywords": "14/19 = 73.7%; 0 partial, 5 missing",
  "OR_AND_example": "Complete Node.js AND TypeScript alternative hits without C#/.NET; AWS does not hit Azure.",
  "PRI_final_artifact_hashes": "Source, PDF and JD hashes verified; no resume/PDF regeneration or edits.",
  "paired_records": "All essential JSONL keys preserved in Markdown, with visible instruction diffs and human scoring tables."
}
```

## known_issues

```json
[
  "Semantic grouping and evidence strength require agent judgment despite fixed arithmetic.",
  "Actual employer ATS criteria are unavailable."
]
```

## next_steps

```json
[
  "Apply this scoring requirement after each future rewrite/revision, keeping JD plan groups stable.",
  "Reassess PRI eligibility only after current-application facts confirm degree-completion timing and office attendance."
]
```

## unified_diff

```diff
--- skills/resume-tailoring/SKILL.md
+++ skills/resume-tailoring/SKILL.md
@@ -19,12 +19,12 @@
 
 ## Workflow
 
-1. For a new application, first complete the full-template read and evidence inventory above. Map required/preferred qualifications to direct matches, partial matches, and gaps. Check eligibility and extra application materials, consulting the official application page when supplied and accessible. Keep unknowns explicit.
+1. For a new application, first complete the full-template read and evidence inventory above. Read [the scoring rubric](references/scoring-rubric.md), extract and freeze the complete JD requirement groups and keyword groups in the application record before tailoring. Map required/preferred qualifications to direct matches, partial matches, and gaps. Check eligibility and extra application materials, consulting the official application page when supplied and accessible. Keep unknowns explicit.
 2. Run the bundled helper (paths below are relative to the skill folder):
    ```cmd
    python scripts\resume_workflow.py prepare --workspace "D:\github_project\resume_tailor" --kind Resume --company "Microsoft" --title "Software Engineer"
    ```
-   Substitute actual inputs and the resolved workspace. This copies the selected template and its dependencies, saves input provenance, and returns the output path. Save the entire pasted posting verbatim (including interface noise) under `resumes/reviews/<stem>/jd.txt`; record the supplied posting URL and matching analysis in paired `application.jsonl` and `application.md` there. These application records must contain the same essential fields: task_id, company, job_title, kind, jd_file, posting_url, extracted_input (company_evidence/title_evidence/jd_scope/ignored_noise/uncertainties), template, evidence_scope (templates_read/current_application_supplements/excluded_historical_facts), requirement_matches (requirement/evidence/source/match), gaps, materials (item/status/source), eligibility, assumptions, and unresolved_issues. Use required/optional/not_mentioned/unable_to_verify for material status.
+   Substitute actual inputs and the resolved workspace. This copies the selected template and its dependencies, saves input provenance, and returns the output path. Save the entire pasted posting verbatim (including interface noise) under `resumes/reviews/<stem>/jd.txt`; record the supplied posting URL and matching analysis in paired `application.jsonl` and `application.md` there. These application records must contain the same essential fields: task_id, company, job_title, kind, jd_file, posting_url, extracted_input (company_evidence/title_evidence/jd_scope/ignored_noise/uncertainties), template, evidence_scope (templates_read/current_application_supplements/excluded_historical_facts), requirement_matches (requirement/evidence/source/match), gaps, materials (item/status/source), eligibility, scoring_plan (rubric_version/requirement_groups/keyword_groups), assumptions, and unresolved_issues. Use required/optional/not_mentioned/unable_to_verify for material status.
 3. Edit only the generated `.tex` and copied dependencies if necessary. Never edit `template/`. Preserve the original header, margins, fonts, confirmed names/dates, and class. Prefer source-only fixes; document any dependency changes and the reason. Use the selected template as the starting point, not a previous employer's tailored draft. On an explicit revision of the same application, modify its existing `.tex` and retain its authorized supplements; this exception does not carry content into a different JD/application. Do not prepare a new application for that revision. Back up the previous source and PDF under its review directory before editing.
 4. Use `HeYang_Yuan_<CV|Resume>_<Company>_<JobTitle>` for both `.tex` and `.pdf`. Spaces become underscores, invalid Windows characters are removed. Different applications with the same stem get `_02`, `_03`, etc.; never silently overwrite one. Preserve the original company/title in records.
 5. Compile after every substantive revision:
@@ -34,12 +34,13 @@
    The helper stages dependencies outside `template/`, compiles, publishes a matching PDF, extracts text, renders every page, and creates paired `validation.jsonl` / `validation.md`. It verifies template hashes and source/PDF provenance. It does not evaluate qualifications or certify ATS acceptance.
 6. Read extracted text in order and inspect **all** rendered PNGs using image viewing tools. Check names/dates/headings, keyword integrity, page boundaries, overlap, short wrapped lines, and bottom whitespace. One page alone does not establish good layout or adequate content. CV has no one-page limit. Use layout evidence to make targeted edits and rebuild; do not add filler or aggressively shrink fonts. Default experience heading spacing is `\vspace{-1.6em}` but adjust a copy when actual PDF layout requires it, especially when a technologies line intervenes.
 7. Record actual visual review and content review in paired `review.jsonl` and `review.md` under that application's review directory. Include task_id, source_sha256, pdf_sha256, visual_status, reading_order_status, factual_checks (trace every retained claim to a current template section or current-application authorization; remove unsupported carryover), changes, unified_diff (against the saved previous source or selected template), warnings, and next_steps. A helper success is not human/agent visual approval. If edits occur after inspection, rebuild and inspect again.
-8. Always display the **entire final `.tex` verbatim in one LaTeX code block in chat**, even though files are saved locally. Briefly state match/gaps, template choice, important edits, extra materials, and actual compilation/layout status in Chinese. Explain that `resume.cls` and copied assets are also required in Overleaf. File links supplement rather than replace the code block. For feedback-only requests, give feedback without generating files or full source.
+8. After each completed rewrite/revision, score the final PDF against the frozen JD plan using [the scoring rubric](references/scoring-rubric.md). Save paired `scoring.jsonl` / `scoring.md` with item-level evidence, arithmetic, source/PDF/JD hashes, deductions and eligibility gates. Always report in chat **overall JD match X/100**, category subtotals, **keyword groups M/N (percentage)**, partial/missing groups and unresolved hard requirements. OR alternatives count once when any complete alternative is met; AND components must all be supported. These are local rubric results, never employer ATS scores or pass probabilities. Recompute after any source/PDF revision; never reuse a stale score.
+9. Always display the **entire final `.tex` verbatim in one LaTeX code block in chat**, even though files are saved locally. Briefly state match/gaps, template choice, important edits, extra materials, and actual compilation/layout status in Chinese. Explain that `resume.cls` and copied assets are also required in Overleaf. File links supplement rather than replace the code block. For feedback-only requests, give feedback without generating files or full source; an explicitly requested scoring audit may create paired scoring records without rewriting the resume.
 
 ## Tooling and continuity
 
 - Helper requires Python 3.10+, a LaTeX engine (prefers workspace `tools/tectonic/tectonic.exe`, then PATH), and PyMuPDF (`pymupdf`) for PDF text/rendering. The helper also checks `tools/python/` for locally installed Python dependencies.
 - Engine override: `build --engine "C:\path\to\xelatex.exe"`. Do not enable shell escape. Tectonic may download TeX resources on first compilation. Do not upload personal resume content to a remote compilation service.
-- If compilation/dependencies fail, preserve source, logs and explicit failure records; say PDF validation is incomplete. An older PDF must never be represented as current. Do not fabricate a PDF or ATS score.
+- If compilation/dependencies fail, preserve source, logs and explicit failure records; say PDF validation is incomplete. An older PDF must never be represented as current. Do not fabricate a PDF, employer ATS score or screening probability. The required local JD/keyword assessment must follow the documented rubric.
 - On continuation, re-read the current application records to recover its approved state. For a new application, reset the evidence scope to the complete current templates and current-application instructions; previous confirmations and review history do not become a shared experience pool. Historical records remain audit trails. Never persist unconfirmed claims as facts.
 - This workflow is already approved. Routine tailoring/revisions do not require a fresh architecture approval; ask only for missing material facts or a genuinely new design decision. Do not submit applications or send materials to others.

--- skills/resume-tailoring/references/writing-rules.md
+++ skills/resume-tailoring/references/writing-rules.md
@@ -182,7 +182,7 @@
 - Certifications.
 - Employment responsibilities.
 
-Do not generate numerical ATS compatibility scores unless a real scoring system is available.
+After every completed rewrite or revision, report a local JD match score out of 100 and grouped keyword coverage as a count and percentage. Follow `scoring-rubric.md` for fixed weights, evidence levels, OR/AND logic, denominators, eligibility gates and paired scoring records. Do not present this rubric score as an employer ATS score or a screening probability.
 
 Never guarantee that a resume will pass an ATS or AI screening process.
 
@@ -407,7 +407,7 @@
 Save complete LaTeX in resumes/latex/ and a matching compiled PDF in resumes/pdfs/.
 Always also display the entire final LaTeX source in chat for Overleaf.
 Include concise match analysis, gaps, important edits, additional application materials,
-and unresolved eligibility/verification issues. File links never replace the full code.
+and unresolved eligibility/verification issues. Always include overall JD match X/100, category subtotals, keyword groups M/N (percentage), and the main deductions under `scoring-rubric.md`. File links never replace the full code.
 Feedback-only requests need no files or full rewrite. Revisions preserve correct content.
 Use the workspace workflow in SKILL.md for template selection, filenames, dependency
 copies, provenance, validation records, and immutable template handling.
@@ -433,6 +433,8 @@
 - Was the actual PDF checked if possible?
 - Were additional application materials explicitly reviewed?
 - Were important eligibility issues identified?
+- Were the final PDF match score out of 100, grouped keyword numerator/denominator/percentage, deductions, and eligibility gates reported in chat?
+- Were OR alternatives counted as one group and complete AND branches checked, without changing the denominator to improve the score?
 - Is the complete LaTeX code directly copyable?
 
 Prioritize accuracy, job relevance, readability, and consistency over maximizing the number of keywords.

--- AGENTS.md
+++ AGENTS.md
@@ -8,6 +8,7 @@
 - Name outputs `HeYang_Yuan_<CV|Resume>_<Company>_<JobTitle>`. Preserve unrelated applications and prior revisions. Explain in Chinese and always show full final English LaTeX in chat for tailoring requests.
 - Compile each revision, extract PDF text, and visually inspect all rendered pages. ATS compatibility is a review of text and structure, never a guaranteed screening outcome. Standard Resume targets one page; CV may exceed one page.
 - Never invent skills, achievements, quantitative results, publication status, dates, or eligibility. For each new JD, read both current templates completely and start from a fresh copy of the selected template. Use template evidence plus supplements/corrections authorized for the current application. Do not automatically reuse previous tailored resumes or earlier chat-only facts absent from the templates. Same-application revisions may retain their authorized supplements. Resolve material conflicts with the user.
+- After each rewrite/revision, report local JD match X/100 and grouped keyword M/N (percentage) using `skills/resume-tailoring/references/scoring-rubric.md`. Preserve explicit OR/AND logic, stable denominators, evidence-based deductions and separate hard-eligibility gates; save paired scoring records. Never call these employer ATS scores or pass probabilities.
 - Use CMD-compatible commands in user instructions. Do not create records for simple informational questions.
 - Approved architecture: skill instructions guide analysis/writing; Python helpers copy templates and compile/check artifacts. Routine tailoring does not need design approval again. Changes to this architecture require design review unless immediate implementation is explicitly authorized.
 - Maintain implementation notes in `docs/changes/`; important structured records need corresponding readable Markdown with explicit diffs where code is changed.

--- README.md
+++ README.md
@@ -17,6 +17,8 @@
 `template/` 中的三个文件始终保持不变：研究岗位以 `CV_template.tex` 为起点；开发岗位以 `resume_template.tex` 为起点。混合岗位根据 JD 的主要职责判断。两种模板都使用 `resume.cls`。用户明确选择优先。
 
 每个新岗位都会重新完整读取两份原始模板，并复制所选模板后定制。不会沿用上一岗位的简历作为底稿，也不会自动带入只在之前聊天或申请记录中出现、尚未写入模板的经历；这类补充需要你明确授权用于当前申请。同一申请的后续修订可保留该申请已确认的补充。`template/` 不会自动更新。
+
+每次改写后，聊天中还会报告岗位匹配评分（满分 100）和关键词要求组命中数/总数/百分比。固定权重为必需能力 45、岗位职责 30、加分项 15、资格与到岗条件 10；直接匹配计 1，部分匹配计 0.5，缺失或未确认计 0。A or B or C 只算一组，命中一个完整选项即可；AND 条件需全部满足。硬性资格单独标记，关键词覆盖率不等于 ATS 分数或通过概率。分组、证据和扣分保存在申请 review 目录的 `scoring.jsonl` / `scoring.md`，详细规则见 `skills/resume-tailoring/references/scoring-rubric.md`。
 
 输出示例：
 

--- /dev/null
+++ skills/resume-tailoring/references/scoring-rubric.md
@@ -0,0 +1,72 @@
+# JD match scoring rubric v1.0
+
+Use after every completed resume/CV rewrite and revision, and for explicit scoring audits. This is a transparent local assessment, not an employer ATS result, validated predictor, or probability of passing. Fixed weights and evidence levels support auditability; extracting semantic requirements still requires agent judgment.
+
+## 1. Freeze the JD plan
+
+Read the whole target JD, including responsibilities, required/preferred qualifications, eligibility and logistics. Prefer explicit official section labels over a job-board summary. Before tailoring, save stable requirement and keyword IDs in application.scoring_plan. For a retrospective audit, disclose that no pre-tailoring plan existed, create the full plan now, and reuse it unchanged for later revisions of that JD.
+
+- Cover every substantive requirement. Exclude benefits, company marketing and application-platform noise; explain other exclusions.
+- Put each clause in one scoring category only. Eligibility/logistics belong in their own category even if printed under Required.
+- Preserve independent obligations. Keep a coherent compound requirement together, with explicit subconditions, or split it before tailoring; document that choice and do not later split/merge to improve the score.
+- Preserve the full logical structure. `A OR B OR C` is one group: any complete branch satisfies it. `(C# AND .NET) OR (Node.js AND TypeScript)` requires all terms in either branch, not just C# or Node.js. For AND-only requirements, one component does not satisfy the whole group.
+- Repeated mentions and spelling aliases do not add more items. Examples introduced by 'such as', 'e.g.' or 'not expected to have them all' are examples, not a collection of mandatory requirements. Do not silently turn a comma-separated list of distinct duties into OR.
+- Build keyword groups independently from the complete JD, not just the candidate's strongest section. Include job-relevant technologies, engineering practices, domain concepts and requested artifacts; omit generic soft-skill adjectives and benefits. Include preferred items but tag their level. Repeated concepts appear once in keyword coverage.
+- Normalize only documented aliases or technically equivalent terms (NodeJS/Node.js, RESTful APIs/REST APIs). Explain semantic mappings with exact PDF evidence. AWS does not match Azure; Word proficiency does not prove Microsoft 365 development; a research manuscript does not prove application documentation.
+- Once frozen, preserve group IDs, logic, category, aliases, counts and weights across revisions. A changed JD or corrected interpretation requires an explicit plan revision and explanation; no denominator changes to inflate a result.
+
+## 2. Overall match score: 100 points
+
+| Category | Default weight | Scope |
+|---|---:|---|
+| Required capabilities | 45 | Non-eligibility technical/functional and behavioral requirements explicitly stated as Required |
+| Responsibilities | 30 | Concrete duties and deliverables, including depth/context such as production operations |
+| Preferred qualifications | 15 | Explicit preferred/bonus/nice-to-have qualifications |
+| Eligibility and logistics | 10 | Degree/enrollment/date constraints, required availability, location/attendance, and work authorization only when the JD states it |
+
+Within a category, unique requirement groups have equal weight. Preserve AND subconditions in each group. Apply one evidence level per group:
+
+- **direct = 1**: the final resume/PDF demonstrates the requested capability and relevant scope with supported evidence. For a familiarity requirement, a truthful named skill can suffice; hands-on delivery requirements need a concrete experience/project. Do not invent measures of proficiency or attitude.
+- **partial = 0.5**: supported transferable/adjacent experience, incomplete AND conditions, or missing requested context/depth. State exactly what is supported and what is missing. Partial is never counted as direct.
+- **gap = 0**: no qualifying evidence or a clear conflict.
+- **unknown = 0**: materially unconfirmed. Unknown is not a claim of no experience or automatic rejection.
+
+For eligibility/logistics only, explicit current-application user confirmations may supplement the PDF; label evidence that is not visible in the resume. All other claimed capabilities must be supported in the final resume and grounded in its authorized sources. Template-only facts omitted from the final resume do not earn those points.
+
+For each nonempty category: `earned = effective_weight * sum(group factors) / group_count`.
+Overall: sum unrounded category values, then round once to the nearest whole point (half up). Show one-decimal category subtotals for readability and retain exact factors/counts in records; displayed subtotals may differ from the rounded total.
+
+If a category truly has no JD requirements, mark N/A and redistribute its weight proportionally over the other applicable categories, showing original and effective weights. Do not invent requirements to fill categories or award free points. If the posting is too incomplete to score meaningfully, say provisional and list missing information.
+
+## 3. Eligibility gates and document quality
+
+Independently label each explicit hard requirement `met`, `not_met`, or `unconfirmed`; overall gate status is not_met if any gate is not_met, otherwise unconfirmed if any is unconfirmed, otherwise met. A high numerical match does not cancel a failed/unconfirmed gate. Always mention such gates beside the score; do not claim application readiness or screening success based on the total. Thesis completion without a defence is not proof that a degree is awarded or will be completed by start.
+
+Compilation, page count, extraction order and visual quality are separate checks, not job-match points. Do not claim an unreadable/uncompiled PDF was scored from actual extracted text. Score the LaTeX provisionally if needed and label it accordingly.
+
+## 4. Grouped keyword coverage
+
+Evaluate every frozen keyword group against the final PDF text and its supported claims. Record exact excerpts or normalized matches, aliases, and logical operators. Keyword presence is distinct from proving hands-on experience: e.g. a security-research keyword does not establish production security operations. Do not change factual evidence ratings just because a word appears.
+
+- `hit`: any complete OR branch or all required AND components are present through a declared alias/equivalent mapping.
+- `partial`: some necessary AND components appear, but no complete branch is satisfied.
+- `missing`: no complete match; distinguish absent text from unverified qualifications in notes.
+- Report `hit_count / total_group_count * 100`, plus partial and missing counts. Partial groups do not enter the fully-hit numerator. Round percentage to one decimal (half up).
+- Do not equate grouped semantic coverage with a proprietary ATS's literal matching, rankings or acceptance.
+- Show the denominator definition and main missing groups. Provide the full group list in the paired record so the count can be reproduced.
+
+## 5. Records and chat delivery
+
+Save canonical `scoring.jsonl` and readable `scoring.md` in `resumes/reviews/<stem>/`, with the same essential information:
+
+- task_id, rubric_version, plan_revision, audit_mode and assessment date;
+- JD/source/PDF/text hashes, artifact paths, and whether the score uses actual final-PDF text;
+- frozen requirement groups with ID, original JD clause/source, category, logic/subconditions, level, evidence/excerpt/source, factor and deduction;
+- original/effective category weights, group counts, factor sums, earned points, raw total, rounded overall score, max_score=100 and rounding convention;
+- eligibility gates with status, evidence and unresolved details;
+- frozen keyword groups with ID, JD source, category/level, alternatives/AND branches, declared aliases, PDF excerpts, hit/partial/missing status, counts and percentage;
+- exclusions, assumptions, uncertainties, main deductions, validation and next steps.
+
+Before delivery, verify arithmetic, group counts, complete JD coverage, OR/AND evaluation, provenance hashes and unchanged template files. After any resume revision, regenerate the matching PDF, re-read extraction and recompute; earlier scores remain historical evidence, not current results.
+
+Always show in Chinese chat: **JD match X/100**, category subtotals, **keyword M/N (P%)**, main missing/partial groups, and failed/unconfirmed eligibility gates. State that this is a local rubric score, not an employer ATS score or pass probability. Full LaTeX remains required for actual tailoring; a scoring-only audit does not require a rewrite or reprinting unchanged LaTeX.

--- skills\resume-tailoring\references\scoring-rubric.md
+++ skills\resume-tailoring\references\scoring-rubric.md
@@ -4,7 +4,7 @@
 
 ## 1. Freeze the JD plan
 
-Read the whole target JD, including responsibilities, required/preferred qualifications, eligibility and logistics. Prefer explicit official section labels over a job-board summary. Before tailoring, save stable requirement and keyword IDs in application.scoring_plan. For a retrospective audit, disclose that no pre-tailoring plan existed, create the full plan now, and reuse it unchanged for later revisions of that JD.
+Read the whole target JD, including responsibilities, required/preferred qualifications, eligibility and logistics. Prefer explicit official section labels over a job-board summary. Before tailoring, save stable requirement and keyword IDs in application.scoring_plan, either with the full group definitions or an explicit local plan-file reference containing those definitions. For a retrospective audit, disclose that no pre-tailoring plan existed, create the full plan now, and reuse it unchanged for later revisions of that JD.
 
 - Cover every substantive requirement. Exclude benefits, company marketing and application-platform noise; explain other exclusions.
 - Put each clause in one scoring category only. Eligibility/logistics belong in their own category even if printed under Required.

```

## updated_at

2026-11-03T17:10:19.579339+00:00

## PRI_audit

```json
{
  "file": "resumes/reviews/HeYang_Yuan_Resume_PRI_Junior_Software_Developer/scoring.jsonl",
  "overall_score": 76,
  "max_score": 100,
  "keyword_hits": 14,
  "keyword_groups": 19,
  "keyword_percent": 73.7,
  "eligibility_status": "unconfirmed"
}
```
