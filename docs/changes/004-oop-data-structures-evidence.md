# 004-Oop-Data-Structures-Evidence

## task_id

oop-data-structures-004

## goal

Persist and show all four source-verified project groups as OOP/data-structure evidence.

## authorization

Current user asks to include these examples and confirms Fortrip submitted work belongs to employment; earlier instruction establishes template-first updates.

## changes

```json
[
  "Added Fintelics OOP/dependency injection and map/set indexing, grouping and duplicate validation.",
  "Added Fortrip Java/Spring Google OAuth service-interface implementation.",
  "Added Easy Trip Travedu set-based tutor filter options.",
  "Added product-catalog set-based filter example as a project, sourced from sinopec directory; no employment claim.",
  "Added explicit OOP and Data Structures concepts; integrated examples into CGI draft, shortening older bullets to target one page."
]
```

## affected_files

```json
[
  "template/resume_template.tex",
  "template/CV_template.tex",
  "resumes\\latex\\HeYang_Yuan_Resume_CGI_Winter_2027_AI_Developer_Co-op_(8_months).tex",
  "resumes\\reviews\\HeYang_Yuan_Resume_CGI_Winter_2027_AI_Developer_Co-op_(8_months)/manifest.jsonl"
]
```

## rationale

Use concrete, contribution-linked evidence rather than treating language/framework names as proof of OOP/data-structure skills.

## expected_behavior

Future tailoring can select evidence from masters; current CGI demonstrates OOP, maps/sets and interface-based Java development.

## assumptions

```json
[
  "Fortrip Google OAuth work belongs to employment per user; preserve existing June 2025-Sept 2025 display dates without inferring an exact revised start date.",
  "Product catalog is a project only.",
  "Git authorship supports contribution, including AI-assisted development, not exclusive manual authorship."
]
```

## evidence

```json
[
  {
    "claim": "Fintelics OOP and dependency injection",
    "path": "D:/Working File/fintelics/agentic_ERP/backend/src/orders/orders.service.ts:83",
    "commit": "55b8cfa1",
    "author": "HeYang Yuan"
  },
  {
    "claim": "Fintelics map/set application",
    "path": "D:/Working File/fintelics/agentic_ERP/backend/src/estimations/estimations.service.ts:108",
    "commit": "627ea475",
    "author": "HeYang Yuan"
  },
  {
    "claim": "Fortrip Java service-interface design",
    "path": "D:/Working File/fortrip/Fortrip-server/src/main/java/com/travel/system/service/impl/GoogleOAuthServiceImpl.java:18",
    "commit": "643cf215",
    "author": "HeYang Yuan"
  },
  {
    "claim": "Travedu tutor filter sets",
    "path": "D:/Working File/EasyTrip/travedu-web/src/app/tutors/page.tsx:413",
    "commit": "18baa2af",
    "author": "HeYang Yuan"
  },
  {
    "claim": "Product catalog filter sets",
    "path": "D:/Working File/sinopec/src/pages/ProductsPage.tsx:81",
    "commit": "681d4bec",
    "author": "HeYang Yuan"
  }
]
```

## backup

resumes\reviews\HeYang_Yuan_Resume_CGI_Winter_2027_AI_Developer_Co-op_(8_months)\revisions\05

## template_hashes_before

```json
{
  "CV_template.tex": "52770591d00dd1f64e4ecab3143a25d167017e096d82fefcc7bb5901d3a22a40",
  "resume.cls": "c9e31264abeb306e3e672b0aca01ae3d80a423ca36425bdb453570cc0a09e6bf",
  "resume_template.tex": "3c833525de4490644ab8a48e2709eaa8b61f9cd700f6b6e1daaa99b5d9c71d3f"
}
```

## template_hashes_after

```json
{
  "CV_template.tex": "a866baf8da9c92321341ece7d906474dfe5cc12dd3f0fcc59e94f8ed404648d8",
  "resume.cls": "c9e31264abeb306e3e672b0aca01ae3d80a423ca36425bdb453570cc0a09e6bf",
  "resume_template.tex": "c2ff585a66b75e22a784d6c9483dafc2478f1eef35f894987980c456b6ec7da0"
}
```

## unified_diff

```diff
--- before/resume_template.tex
+++ template/resume_template.tex
@@ -66,7 +66,7 @@
 \textbf{Web Development:} HTML, CSS, React, Next.js, Node.js, NestJS, Express, Vite, REST APIs\\
 \textbf{Databases \& Data Tools:} PostgreSQL, MongoDB, Pandas, NumPy, JSON\\
 \textbf{Development Tools \& Cloud:} Git, Postman, Docker, AWS, Google Cloud, Vercel, Jest, Playwright\\
-\textbf{Software Engineering Practices:} Agile Development, Iterative Development, Unit Testing, Integration Testing, End-to-End Testing, Git Pre-push Hooks, CI/CD\\
+\textbf{Software Engineering Practices:} Object-Oriented Programming (OOP), Data Structures, Dependency Injection, Agile Development, Iterative Development, Unit Testing, Integration Testing, End-to-End Testing, Git Pre-push Hooks, CI/CD\\
 \textbf{Development Environment:} Linux, Windows
 \end{rSection}
 
@@ -158,6 +158,14 @@
     architecture, API behavior, AI workflows, feature changes,
     validation procedures, and operating runbooks.
 
+    \item Apply object-oriented design and dependency injection
+    in NestJS services to separate order processing,
+    inventory operations, and PostgreSQL persistence.
+
+    \item Use maps and sets to index products by SKU,
+    aggregate sales by customer, product, and week,
+    and reject duplicate products in ERP orders.
+
 \end{itemize}
 
 \vspace{-0.3em}
@@ -229,6 +237,10 @@
 
     \item Built and maintained CI/CD workflows for
     automated testing and deployment.
+
+    \item Implemented Google OAuth integration in a Java/Spring
+    backend through a service interface, an implementation
+    class, and injected controller dependencies.
 
 \end{itemize}
 
@@ -272,6 +284,9 @@
     a separate business initiative, taking
     ownership of the complete software
     development lifecycle.
+
+    \item Used sets to derive unique subject and language
+    options for Travedu tutor filters.
 
 \end{itemize}
 
@@ -289,6 +304,15 @@
 %    models for sign language processing.
 %\end{itemize}
 
+\end{rSection}
+
+% Source: D:/Working File/sinopec; project evidence only, no employment relationship inferred.
+\begin{rSection}{Selected Projects}
+\textbf{Product Catalog Web Application}
+\begin{itemize}
+    \item Used sets to derive unique brand and category options
+    for React product-catalog filters.
+\end{itemize}
 \end{rSection}
 
 % ============================================================

--- before/CV_template.tex
+++ template/CV_template.tex
@@ -105,6 +105,14 @@
     \item Maintain technical documentation for system
     architecture, API behavior, AI workflows, feature changes,
     validation procedures, and operating runbooks.
+    \item Apply object-oriented design and dependency injection
+    in NestJS services to separate order processing,
+    inventory operations, and PostgreSQL persistence.
+
+    \item Use maps and sets to index products by SKU,
+    aggregate sales by customer, product, and week,
+    and reject duplicate products in ERP orders.
+
 \end{itemize}
 
 
@@ -135,6 +143,10 @@
     \item Built Python pipelines to process JSON data and store structured travel data in PostgreSQL.
     
     \item Built and maintained CI/CD workflows for automated testing and deployment.
+    \item Implemented Google OAuth integration in a Java/Spring
+    backend through a service interface, an implementation
+    class, and injected controller dependencies.
+
 \end{itemize}
 
 \textbf{{Easy Trip. Inc}} - Software Developer Internship \textbf{{\hfill Feb 2025 - June 2025\\}}
@@ -144,6 +156,9 @@
 \item Designed, integrated, and tested RESTful APIs with Postman to validate endpoint functionality, request handling, and response behavior. 
 \item Collaborated with UX and Marketing teams to implement A/B-tested React UI components, contributing to a 15\% increase in user engagement metrics. 
 \item Debugged and resolved frontend and backend issues across the React, Node.js, Express, and MongoDB application stack. 
+    \item Used sets to derive unique subject and language
+    options for Travedu tutor filters.
+
 \end{itemize}
 
 \textbf{{York University. Inc, Toronto, ON, Canada } \hfill Sept 2023 - Dec 2023\\}
@@ -152,6 +167,15 @@
 
 \end{rSection}
 
+
+% Source: D:/Working File/sinopec; project evidence only, no employment relationship inferred.
+\begin{rSection}{Selected Projects}
+\textbf{Product Catalog Web Application}
+\begin{itemize}
+    \item Used sets to derive unique brand and category options
+    for React product-catalog filters.
+\end{itemize}
+\end{rSection}
 
 \begin{rSection}{RESEARCH INTERESTS}
 

```

## validation

```json
{
  "status": "passed",
  "class_unchanged": true,
  "master_template_compilation": [
    {
      "template": "resume_template.tex",
      "compile_status": "passed",
      "log": "resumes\\build\\master-validation-004\\resume_template\\compile.log"
    },
    {
      "template": "CV_template.tex",
      "compile_status": "passed",
      "log": "resumes\\build\\master-validation-004\\CV_template\\compile.log"
    }
  ],
  "final_CGI_compile_status": "passed",
  "final_CGI_visual_status": "passed",
  "page_count": 1,
  "source_sha256": "678961cc5e2e3cccfb08349360119bfb5c339bf93cbfe9453379b077878aa4a0",
  "pdf_sha256": "6a5cd1ab0d8882df056265fb0e8a9951257a232e851dc449957c2910b75aa242",
  "bottom_whitespace_pt": 28.7833251953125,
  "scoring_plan_unchanged": true,
  "overall_score": 73,
  "keyword_hits": 21,
  "keyword_groups": 26,
  "template_snapshot_stable": true
}
```

## known_issues

```json
[
  "No advanced graph/tree/heap implementation, design-pattern expertise, or complexity/speedup claims inferred.",
  "Current CGI Bachelor-in-progress eligibility exception remains unknown."
]
```

## next_steps

```json
[
  "Use updated masters for subsequent tailoring.",
  "Confirm CGI graduate eligibility and exact application form requirements."
]
```

## updated_at

2026-11-03T21:17:31.694065+00:00
