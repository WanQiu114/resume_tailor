# 009-Cv-Ma-End-Date

## task_id

cv-ma-end-date-009

## goal

Resolve the MA end-date conflict between templates (CV Sept 2027 vs Resume Dec 2027).

## authorization

User explicitly requested on 2026-11-04 ('Yes, set Dec 2027'); user had confirmed Dec 2027 for earlier applications.

## changes

```json
[
  "CV_template.tex Education: York MA 'Sept 2025 - Sept 2027' -> 'Sept 2025 - Dec 2027'"
]
```

## affected_files

```json
[
  "template/CV_template.tex",
  "docs/changes/009-cv-ma-end-date.jsonl",
  "docs/changes/009-cv-ma-end-date.md"
]
```

## rationale

Both templates now agree; graduation-date gates (e.g., Qualcomm 'November 2027 or later') no longer depend on template choice.

## expected_behavior

New CVs and Resumes show MA end Dec 2027 without per-application confirmation.

## assumptions

```json
[
  "Only the MA entry was changed, as requested"
]
```

## template_hashes_before

```json
{
  "CV_template.tex": "88d1323a5506563e6b4500d9a608dfb6f26210c54293803ac5e4bff03d4bddf1",
  "resume_template.tex": "0fb1f878e84ef43a1b50a24b22a0fcd11629dbac32200769c4b1faed123a8d51",
  "resume.cls": "c9e31264abeb306e3e672b0aca01ae3d80a423ca36425bdb453570cc0a09e6bf"
}
```

## template_hashes_after

```json
{
  "CV_template.tex": "7204ed0a1e8629329ad6f4b4ec830810aec1d024c4c75325c81e23dacdaa7131",
  "resume_template.tex": "0fb1f878e84ef43a1b50a24b22a0fcd11629dbac32200769c4b1faed123a8d51",
  "resume.cls": "c9e31264abeb306e3e672b0aca01ae3d80a423ca36425bdb453570cc0a09e6bf"
}
```

## unified_diff

```diff
--- before/CV_template.tex
+++ template/CV_template.tex
@@ -47,7 +47,7 @@
 
 
 
-\large{{\bf York University, Toronto, ON, Canada}} \hfill {\textbf{Sept 2025 - Sept 2027}}\\
+\large{{\bf York University, Toronto, ON, Canada}} \hfill {\textbf{Sept 2025 - Dec 2027}}\\
 Faculty of Liberal Arts \& Professional Studies\\
 Master of Arts in Information Systems \& Technology\\  
 Supervised by Zhenhao Li

```

## validation

```json
{
  "master_compilation": "CV_template.tex compiled with tools/tectonic in a temporary directory (exit 0); 4 pages; 'Sept 2025 - Dec 2027' present",
  "line_endings": "CRLF preserved",
  "resume_template_unchanged": true,
  "resume_cls_unchanged": true
}
```

## known_issues

```json
[
  "CV_template.tex line 119: York Research Assistant entry still ends 'Sept 2027' (not changed; may be intended as RA end)",
  "CV_template.tex Academic Plans: PhD 'beginning in Fall 2027' conflicts with MA ending Dec 2027 (not changed)",
  "Existing application manifests hold older template hashes; re-snapshot with a documented reason before revising them"
]
```

## next_steps

```json
[
  "Confirm whether the CV RA end date and Academic Plans should change"
]
```

## updated_at

2026-11-04T19:52:33.899298+00:00
