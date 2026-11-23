# Change: Add Linux (Ubuntu) development and deployment environment to both templates

## Goal

The user runs research code, experiments, and tests on Ubuntu 24.04 LTS virtual machines on Google Cloud, and deploys the Fintelics ERP to an Ubuntu server on AWS Lightsail over SSH. On 2026-11-19 the user explicitly authorized writing these facts into both templates so every agent can use them.

## Changes

- `template/resume_template.tex`: Development Environment skills line now reads `Linux (Ubuntu), Windows, Bash, SSH`; new Fintelics bullet on Ubuntu/Lightsail/SSH/Bash deployment; new York University RA bullet on Ubuntu 24.04 LTS VMs on Google Cloud.
- `template/CV_template.tex`: the same Fintelics and RA bullets (the CV template has no skills section).

~~~diff
--- template/resume_template.tex (before)
+++ template/resume_template.tex (after)
@@ -67,7 +67,7 @@
 \textbf{Databases \& Data Tools:} PostgreSQL, MongoDB, Pandas, NumPy, JSON\\
 \textbf{Development Tools \& Cloud:} Git, Postman, Docker, AWS, Google Cloud, Vercel, Jest, Playwright\\
 \textbf{Software Engineering Practices:} Object-Oriented Programming (OOP), Data Structures, Dependency Injection, Agile Development, Iterative Development, Unit Testing, Integration Testing, End-to-End Testing, Git Pre-push Hooks, CI/CD\\
-\textbf{Development Environment:} Linux, Windows
+\textbf{Development Environment:} Linux (Ubuntu), Windows, Bash, SSH
 \end{rSection}
 
 
@@ -139,6 +139,12 @@
     use PostgreSQL for data persistence, and deploy
     ERP applications to AWS.
 
+    % Linux deployment added 2026-11-19 by explicit user authorization; source-verified in agentic_ERP
+    % (docs/runbooks/lightsail-*.md, scripts/deploy-lightsail.sh, functional-gate.yml SSH deploy). See docs/changes/014-linux-environment.md.
+    \item Deploy and operate ERP services on an Ubuntu
+    server on AWS Lightsail over SSH with Bash
+    deployment scripts.
+
     \item Work on an ERP system initially developed
     through a waterfall-style process, then deliver
     incremental features through Agile-style
@@ -195,6 +201,10 @@
     mined 5,000 commits into 114 tasks, and benchmarked
     110 variants over 10,000 runs each.
 
+    % Linux environment added 2026-11-19 by explicit user statement; see docs/changes/014-linux-environment.md.
+    \item Run research code, experiments, and tests on
+    Ubuntu 24.04 LTS virtual machines on Google Cloud.
+
     % User-authorized research evaluation and experimental harness experience, 2026-11-13.
     \item Built automated evaluation pipelines with
     functional tests defined before agent runs to
~~~

~~~diff
--- template/CV_template.tex (before)
+++ template/CV_template.tex (after)
@@ -105,6 +105,9 @@
     and separate API and worker services to prepare for
     future database migration and capacity upgrades.
 
+    % Linux deployment added 2026-11-19 by explicit user authorization; source-verified in agentic_ERP. See docs/changes/014-linux-environment.md.
+    \item Deploy and operate ERP services on an Ubuntu server on AWS Lightsail over SSH with Bash deployment scripts.
+
     \item Maintain technical documentation for system
     architecture, API behavior, AI workflows, feature changes,
     validation procedures, and operating runbooks.
@@ -137,6 +140,8 @@
     % User-reported experiment; 34% is a relative alignment improvement, not percentage points.
     % Separate from the paper's agent/context comparisons; raw run logs were not supplied here.
     \item Collected, analyzed, and structured real-world software engineering data from open-source repositories to support empirical studies and benchmark construction.
+    % Linux environment added 2026-11-19 by explicit user statement; see docs/changes/014-linux-environment.md.
+    \item Run research code, experiments, and tests on Ubuntu 24.04 LTS virtual machines on Google Cloud.
     \item Prepared research manuscripts on coding agents, reinforcement learning in the software development lifecycle, and LLM-based logging security analysis.
     % FSE 2026 talk added 2026-11-19 by explicit user authorization; see docs/changes/013-fse-2026-talk.md.
     \item Presented the first-author paper ``Towards Secure Logging: Characterizing and Benchmarking Logging Code Security Issues with LLMs'' at ACM FSE 2026 in Montreal, QC, Canada.
~~~

## Affected Files

- `template/resume_template.tex` (sha256 60ef15956b6a4fde... -> 0366e0d6afb34f10...)
- `template/CV_template.tex` (sha256 ed6913e3b4072a09... -> ece7caf7368de9e9...)

## Rationale

- Fintelics deployment facts are source-verified in `D:/Working File/fintelics/agentic_ERP`: `docs/runbooks/lightsail-production-demo.md` (Ubuntu Lightsail instance), `docs/runbooks/lightsail-cicd.md` (SSH as `ubuntu`), `scripts/deploy-lightsail.sh`, and `.github/workflows/functional-gate.yml` (deploy over verified SSH).
- The Google Cloud Ubuntu 24.04 LTS fact comes from the user's statement in chat on 2026-11-19.
- Wording claims a Linux development and deployment environment only. It does not claim Linux kernel/system programming or system administrator experience.

## Validation

- Both templates compiled with `tools/tectonic/tectonic.exe` in a scratchpad copy (exit 0); resume template 3 pages, CV template 4 pages (full evidence pools).
- PyMuPDF text extraction found "Ubuntu 24.04" and "Lightsail over SSH" in both PDFs and the new skills line in the resume template PDF.
- Scratchpad copies were deleted after validation.

## Known Issues

- Previous application records cite older template hashes (historical).
- The ERP repository runbook `docs/runbooks/lightsail-production-demo.md` still calls the deployment a controlled demo. On 2026-11-19 the user confirmed that the system is now in formal production use at Snackphoria, so that runbook wording is out of date. Resumes may describe the system as in production use on the basis of this user confirmation.

## Next Steps

- Use these bullets when a JD asks for Linux, Unix, shell, cloud VMs, or deployment experience.
