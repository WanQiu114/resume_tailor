# Change: Spell out acronyms at first use

## Goal

The user asked (2026-11-17, Stripe Software Engineer, New Grad revision 02) for ERP and TDD to be written as full name plus acronym at first occurrence, then confirmed adding this to the skill.

## Changes

`skills/resume-tailoring/references/writing-rules.md` (`.claude/skills/resume-tailoring` is a junction to the same folder):

```diff
 Use consistent terminology for the same project or technical concept.
 
+Spell out domain, business, and methodology acronyms at their first occurrence in the experience or project text, using `Full Name (ACRONYM)`, for example `Enterprise Resource Planning (ERP)` and `Test-Driven Development (TDD)`. Use the acronym alone afterwards. This applies to Resume and CV. Widely used technology names (for example SQL, REST APIs, AWS, HTML, CSS, JSON, CI/CD) and Technical Skills list entries may remain abbreviated. If the expansion causes hyphenation, an overfull line, or an extra line, rephrase the bullet instead of forcing it with `\mbox`.
```

```diff
 - In a Resume, do research assistant entries show research direction and outcomes only, without ongoing experiment setup details or supervisor names?
+- Are domain and methodology acronyms (for example ERP, TDD) spelled out as `Full Name (ACRONYM)` at their first occurrence in experience or project text?
```

## Affected Files

- `skills/resume-tailoring/references/writing-rules.md`
- First application: `resumes/latex/HeYang_Yuan_Resume_Stripe_Software_Engineer,_New_Grad.tex` (revision 02; backup `resumes/reviews/<stem>/revisions/02-before-acronym-expansion/`)

## Rationale

Recruiters may not know domain acronyms such as ERP or TDD. Common technology names are exempt because expanding them adds length without helping readers. The `\mbox` note records what happened in the Stripe revision: forcing an unbreakable full name pushed text into the margin (55pt and 9pt overfull), and rephrasing was the fix.

## Validation

The Stripe New Grad revision 02 was rebuilt: one page, no hyphenated or overfull lines, visually inspected and rescored (86/100, keywords 18/23).

## Known Issues

Whether a given acronym counts as "widely used" needs judgement. Earlier tailored resumes are not changed retroactively.

## Next Steps

Apply the rule to new applications and explicit revisions.
