# Change: Resume RA entries show direction and outcomes only

## Goal

The user reviewed the Stripe Software Engineer, New Grad resume (2026-11-17). They said recruiters do not read ongoing experiment setup details, and do not know the supervisor. A Resume should instead state the research direction and research outcomes for research assistant roles.

## Changes

`skills/resume-tailoring/references/writing-rules.md` (the `.claude/skills/resume-tailoring` path is a junction to the same folder):

```diff
 An academic CV may exceed one page. Do not apply the one-page resume rule when a detailed research CV is explicitly requested.
 
+### Research Assistant Experience in a Resume
+
+This rule applies to **Resume** outputs only. A research **CV** may keep supervisors and experiment detail.
+
+In a Resume, describe each research assistant role by:
+
+- Its research direction or area (...).
+- Its research outcomes: published or under-review papers, released benchmarks or tools, and completed results (...).
+- Engineering work that is relevant to the JD (...) and its completed result.
+
+Do not include:
+
+- Experiment setup or in-progress experiment details for ongoing work, such as pattern counts, mined commit counts, task counts, variant counts, run counts, or configurations. An ongoing study may be named only as a research direction.
+- "Supervised by <name>" or other supervisor names. Recruiters do not use them.
+
+When a completed result is kept, keep the qualifiers that make it accurate (...), but drop setup numbers that do not change its meaning.
+
 ### Internship and Co-op Roles
```

```diff
 - Were both complete current templates read for this new application?
+- In a Resume, do research assistant entries show research direction and outcomes only, without ongoing experiment setup details or supervisor names?
```

## Affected Files

- `skills/resume-tailoring/references/writing-rules.md`
- First application: `resumes/latex/HeYang_Yuan_Resume_Stripe_Software_Engineer,_New_Grad.tex` (revision 01; backup under `resumes/reviews/<stem>/revisions/01-before-ra-direction-outcomes/`)

## Rationale

The user explicitly asked for this rule to be added to the skill. It is a writing rule, not an architecture change. `template/` is not modified: the templates keep the full evidence, and the rule only governs what a Resume selects from them. CVs are unaffected.

## Validation

The Stripe New Grad resume was revised under the new rule, rebuilt, inspected visually and rescored (see that application's `review.*` and `scoring.*`).

## Known Issues

Earlier tailored resumes are not retroactively changed.

## Next Steps

Apply the rule to all new Resume applications and to explicit revisions of older ones.
