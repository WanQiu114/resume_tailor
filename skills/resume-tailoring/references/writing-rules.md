# Resume Tailoring Skill

## 1. Objective

Tailor the user's existing resume to a specific Job Description (JD).

Optimize the resume for:
- Applicant Tracking Systems (ATS).
- AI-assisted resume screening.
- Relevance to the target position.
- Human recruiter readability.
- Accurate representation of experience.
- Professional LaTeX formatting.

The goal is to improve job relevance and screening compatibility without exaggerating or fabricating qualifications.

For every new application, start from the complete current original templates and the current JD. Apply only supplements/corrections authorized for that application, together with the user's formatting preferences.

## 2. Required Inputs

Use the following inputs when available:

1. Target Job Description.
2. Complete current `resume_template.tex` and `CV_template.tex`, both read in full.
3. Original `resume.cls` and the selected template for layout.
4. Professional experience explicitly supplied or authorized for the current application.
5. The current application's compiled PDF for layout inspection.
6. Additional instructions supplied by the user.

Current-application user corrections override template facts. Do not use previous tailored resumes, PDFs, application records, or earlier chat-only confirmations as the factual baseline for a new JD. Facts absent from the templates need current-application authorization before reuse. See SKILL.md for the full evidence-scope and same-application revision rules.

Do not change employment dates, graduation dates, job titles, academic status, or personal information without evidence or explicit instructions.

If the user provides a PDF but not its LaTeX source, use the PDF to understand the content and structure. Do not assume an exact reconstruction of the original LaTeX template is possible.

## 3. Job Description Analysis

Before rewriting the resume:

1. Identify the role, seniority, location, and employment type.
2. Extract required technical skills.
3. Extract preferred technical skills.
4. Identify responsibilities and engineering practices.
5. Identify relevant domain knowledge.
6. Identify eligibility requirements and application deadlines.
7. Map each requirement to the user's documented experience.

Prioritize qualifications in this order:

1. Required skills supported by actual experience.
2. Relevant engineering responsibilities.
3. Preferred skills supported by actual experience.
4. Relevant projects, research, and measurable achievements.

Distinguish between:

- Direct match: demonstrated in work or projects.
- Partial match: related experience but not identical technology.
- Gap: no documented experience.

Never describe a partial match as direct experience.

Do not invent skills or add technologies merely because they appear in the JD.

## 4. Resume Tailoring Strategy

### Software Engineering Roles

Prioritize:

- Software development experience.
- Programming languages.
- Full-stack and backend development.
- REST APIs and database integration.
- Automated testing.
- CI/CD and deployment.
- Debugging and troubleshooting.
- Cross-functional collaboration.
- Production-oriented engineering practices.

Generally remove Publications from a one-page software engineering resume unless the publication is particularly relevant to the role.

### AI / Agent Engineering Roles

Prioritize:

- LLM applications.
- AI coding agents.
- Agentic workflows.
- Tool calling and API integration.
- Agent orchestration.
- Python development.
- Evaluation pipelines.
- Automated testing.
- RAG and context engineering.
- Full-stack AI application development.

Distinguish clearly between:

- Building AI applications.
- Developing AI agents.
- Evaluating coding agents.
- Using AI coding tools during development.

Do not merge distinct projects or imply the user implemented capabilities that were only studied or evaluated.

### Research Roles

Prioritize:

- Research experience.
- Research interests.
- Publications.
- Benchmark construction.
- Experimental methodology.
- Quantitative results.
- Research software and evaluation pipelines.
- Relevant academic projects.

For research-oriented positions, use the user's academic CV when appropriate.

An academic CV may exceed one page. Do not apply the one-page resume rule when a detailed research CV is explicitly requested.

### Research Assistant Experience in a Resume

This rule applies to **Resume** outputs only. A research **CV** may keep supervisors and experiment detail.

In a Resume, describe each research assistant role by:

- Its research direction or area (for example, AI for software engineering, LLM-based coding agents, agent evaluation, logging code maintenance).
- Its research outcomes: published or under-review papers, released benchmarks or tools, and completed results that recruiters can read without background knowledge.
- Engineering work that is relevant to the JD (for example, evaluation pipelines or an agent harness) and its completed result.

Do not include:

- Experiment setup or in-progress experiment details for ongoing work, such as pattern counts, mined commit counts, task counts, variant counts, run counts, or configurations. An ongoing study may be named only as a research direction.
- "Supervised by <name>" or other supervisor names. Recruiters do not use them.

When a completed result is kept, keep only the qualifiers that define what the number means, such as the baseline ("relative to native Codex/GPT"), and drop setup numbers that do not change its meaning.

A resume presents the candidate's strengths; it is not a defensive disclosure. Do not add status or hedging qualifiers such as "(unpublished experiment)", "preliminary", or "in a small study" to completed results. Keep that status in a LaTeX comment and the review record so it can be explained in an interview. This does not permit false claims: never call such a result published, peer-reviewed, or production-deployed when it is not.

### Internship and Co-op Roles

Check:

- Academic enrollment requirements.
- Expected graduation date requirements.
- Internship duration.
- Required availability.
- Degree-level restrictions.
- Work authorization requirements.

Do not assume planned PhD enrollment satisfies eligibility requirements.

## 5. ATS and AI Screening Optimization

Use standard resume section headings:

- EDUCATION
- TECHNICAL SKILLS
- PROFESSIONAL EXPERIENCE
- RESEARCH EXPERIENCE
- PUBLICATIONS

Only include sections appropriate for the role.

Use technology names that match the JD when they accurately describe the user's experience.

Examples:
- React
- TypeScript
- JavaScript
- Python
- Node.js
- PostgreSQL
- REST APIs
- Docker
- CI/CD
- Playwright

Include relevant keywords naturally in both Technical Skills and experience bullets when supported by evidence.

Each important keyword should ideally be connected to an actual project or responsibility.

Prefer specific evidence:

"Developed React and TypeScript features for an ERP application backed by PostgreSQL."

Avoid unsupported keyword stuffing:

"Expert in React, GraphQL, Kubernetes, AWS, Azure, and every modern technology."

Do not invent:
- Technologies.
- Years of experience.
- Performance improvements.
- Project outcomes.
- Team leadership.
- Publications.
- Certifications.
- Employment responsibilities.

### Level of Technical Detail

Omit low-value implementation details that make the work look smaller without making it more accurate. Name a cloud provider and the meaningful services actually used (for example `AWS`, `Amazon S3`), not lightweight hosting product names such as AWS Lightsail. Write `deployed to AWS` rather than `deployed to AWS Lightsail`. Omit version numbers of operating systems, tools, and frameworks (write `Ubuntu`, not `Ubuntu 24.04 LTS`) unless the JD asks for a specific version.

Describe the approach, not its parameters. A recruiter needs to know what problem was handled and the general method, for example `handled AI extraction failures with timeouts, automatic retries, and clear error messages`. Leave exact values (timeout seconds, retry counts, port numbers, file names, record counts in a window) for the interview and keep them in LaTeX comments or review records. Keep numbers that show an outcome or scale, such as `15% higher user engagement` or `34% better alignment`.

Describe internal or little-known product names by what they are, because recruiters do not know them. Write `an education services web platform for a new business line`, not `Travedu`. When the name helps credibility (for example a real business using the system), keep it with a short descriptor, as in `Snackphoria, a snack and vending business`. Keep the original name in a LaTeX comment for traceability. Do not inflate scale or audience when generalizing.

Omitting a detail must not create a false impression. Do not name services, scale, traffic, or architecture that were not used (for example EC2, ECS, Kubernetes, multi-region, or high-traffic claims when the system ran on a single instance). Keep source-level details in LaTeX comments and review records for traceability.

After every completed rewrite or revision, report a local JD match score out of 100 and grouped keyword coverage as a count and percentage. Follow `scoring-rubric.md` for fixed weights, evidence levels, OR/AND logic, denominators, eligibility gates and paired scoring records. Do not present this rubric score as an employer ATS score or a screening probability.

Never guarantee that a resume will pass an ATS or AI screening process.

## 6. Experience Bullet Writing

Use concise, professional English.

Prefer:

Action + Technology + Engineering Contribution + Outcome

When possible, include:
- What was developed.
- Which technology was used.
- What problem it addressed.
- How it was tested or evaluated.
- Measurable outcomes supported by evidence.

Avoid exaggerated language.

Avoid unnecessary repetition between bullets.

Use consistent terminology for the same project or technical concept.

Spell out domain, business, and methodology acronyms at their first occurrence in the experience or project text, using `Full Name (ACRONYM)`, for example `Enterprise Resource Planning (ERP)` and `Test-Driven Development (TDD)`. Use the acronym alone afterwards. This applies to Resume and CV. Widely used technology names (for example SQL, REST APIs, AWS, HTML, CSS, JSON, CI/CD) and Technical Skills list entries may remain abbreviated. If the expansion causes hyphenation, an overfull line, or an extra line, rephrase the bullet instead of forcing it with `\mbox`.

Do not use:
- "not only ... but also"
- Em dashes or en dashes
- Promotional or unsupported claims
- Unnecessary complicated sentence structures

Prefer active verbs such as:
- Developed
- Built
- Implemented
- Integrated
- Automated
- Evaluated
- Tested
- Analyzed
- Collaborated

Use present tense for ongoing responsibilities and past tense for completed work.

Maintain accurate distinctions between internal applications, external tools, separate agents, and research projects.

## 7. LaTeX Template Rules

### Preserve the Existing Template

Use the user's existing `resume.cls` and LaTeX structure.

Do not redesign the entire resume.

Keep existing:
- Page margins.
- Header.
- Font conventions.
- Section formatting.
- Contact information.
- Overall resume structure.

Default to a single-column, ATS-readable layout.

### Technical Skills Formatting

Never insert blank lines between Technical Skills entries.

Correct:

\begin{rSection}{Technical Skills}
\textbf{Programming Languages:} Python, TypeScript, JavaScript, SQL\\
\textbf{Full-Stack Development:} React, Node.js, NestJS, Express\\
\textbf{Databases:} PostgreSQL, MongoDB\\
\textbf{Developer Tools:} Git, Docker, CI/CD, Playwright
\end{rSection}

Do not add empty paragraphs between these lines.

Arrange technical skills according to the JD rather than using a fixed ordering for every application.

### Experience Heading Spacing

Use the following default format:

\textbf{Fintelics} - Agentic Software Developer Intern
\hfill \textbf{[Sept 2026 - Present]}\\
\vspace{-1.6em}
\begin{itemize}
    \item Example experience bullet.
\end{itemize}

Important:
- Default to `\vspace{-1.6em}`.
- Do not replace it with `\vspace{-0.6em}`.
- Apply this rule consistently across experience sections.
- If the actual PDF shows overlapping text, adjust only as necessary.

### Education Formatting

Never automatically append:
- (Expected)
- Expected Graduation
- Expected Completion
- Anticipated

Preserve the dates exactly as confirmed by the user.

Do not silently change September 2027 to December 2027, or vice versa.

If the user has formally accepted a PhD offer, an "Incoming PhD Student" entry may be appropriate.

Do not describe planned or unconfirmed PhD enrollment as an accepted offer.

## 8. One-Page Resume Requirement

For standard software engineering resumes, target exactly one page.

Use the existing template's page dimensions and margins.

Do not reduce the font size aggressively.

Avoid wasting vertical space.

When a bullet wraps onto two lines, try to avoid an extremely short second line.

However, never add meaningless text solely to fill horizontal space.

Prefer informative details about:
- System functionality.
- Backend integration.
- Database operations.
- Testing coverage.
- Engineering automation.
- Quantitative results.

If there is available space near the bottom of the page:

1. Identify missing JD-relevant evidence.
2. Add an informative bullet when supported.
3. Prefer quantified engineering or research achievements.
4. Otherwise expand an existing bullet with useful detail.
5. Do not add filler text merely to occupy space.

If the resume overflows to a second page:

1. Remove redundant wording.
2. Shorten oversized Technical Skills entries.
3. Combine overlapping experience bullets.
4. Remove lower-relevance details.
5. Adjust spacing conservatively if necessary.
6. Preserve the most important achievements.

Prefer targeted edits over deleting entire jobs or projects.

## 9. PDF Validation

When tools and the original LaTeX template are available:

1. Compile the modified LaTeX.
2. Check that compilation succeeds.
3. Confirm the PDF contains exactly one page when required.
4. Visually inspect the rendered PDF.
5. Extract PDF text and verify reading order.
6. Verify names, dates, headings, and skills.
7. Inspect line wrapping and word hyphenation.
8. Check that no bullet spills onto another page.
9. Check for overlapping text or unusual whitespace.

Pay particular attention to technical keywords such as:
- PostgreSQL
- JavaScript
- TypeScript
- MongoDB
- Software Engineering

Avoid breaking these terms across lines when practical.

If the original resume.cls is unavailable, explicitly state that the original template could not be validated.

Never claim to have compiled or verified a PDF unless the validation actually occurred.

## 10. Application Materials Check

EVERY time the user provides a JD, check whether the application requires anything beyond a resume.

Specifically check:

- Cover Letter.
- Academic Transcript.
- Research CV.
- Portfolio.
- GitHub profile.
- Reference letters.
- Writing samples.
- Other required attachments.
- Online assessments or coding tests.

Classify each item as:

- Required.
- Optional.
- Not mentioned.
- Unable to verify.

Check the official application page when accessible.

Do not treat "not mentioned" as proof that a document will never be required.

If the application page contains additional mandatory fields, those requirements take precedence.

Also flag relevant restrictions involving:
- Work authorization.
- Graduation date.
- Academic enrollment.
- Internship availability.
- Location and hybrid attendance.
- Export control or other eligibility constraints.

## 11. Output Requirements

Respond in Chinese for explanations and professional English for resume/CV content.
Save complete LaTeX in resumes/latex/ and a matching compiled PDF in resumes/pdfs/.
Always also display the entire final LaTeX source in chat for Overleaf.
Include concise match analysis, gaps, important edits, additional application materials,
and unresolved eligibility/verification issues. Always include overall JD match X/100, category subtotals, keyword groups M/N (percentage), and the main deductions under `scoring-rubric.md`. File links never replace the full code.
Feedback-only requests need no files or full rewrite. Revisions preserve correct content.
Use the workspace workflow in SKILL.md for template selection, filenames, dependency
copies, provenance, validation records, and immutable template handling.

## 12. Final Quality Checklist

Before submitting a tailored resume, verify:

- Does the resume reflect the JD's main requirements?
- Were both complete current templates read for this new application?
- In a Resume, do research assistant entries show research direction and outcomes only, without ongoing experiment setup details or supervisor names?
- Are domain and methodology acronyms (for example ERP, TDD) spelled out as `Full Name (ACRONYM)` at their first occurrence in experience or project text?
- Are cloud services named at the provider level (AWS, Amazon S3) without lightweight product names such as Lightsail, without unneeded version numbers (for example Ubuntu 24.04 LTS), and without implying services or scale that were not used?
- Do bullets describe the general approach rather than implementation parameters (exact timeouts, retry counts, ports), while keeping outcome numbers?
- Are little-known product names (for example Travedu) replaced with a plain description a recruiter understands?
- Are completed results stated confidently, without defensive status qualifiers such as "(unpublished experiment)", while the status stays in comments and records?
- Can every claim be traced to a template section or an explicit current-application authorization, without automatic historical carryover?
- Are important keywords supported by actual experience?
- Are the most relevant skills placed prominently?
- Are job titles and dates accurate?
- Are quantitative results grounded in evidence?
- Is the user's original LaTeX template preserved?
- Does Technical Skills contain no extra blank lines?
- Does each experience heading use the preferred spacing?
- Are unwanted "Expected" date labels absent?
- Is the resume one page when required?
- Are bullets informative without unnecessary repetition?
- Are long or orphaned lines minimized?
- Was the actual PDF checked if possible?
- Were additional application materials explicitly reviewed?
- Were important eligibility issues identified?
- Were the final PDF match score out of 100, grouped keyword numerator/denominator/percentage, deductions, and eligibility gates reported in chat?
- Were OR alternatives counted as one group and complete AND branches checked, without changing the denominator to improve the score?
- Is the complete LaTeX code directly copyable?

Prioritize accuracy, job relevance, readability, and consistency over maximizing the number of keywords.
