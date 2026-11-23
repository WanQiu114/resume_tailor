# 007-Nficodebench-Grpo-Experience

## task_id

nficodebench-grpo-experience-007

## goal

Persist the user-confirmed NFICodeBench GRPO fine-tuning experience in both master templates so future applications can use it.

## authorization

User explicitly requested on 2026-11-04: add the NFI deep learning experience (from the Qualcomm application) to the templates.

## source_facts

User statements 2026-11-04 (Qualcomm application): follow-up to NFICodeBench; GRPO RL fine-tuning after SFT of Qwen3-14B and Qwen2.5-Coder-14B; rented cloud GPU servers; reward samples eight candidate answers per task scored with NFICodeBench metrics; user is co-first author and co-wrote reward function and training code; PyTorch with CUDA; experiments ongoing, no results yet

## changes

```json
[
  "CV_template.tex: NFICodeBench project dates 'May 2026 - July 2026' -> 'May 2026 - Present' (work ongoing)",
  "CV_template.tex: added GRPO fine-tuning bullet and co-first-author reward design bullet to the NFICodeBench project",
  "resume_template.tex: added the same two bullets to the York University Research Assistant entry (before the manuscripts bullet)",
  "resume_template.tex: AI & Machine Learning skills add 'LLM Fine-Tuning (SFT, GRPO)'"
]
```

## affected_files

```json
[
  "template/CV_template.tex",
  "template/resume_template.tex",
  "docs/changes/007-nficodebench-grpo-experience.jsonl",
  "docs/changes/007-nficodebench-grpo-experience.md"
]
```

## rationale

Wording reuses the Qualcomm-approved bullets. 'Co-' verbs reflect co-first-author shared work; '(ongoing)' prevents implying results.

## expected_behavior

New applications may select GRPO/SFT evidence from templates without a separate supplement; earlier tailored outputs are unchanged.

## assumptions

```json
[
  "Cloud provider not named (user wrote 'vest ai', likely Vast.ai, unconfirmed)",
  "No metrics or outcomes claimed"
]
```

## template_hashes_before

```json
{
  "CV_template.tex": "5eab92ebfb4e9e468c4ff36504454620addbd7ba9af32f6fc24a7350527beeb1",
  "resume_template.tex": "e169be78619eabbbf97f9d3210ec4bee8fa4893b92259a8e2c1d310b2520a855",
  "resume.cls": "c9e31264abeb306e3e672b0aca01ae3d80a423ca36425bdb453570cc0a09e6bf"
}
```

## template_hashes_after

```json
{
  "CV_template.tex": "5dae13eec0112307a8224c323eca643d3674efdf2cfc7ffb8fca898f8ead8b51",
  "resume_template.tex": "6c990c421f20b8b81537d03bdffe43cea1e41faba59e517bdc4ae0d2e245d0d8",
  "resume.cls": "c9e31264abeb306e3e672b0aca01ae3d80a423ca36425bdb453570cc0a09e6bf"
}
```

## unified_diff

```diff
--- before/CV_template.tex
+++ template/CV_template.tex
@@ -211,13 +211,16 @@
 \end{itemize}
 
 
-\textbf{Coding Agents for Non-Functional Improvements Benchmarking} \hfill {\textbf{May 2026 - July 2026}} \\
+\textbf{Coding Agents for Non-Functional Improvements Benchmarking} \hfill {\textbf{May 2026 - Present}} \\
 %\textit{Collaborative Research}
 \vspace{-1.5em}
 \begin{itemize}
     \item Integrated Test-Driven Development principles into the evaluation pipeline, utilizing test suites to ensure the functional integrity of agent-generated code.
     \item Developed a benchmark suite with executable evaluation rules to assess coding agents on non-functional improvements.
     \item Designed an evaluation framework to measure agentic performance in complex, long-horizon software maintenance tasks.
+    % GRPO fine-tuning added 2026-11-04 by explicit user request; see docs/changes/007-nficodebench-grpo-experience.md. Ongoing work: no results claimed.
+    \item Co-implement Group Relative Policy Optimization (GRPO) fine-tuning of Qwen3-14B and \mbox{Qwen2.5-Coder-14B} after SFT, using PyTorch with CUDA on rented cloud GPUs (ongoing).
+    \item As co-first author, co-designed a reward function that samples eight candidate solutions per task and scores them with NFICodeBench metrics to provide the GRPO learning signal.
 \end{itemize}
 
 
--- before/resume_template.tex
+++ template/resume_template.tex
@@ -61,7 +61,7 @@
 % ============================================================
 
 \begin{rSection}{Technical Skills}
-\textbf{AI \& Machine Learning:} Agentic Coding, OpenAI Codex, Claude Code, LangGraph, Agent Skills, LLMs, RAG, Reinforcement Learning, NLP, AI-Powered Workflows, OpenAI API, Anthropic API, Open-Source Models, Prompt Engineering\\
+\textbf{AI \& Machine Learning:} Agentic Coding, OpenAI Codex, Claude Code, LangGraph, Agent Skills, LLMs, RAG, Reinforcement Learning, LLM Fine-Tuning (SFT, GRPO), NLP, AI-Powered Workflows, OpenAI API, Anthropic API, Open-Source Models, Prompt Engineering\\
 \textbf{Programming Languages:} Python, C, C\#, C++, Java, JavaScript, TypeScript, SQL\\
 \textbf{Web Development:} HTML, CSS, React, Next.js, Node.js, NestJS, Express, Vite, REST APIs\\
 \textbf{Databases \& Data Tools:} PostgreSQL, MongoDB, Pandas, NumPy, JSON\\
@@ -202,6 +202,17 @@
     training in PyTorch, reducing model training
     time by 80\% while achieving over 85\%
     classification accuracy.
+
+    % GRPO fine-tuning added 2026-11-04 by explicit user request; see docs/changes/007-nficodebench-grpo-experience.md. Ongoing work: no results claimed.
+    \item Co-implement Group Relative Policy Optimization
+    (GRPO) fine-tuning of Qwen3-14B and \mbox{Qwen2.5-Coder-14B}
+    after SFT, using PyTorch with CUDA on rented cloud
+    GPUs (ongoing).
+
+    \item As co-first author, co-designed a reward function
+    that samples eight candidate solutions per task and
+    scores them with NFICodeBench metrics to provide
+    the GRPO learning signal.
 
     \item Contributed to four research manuscripts,
     including one first-author paper published at

```

## validation

```json
{
  "master_compilation": "Both templates compiled with tools/tectonic in a temporary directory (exit 0)",
  "CV_template_pdf": "4 pages; GRPO text and 'Qwen2.5-Coder-14B' render intact",
  "resume_template_pdf": "3 pages; GRPO text renders intact",
  "line_endings": "CRLF preserved",
  "resume_cls_unchanged": true
}
```

## known_issues

```json
[
  "Existing application manifests (Amazon, Frontier Dental, Qualcomm, Lyft) hold older template hashes; the build helper will refuse further revisions until each manifest is re-snapshotted with a documented reason"
]
```

## next_steps

```json
[
  "Update templates again when GRPO results or a paper submission exist",
  "Confirm cloud provider name if it should appear"
]
```

## updated_at

2026-11-04T18:35:28.337996+00:00
