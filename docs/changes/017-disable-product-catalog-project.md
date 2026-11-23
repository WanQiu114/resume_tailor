# Change: Disable the Product Catalog project in both templates

## Goal

On 2026-11-20 the user said the "Product Catalog Web Application" entry (from `D:/Working File/sinopec`) was a part-time job and is not worth listing on a resume. It should no longer appear by default.

## Changes

- `template/resume_template.tex`, `template/CV_template.tex`: the "Selected Projects" section is commented out, not deleted, with a note explaining why. The source evidence (file and commit) stays in the comment.
- Gradient application, revision 02: the section was removed and the space was used for three relevant bullets (photo import failure handling, Easy Trip debugging, Fortrip REST APIs with Postman).

~~~diff
--- template/resume_template.tex (before)
+++ template/resume_template.tex (after)
@@ -381,14 +381,16 @@
 
 \end{rSection}
 
-% Source: D:/Working File/sinopec; project evidence only, no employment relationship inferred.
-\begin{rSection}{Selected Projects}
-\textbf{Product Catalog Web Application}
-\begin{itemize}
-    \item Used sets to derive unique brand and category options
-    for React product-catalog filters.
-\end{itemize}
-\end{rSection}
+% Disabled 2026-11-20 by user request: this was a part-time job, not a personal project, and is not worth listing.
+% Do not re-enable by default; see docs/changes/017-disable-product-catalog-project.md.
+% Source: D:/Working File/sinopec (src/pages/ProductsPage.tsx, commit 681d4bec).
+%\begin{rSection}{Selected Projects}
+%\textbf{Product Catalog Web Application}
+%\begin{itemize}
+%    \item Used sets to derive unique brand and category options
+%    for React product-catalog filters.
+%\end{itemize}
+%\end{rSection}
 
 % ============================================================
 % PUBLICATIONS
~~~

~~~diff
--- template/CV_template.tex (before)
+++ template/CV_template.tex (after)
@@ -191,14 +191,16 @@
 \end{rSection}
 
 
-% Source: D:/Working File/sinopec; project evidence only, no employment relationship inferred.
-\begin{rSection}{Selected Projects}
-\textbf{Product Catalog Web Application}
-\begin{itemize}
-    \item Used sets to derive unique brand and category options
-    for React product-catalog filters.
-\end{itemize}
-\end{rSection}
+% Disabled 2026-11-20 by user request: this was a part-time job, not a personal project, and is not worth listing.
+% Do not re-enable by default; see docs/changes/017-disable-product-catalog-project.md.
+% Source: D:/Working File/sinopec (src/pages/ProductsPage.tsx, commit 681d4bec).
+%\begin{rSection}{Selected Projects}
+%\textbf{Product Catalog Web Application}
+%\begin{itemize}
+%    \item Used sets to derive unique brand and category options
+%    for React product-catalog filters.
+%\end{itemize}
+%\end{rSection}
 
 \begin{rSection}{RESEARCH INTERESTS}
~~~

## Affected Files

- `template/resume_template.tex` (sha256 d356d99a0809c9a8... -> b807f9d38a876029...)
- `template/CV_template.tex` (sha256 068babc9a186f131... -> 5fc7fc9debfb4d85...)
- `resumes/latex/HeYang_Yuan_Resume_Gradient_Junior_Full_Stack_Developer.tex` and its review records

## Rationale

The entry was a single low-value bullet and was described as a project although it came from a part-time job. Commenting it out keeps the evidence for traceability while keeping it out of default resumes.

## Validation

- Both templates compiled with tectonic in a scratchpad copy (exit 0; 3 and 4 pages); "Product Catalog" no longer appears in extracted text.
- Gradient resume rebuilt before the template change: one page, visually inspected, 36 scoring excerpts re-verified, score 93/100, keywords 14/15.

## Known Issues

- The template comment says "part-time job", but the employer, title, and dates of that job are not recorded. It is not listed as employment anywhere.
- The Gradient application was built before this template change; a later rebuild needs a recorded manifest snapshot refresh.
- Earlier tailored resumes (for example CGI) may still contain this project; they are unchanged.

## Next Steps

- None unless the user wants the part-time job listed as experience with confirmed details.
