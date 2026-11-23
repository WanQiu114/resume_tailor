# JD match scoring rubric v1.0

Use after every completed resume/CV rewrite and revision, and for explicit scoring audits. This is a transparent local assessment, not an employer ATS result, validated predictor, or probability of passing. Fixed weights and evidence levels support auditability; extracting semantic requirements still requires agent judgment.

## 1. Freeze the JD plan

Read the whole target JD, including responsibilities, required/preferred qualifications, eligibility and logistics. Prefer explicit official section labels over a job-board summary. Before tailoring, save stable requirement and keyword IDs in application.scoring_plan, either with the full group definitions or an explicit local plan-file reference containing those definitions. For a retrospective audit, disclose that no pre-tailoring plan existed, create the full plan now, and reuse it unchanged for later revisions of that JD.

- Cover every substantive requirement. Exclude benefits, company marketing and application-platform noise; explain other exclusions.
- Put each clause in one scoring category only. Eligibility/logistics belong in their own category even if printed under Required.
- Preserve independent obligations. Keep a coherent compound requirement together, with explicit subconditions, or split it before tailoring; document that choice and do not later split/merge to improve the score.
- Preserve the full logical structure. `A OR B OR C` is one group: any complete branch satisfies it. `(C# AND .NET) OR (Node.js AND TypeScript)` requires all terms in either branch, not just C# or Node.js. For AND-only requirements, one component does not satisfy the whole group.
- Repeated mentions and spelling aliases do not add more items. Examples introduced by 'such as', 'e.g.' or 'not expected to have them all' are examples, not a collection of mandatory requirements. Do not silently turn a comma-separated list of distinct duties into OR.
- Build keyword groups independently from the complete JD, not just the candidate's strongest section. Include job-relevant technologies, engineering practices, domain concepts and requested artifacts; omit generic soft-skill adjectives and benefits. Include preferred items but tag their level. Repeated concepts appear once in keyword coverage.
- Normalize only documented aliases or technically equivalent terms (NodeJS/Node.js, RESTful APIs/REST APIs). Explain semantic mappings with exact PDF evidence. AWS does not match Azure; Word proficiency does not prove Microsoft 365 development; a research manuscript does not prove application documentation.
- Once frozen, preserve group IDs, logic, category, aliases, counts and weights across revisions. A changed JD or corrected interpretation requires an explicit plan revision and explanation; no denominator changes to inflate a result.

## 2. Overall match score: 100 points

| Category | Default weight | Scope |
|---|---:|---|
| Required capabilities | 45 | Non-eligibility technical/functional and behavioral requirements explicitly stated as Required |
| Responsibilities | 30 | Concrete duties and deliverables, including depth/context such as production operations |
| Preferred qualifications | 15 | Explicit preferred/bonus/nice-to-have qualifications |
| Eligibility and logistics | 10 | Degree/enrollment/date constraints, required availability, location/attendance, and work authorization only when the JD states it |

Within a category, unique requirement groups have equal weight. Preserve AND subconditions in each group. Apply one evidence level per group:

- **direct = 1**: the final resume/PDF demonstrates the requested capability and relevant scope with supported evidence. For a familiarity requirement, a truthful named skill can suffice; hands-on delivery requirements need a concrete experience/project. Do not invent measures of proficiency or attitude.
- **partial = 0.5**: supported transferable/adjacent experience, incomplete AND conditions, or missing requested context/depth. State exactly what is supported and what is missing. Partial is never counted as direct.
- **gap = 0**: no qualifying evidence or a clear conflict.
- **unknown = 0**: materially unconfirmed. Unknown is not a claim of no experience or automatic rejection.

For eligibility/logistics only, explicit current-application user confirmations may supplement the PDF; label evidence that is not visible in the resume. All other claimed capabilities must be supported in the final resume and grounded in its authorized sources. Template-only facts omitted from the final resume do not earn those points.

For each nonempty category: `earned = effective_weight * sum(group factors) / group_count`.
Overall: sum unrounded category values, then round once to the nearest whole point (half up). Show one-decimal category subtotals for readability and retain exact factors/counts in records; displayed subtotals may differ from the rounded total.

If a category truly has no JD requirements, mark N/A and redistribute its weight proportionally over the other applicable categories, showing original and effective weights. Do not invent requirements to fill categories or award free points. If the posting is too incomplete to score meaningfully, say provisional and list missing information.

## 3. Eligibility gates and document quality

Independently label each explicit hard requirement `met`, `not_met`, or `unconfirmed`; overall gate status is not_met if any gate is not_met, otherwise unconfirmed if any is unconfirmed, otherwise met. A high numerical match does not cancel a failed/unconfirmed gate. Always mention such gates beside the score; do not claim application readiness or screening success based on the total. Thesis completion without a defence is not proof that a degree is awarded or will be completed by start.

Compilation, page count, extraction order and visual quality are separate checks, not job-match points. Do not claim an unreadable/uncompiled PDF was scored from actual extracted text. Score the LaTeX provisionally if needed and label it accordingly.

## 4. Grouped keyword coverage

Evaluate every frozen keyword group against the final PDF text and its supported claims. Record exact excerpts or normalized matches, aliases, and logical operators. Keyword presence is distinct from proving hands-on experience: e.g. a security-research keyword does not establish production security operations. Do not change factual evidence ratings just because a word appears.

- `hit`: any complete OR branch or all required AND components are present through a declared alias/equivalent mapping.
- `partial`: some necessary AND components appear, but no complete branch is satisfied.
- `missing`: no complete match; distinguish absent text from unverified qualifications in notes.
- Report `hit_count / total_group_count * 100`, plus partial and missing counts. Partial groups do not enter the fully-hit numerator. Round percentage to one decimal (half up).
- Do not equate grouped semantic coverage with a proprietary ATS's literal matching, rankings or acceptance.
- Show the denominator definition and main missing groups. Provide the full group list in the paired record so the count can be reproduced.

## 5. Records and chat delivery

Save canonical `scoring.jsonl` and readable `scoring.md` in `resumes/reviews/<stem>/`, with the same essential information:

- task_id, rubric_version, plan_revision, audit_mode and assessment date;
- JD/source/PDF/text hashes, artifact paths, and whether the score uses actual final-PDF text;
- frozen requirement groups with ID, original JD clause/source, category, logic/subconditions, level, evidence/excerpt/source, factor and deduction;
- original/effective category weights, group counts, factor sums, earned points, raw total, rounded overall score, max_score=100 and rounding convention;
- eligibility gates with status, evidence and unresolved details;
- frozen keyword groups with ID, JD source, category/level, alternatives/AND branches, declared aliases, PDF excerpts, hit/partial/missing status, counts and percentage;
- exclusions, assumptions, uncertainties, main deductions, validation and next steps.

Before delivery, verify arithmetic, group counts, complete JD coverage, OR/AND evaluation, provenance hashes and unchanged template files. After any resume revision, regenerate the matching PDF, re-read extraction and recompute; earlier scores remain historical evidence, not current results.

Always show in Chinese chat: **JD match X/100**, category subtotals, **keyword M/N (P%)**, main missing/partial groups, and failed/unconfirmed eligibility gates. State that this is a local rubric score, not an employer ATS score or pass probability. Full LaTeX remains required for actual tailoring; a scoring-only audit does not require a rewrite or reprinting unchanged LaTeX.
