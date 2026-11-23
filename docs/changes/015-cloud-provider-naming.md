# Change: Name cloud providers at the provider level (no Lightsail in visible text)

## Goal

On 2026-11-19 the user asked that resumes stop mentioning AWS Lightsail, a lightweight product, and name the provider instead (AWS, S3). The user wants unnecessary details omitted so that the technical work is presented at its real engineering level.

## Changes

- `skills/resume-tailoring/references/writing-rules.md`: new subsection "Level of Technical Detail" in section 5 and a matching final-checklist item.
- `template/resume_template.tex`, `template/CV_template.tex`: the Fintelics deployment bullet now says `on AWS` instead of `on AWS Lightsail`. Source traceability remains in LaTeX comments.

~~~diff
--- skills/resume-tailoring/references/writing-rules.md (section 5, after "Do not invent")
+### Level of Technical Detail
+
+Omit low-value implementation details that make the work look smaller without making it more accurate. Name a cloud provider and the meaningful services actually used (for example `AWS`, `Amazon S3`), not lightweight hosting product names such as AWS Lightsail. Write `deployed to AWS` rather than `deployed to AWS Lightsail`.
+
+Omitting a detail must not create a false impression. Do not name services, scale, traffic, or architecture that were not used (for example EC2, ECS, Kubernetes, multi-region, or high-traffic claims when the system ran on a single instance). Keep source-level details in LaTeX comments and review records for traceability.
+~~~

~~~diff
+- Are cloud services named at the provider level (AWS, Amazon S3) without lightweight product names such as Lightsail, and without implying services or scale that were not used?
~~~

~~~diff
--- template/resume_template.tex (before)
+++ template/resume_template.tex (after)
@@ -141,9 +141,10 @@
 
     % Linux deployment added 2026-11-19 by explicit user authorization; source-verified in agentic_ERP
     % (docs/runbooks/lightsail-*.md, scripts/deploy-lightsail.sh, functional-gate.yml SSH deploy). See docs/changes/014-linux-environment.md.
+    % Resume wording names the provider (AWS), not the Lightsail product; see docs/changes/015-cloud-provider-naming.md.
     \item Deploy and operate ERP services on an Ubuntu
-    server on AWS Lightsail over SSH with Bash
-    deployment scripts.
+    server on AWS over SSH with Bash deployment
+    scripts.
 
     \item Work on an ERP system initially developed
     through a waterfall-style process, then deliver
~~~

~~~diff
--- template/CV_template.tex (before)
+++ template/CV_template.tex (after)
@@ -106,7 +106,8 @@
     future database migration and capacity upgrades.
 
     % Linux deployment added 2026-11-19 by explicit user authorization; source-verified in agentic_ERP. See docs/changes/014-linux-environment.md.
-    \item Deploy and operate ERP services on an Ubuntu server on AWS Lightsail over SSH with Bash deployment scripts.
+    % Resume wording names the provider (AWS), not the Lightsail product; see docs/changes/015-cloud-provider-naming.md.
+    \item Deploy and operate ERP services on an Ubuntu server on AWS over SSH with Bash deployment scripts.
 
     \item Maintain technical documentation for system
     architecture, API behavior, AI workflows, feature changes,
~~~

## Affected Files

- `skills/resume-tailoring/references/writing-rules.md`
- `template/resume_template.tex` (sha256 0366e0d6afb34f10... -> 1c1e639ee30171c5...)
- `template/CV_template.tex` (sha256 ece7caf7368de9e9... -> a0c999c657cb9c3e...)

## Rationale

Lightsail is an AWS service, so `AWS` is accurate. The rule allows omission of a product tier but forbids implying services, scale, or architecture that were not used, so the change does not overstate the work.

## Validation

- Both templates compiled with tectonic in a scratchpad copy (exit 0; 3 and 4 pages, the full evidence pools).
- Extracted PDF text contains "Ubuntu server on AWS over SSH" and no visible "Lightsail" in either template.
- Scratchpad copies were deleted after validation.

## Known Issues

- Earlier tailored resumes still show Lightsail in visible text: DoorDash, InstaLILY, Tenstorrent, Viggle. They are unchanged until the user asks for revisions.

## Next Steps

- Apply the rule to all new applications. Revise the earlier resumes listed above only on request.
