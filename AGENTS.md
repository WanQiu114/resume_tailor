# Resume tailoring workspace

This workspace is HeYang Yuan's personal resume/CV agent, executed by Codex or Claude Code (Claude loads this file through `CLAUDE.md`).
Read `skills/resume-tailoring/SKILL.md` and its writing reference before tailoring.

- `template/` is immutable source evidence and layout guidance. Never modify it. Use `CV_template.tex` for research focused roles and `resume_template.tex` for development focused roles; consider JD responsibilities for mixed titles.
- Save generated sources in `resumes/latex/`, PDFs in `resumes/pdfs/`, and paired JSONL/Markdown application and validation records in `resumes/reviews/<stem>/`. Dependencies are copied per application under `resumes/latex/dependencies/<stem>/`; compilation intermediates belong in `resumes/build/<stem>/`.
- Name outputs `HeYang_Yuan_<CV|Resume>_<Company>_<JobTitle>`. Preserve unrelated applications and prior revisions. Explain in Chinese and always show full final English LaTeX in chat for tailoring requests.
- Compile each revision, extract PDF text, and visually inspect all rendered pages. ATS compatibility is a review of text and structure, never a guaranteed screening outcome. Standard Resume targets one page; CV may exceed one page.
- Never invent skills, achievements, quantitative results, publication status, dates, or eligibility. For each new JD, read both current templates completely and start from a fresh copy of the selected template. Use template evidence plus supplements/corrections authorized for the current application. Do not automatically reuse previous tailored resumes or earlier chat-only facts absent from the templates. Same-application revisions may retain their authorized supplements. Resolve material conflicts with the user.
- After each rewrite/revision, report local JD match X/100 and grouped keyword M/N (percentage) using `skills/resume-tailoring/references/scoring-rubric.md`. Preserve explicit OR/AND logic, stable denominators, evidence-based deductions and separate hard-eligibility gates; save paired scoring records. Never call these employer ATS scores or pass probabilities.
- Use CMD-compatible commands in user instructions. Do not create records for simple informational questions.
- Approved architecture: skill instructions guide analysis/writing; Python helpers copy templates and compile/check artifacts. Routine tailoring does not need design approval again. Changes to this architecture require design review unless immediate implementation is explicitly authorized.
- Maintain implementation notes in `docs/changes/`; important structured records need corresponding readable Markdown with explicit diffs where code is changed.
