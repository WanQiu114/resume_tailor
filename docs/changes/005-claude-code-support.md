# Change: Claude Code support (project level)

**task_id:** `claude-code-support-005`

## Goal

Let Claude Code invoke the existing resume-tailoring skill in this project without changing the approved architecture.

## Authorization

User approved the project-level option only (no global ~/.claude/skills install, install_skill.py unchanged).

## Changes

- Added CLAUDE.md that imports AGENTS.md so Claude Code loads the same project rules.
- Created directory junction .claude/skills/resume-tailoring -> skills/resume-tailoring (single skill source shared with Codex).
- Made SKILL.md agent-neutral and added trigger guidance to its description.
- Updated AGENTS.md first line and README usage/setup for Claude Code.

## Affected Files

- `CLAUDE.md`
- `AGENTS.md`
- `README.md`
- `skills/resume-tailoring/SKILL.md`
- `.claude/skills/resume-tailoring (junction)`

## Code Change

```diff
--- /dev/null
+++ CLAUDE.md
@@ -0,0 +1,5 @@
+# Resume tailoring workspace (Claude Code entry point)
+
+Project rules are maintained in AGENTS.md (shared with Codex). Do not duplicate them here.
+
+@AGENTS.md

--- AGENTS.md
+++ AGENTS.md
@@ -3 +3 @@
-This workspace is HeYang Yuan's personal resume/CV agent, executed by Codex.
+This workspace is HeYang Yuan's personal resume/CV agent, executed by Codex or Claude Code (Claude loads this file through `CLAUDE.md`).

--- skills/resume-tailoring/SKILL.md
+++ skills/resume-tailoring/SKILL.md
@@ -3 +3 @@
-description: Tailor HeYang Yuan's LaTeX resume or research CV to a job description, preserve original templates, and generate matching LaTeX and reviewed PDFs.
+description: Tailor HeYang Yuan's LaTeX resume or research CV to a job description, preserve original templates, and generate matching LaTeX and reviewed PDFs. Use when the user pastes a job posting (LinkedIn or company job board) or asks to tailor, revise, or score a resume/CV for a job.
@@ -8 +8 @@
-Use Codex as the agent. Explain decisions in Chinese; ...
+The agent is Codex or Claude Code; the workflow and rules are identical for both. Explain decisions in Chinese; ...

--- README.md
+++ README.md
@@ -3 +3 @@
-由 Codex 执行的个人简历/CV工作区。...
+由 Codex 或 Claude Code 执行的个人简历/CV工作区。...
@@ +16 @@
+在此项目的 Claude Code 会话中输入（直接粘贴招聘内容时也可能自动触发）：
+/resume-tailoring ...
@@ before "## 编译环境" @@
+## 在本项目中使用 Claude Code
+(CLAUDE.md import, junction explanation, CMD rebuild commands, safe rmdir removal note)

+++ .claude/skills/resume-tailoring  (directory junction -> skills/resume-tailoring, created with mklink /J)
```

## Rationale

Claude Code and Codex share the SKILL.md format, so a junction avoids a drifting copy; an @import keeps AGENTS.md as the only rule source. Helpers, templates, rubric and output layout are untouched.

## Expected Behavior

In a Claude Code session opened in this workspace, /resume-tailoring is available (and may auto-trigger on a pasted job posting); AGENTS.md rules are in context. Codex behavior is unchanged apart from the wording/description update.

## Assumptions

- Claude Code follows NTFS directory junctions when discovering project skills (confirmed by the validation below).

## Validation

- **unit_tests:** python -m unittest discover -s tests: Ran 3 tests, OK
- **junction:** dir /AL .claude\skills shows <JUNCTION> resume-tailoring [D:\github_projectesume_tailor\skillsesume-tailoring]
- **headless_skill_discovery:** claude -p in workspace reported skill=yes
- **headless_rules_loaded:** claude -p quoted the AGENTS.md sentence about template/ being immutable
- **template_files_modified:** False
- **end_to_end_tailoring_run:** not performed

## Known Issues

- Junction is a local filesystem object; a fresh clone or copy needs it recreated (README gives CMD commands). If the project becomes a git repo, the junction should not be committed as a directory copy.
- Recursive deletion of .claude/skills/resume-tailoring could delete the real skill files; use rmdir on the junction only.
- Installed Codex copy in ~/.codex/skills is not synced automatically; run install_skill.py --update if Codex should get the new SKILL.md wording.

## Next Steps

- Run one real tailoring task in Claude Code to confirm end-to-end behavior (prepare, build, PNG inspection, scoring).

_updated_at: 2026-11-04T16:07:55.649173+00:00_
