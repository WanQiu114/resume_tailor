# 006-Nficodebench-Venue-Fse

## task_id

nficodebench-venue-fse-006

## goal

Correct the NFICodeBench submission venue in both master templates from ICSE 2027 to FSE 2027.

## authorization

User explicitly requested on 2026-11-04: change the ICSE entry in template to FSE (exception to template immutability, limited to this edit).

## changes

```json
[
  "CV_template.tex: NFICodeBench publication tag [ICSE 2027] -> [FSE 2027]",
  "CV_template.tex: venue line '49th IEEE/ACM International Conference on Software Engineering (ICSE 2027, Research Track)' -> 'ACM International Conference on the Foundations of Software Engineering (ESEC/FSE 2027)'; '(Under Review)' kept",
  "resume_template.tex: commented NFICodeBench venue 'ICSE 2027, Under Review.' -> 'FSE 2027, Under Review.'"
]
```

## affected_files

```json
[
  "template/CV_template.tex",
  "template/resume_template.tex",
  "docs/changes/006-nficodebench-venue-fse.jsonl",
  "docs/changes/006-nficodebench-venue-fse.md"
]
```

## rationale

User-confirmed fact correction; templates are the evidence source for future applications, so the venue must be fixed at the source.

## expected_behavior

Future CVs list NFICodeBench as under review at ESEC/FSE 2027; resume.cls and all other template content unchanged.

## assumptions

```json
[
  "Year assumed FSE 2027 (same cycle as the other FSE 2027 submission); author list, order and '*' markers unchanged"
]
```

## template_hashes_before

```json
{
  "CV_template.tex": "a866baf8da9c92321341ece7d906474dfe5cc12dd3f0fcc59e94f8ed404648d8",
  "resume_template.tex": "c2ff585a66b75e22a784d6c9483dafc2478f1eef35f894987980c456b6ec7da0",
  "resume.cls": "c9e31264abeb306e3e672b0aca01ae3d80a423ca36425bdb453570cc0a09e6bf"
}
```

## template_hashes_after

```json
{
  "CV_template.tex": "5eab92ebfb4e9e468c4ff36504454620addbd7ba9af32f6fc24a7350527beeb1",
  "resume_template.tex": "e169be78619eabbbf97f9d3210ec4bee8fa4893b92259a8e2c1d310b2520a855",
  "resume.cls": "c9e31264abeb306e3e672b0aca01ae3d80a423ca36425bdb453570cc0a09e6bf"
}
```

## unified_diff

```diff
--- before/CV_template.tex
+++ template/CV_template.tex
@@ -285,9 +285,9 @@
     \textit{ACM International Conference on the Foundations of Software Engineering (ESEC/FSE 2027)} (Under Review)
 
 
-\item “NFICodeBench: Benchmarking Coding Agents for Non-Functional Improvements Beyond Functional Correctness”\hfill {[ICSE 2027]}\\
+\item “NFICodeBench: Benchmarking Coding Agents for Non-Functional Improvements Beyond Functional Correctness”\hfill {[FSE 2027]}\\
     Pengyu Xue, \underline{\textbf{He Yang Yuan*}}, Xin Wang, Junkai Chen, Haonan Zhang, Boyuan Chen, Zishuo Ding, Zhenhao Li, Weiyi Shang\\
-    \textit{49th IEEE/ACM International Conference on Software Engineering (ICSE 2027, Research Track)} (Under Review)
+    \textit{ACM International Conference on the Foundations of Software Engineering (ESEC/FSE 2027)} (Under Review)
 
     
     \item “Towards Secure Logging: Characterizing and Benchmarking Logging Code Security Issues with LLMs” \\
--- before/resume_template.tex
+++ template/resume_template.tex
@@ -329,7 +329,7 @@
     %\item ``NFICodeBench: Benchmarking Coding Agents
     %for Non-Functional Improvements Beyond
     %Functional Correctness''
-    %\textit{ICSE 2027, Under Review.}
+    %\textit{FSE 2027, Under Review.}
 
     %\item ``Reinforcement Learning in the Software
     %Development Lifecycle: Methods, Applications,

```

## validation

```json
{
  "master_compilation": "Both templates compiled with tools/tectonic in a temporary directory (exit 0)",
  "CV_template_pdf": "4 pages; contains 'FSE 2027'; no 'ICSE'",
  "resume_template_pdf": "3 pages; NFICodeBench line is commented out",
  "resume_cls_unchanged": true
}
```

## known_issues

```json
[
  "Earlier tailored outputs still list ICSE 2027: resumes/latex/HeYang_Yuan_CV_Chainlink_Labs_Research_Internship.tex (not changed; historical record)",
  "Qualcomm Deep Learning Research CV updated separately in its revision 3"
]
```

## next_steps

```json
[
  "Confirm FSE year if different",
  "Update Chainlink CV only if that application will be resubmitted"
]
```

## updated_at

2026-11-04T18:12:36.096088+00:00
