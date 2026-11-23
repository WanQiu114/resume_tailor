# Resume Tailor

由 Codex 或 Claude Code 执行的个人简历/CV工作区。使用 `resume-tailoring` skill，根据公司、Job Title 和 JD 定制 LaTeX，保存 PDF，并在聊天中提供完整 LaTeX。

## 使用

直接粘贴从 LinkedIn 或公司 job board 复制的整段招聘内容即可，无需整理成 Company / Job Title / JD 字段。agent 会自动提取公司、职位及要求，忽略按钮、推荐职位等界面杂项；仅在关键信息缺失或存在歧义时询问。

例如在此项目的 Codex 聊天中输入：

```text
使用 $resume-tailoring
请根据下面的招聘内容定制简历：
[直接粘贴 LinkedIn 或公司招聘页面的内容]
```

在此项目的 Claude Code 会话中输入（直接粘贴招聘内容时也可能自动触发）：

```text
/resume-tailoring
请根据下面的招聘内容定制简历：
[直接粘贴 LinkedIn 或公司招聘页面的内容]
```

`template/` 中的三个文件始终保持不变：研究岗位以 `CV_template.tex` 为起点；开发岗位以 `resume_template.tex` 为起点。混合岗位根据 JD 的主要职责判断。两种模板都使用 `resume.cls`。用户明确选择优先。

每个新岗位都会重新完整读取两份原始模板，并复制所选模板后定制。不会沿用上一岗位的简历作为底稿，也不会自动带入只在之前聊天或申请记录中出现、尚未写入模板的经历；这类补充需要你明确授权用于当前申请。同一申请的后续修订可保留该申请已确认的补充。`template/` 不会自动更新。

每次改写后，聊天中还会报告岗位匹配评分（满分 100）和关键词要求组命中数/总数/百分比。固定权重为必需能力 45、岗位职责 30、加分项 15、资格与到岗条件 10；直接匹配计 1，部分匹配计 0.5，缺失或未确认计 0。A or B or C 只算一组，命中一个完整选项即可；AND 条件需全部满足。硬性资格单独标记，关键词覆盖率不等于 ATS 分数或通过概率。分组、证据和扣分保存在申请 review 目录的 `scoring.jsonl` / `scoring.md`，详细规则见 `skills/resume-tailoring/references/scoring-rubric.md`。

输出示例：

```text
resumes/latex/HeYang_Yuan_Resume_Microsoft_Software_Engineer.tex
resumes/latex/dependencies/HeYang_Yuan_Resume_Microsoft_Software_Engineer/resume.cls
resumes/pdfs/HeYang_Yuan_Resume_Microsoft_Software_Engineer.pdf
resumes/reviews/HeYang_Yuan_Resume_Microsoft_Software_Engineer/
```

同名新申请添加编号；明确修订已有申请时更新对应版本，并先将旧源文件和 PDF 备份至其 review 目录。上传 Overleaf 时除聊天中的 `.tex` 外，还需要 `resume.cls` 和相关资源。普通 Resume 目标为一页，CV 可多页。

## 安装到本机 Codex

以下命令使用 CMD 语法，从项目根目录运行：

```cmd
cd /d D:\github_project\resume_tailor
python scripts\install_skill.py
```

安装到 `%CODEX_HOME%\skills\resume-tailoring`，未设置时使用 `%USERPROFILE%\.codex\skills\resume-tailoring`，并写入此工作区路径。若目标已存在则停止，避免覆盖。修改项目中的 skill 后，可运行 `python scripts\install_skill.py --update` 同步此工作区绑定的安装；其他工作区绑定的安装不会被覆盖。也可通过 `--destination` 指定其他技能父目录。项目 `AGENTS.md` 可以直接引导当前工作区，无需重复安装。

在 Codex 使用 `$resume-tailoring`；若当前客户端提供 `@` 技能选择器，也可从其中选择。若列表未更新，重新打开 Codex。此本地安装不等于已部署到普通 ChatGPT 网页聊天。

## 在本项目中使用 Claude Code

仅项目级接入，无需安装：

- `CLAUDE.md` 通过 `@AGENTS.md` 导入项目规则，规则只在 `AGENTS.md` 维护。
- `.claude/skills/resume-tailoring` 是指向 `skills/resume-tailoring` 的目录 junction，与 Codex 共用同一份 skill 源文件。

若 junction 丢失（例如重新 clone 后），在项目根目录用 CMD 重建：

```cmd
cd /d D:\github_project\resume_tailor
mkdir .claude\skills
mklink /J .claude\skills\resume-tailoring skills\resume-tailoring
```

若 `/resume-tailoring` 未出现在命令列表中，开启新的 Claude Code 会话。删除 junction 请用 `rmdir .claude\skills\resume-tailoring`（只删链接，不删源文件），不要对其递归删除。

## 编译环境

```cmd
python -m pip install --target tools\python -r requirements.txt
python scripts\setup_tools.py
```

第二条命令从 Tectonic 官方 GitHub release 下载固定版本 0.17.0 Windows x64 编译器到项目 `tools/`，存在时不覆盖，记录下载地址及 SHA256；若上游提供 digest 则核对。首次编译可能联网下载 TeX 资源，缓存保存在项目 `tools/tectonic/cache/`。个人简历不上传到远程编译服务。已有 LaTeX 引擎也可通过 `build --engine` 指定。

自动验证记录包括编译状态、源码/PDF hash、页数、文字提取、页面 PNG、文字边界和模板完整性。文字底部留白仅为排版参考，不能替代视觉检查，也不是 ATS 得分。每次最终提交前仍须由 agent 检查所有页面和阅读顺序；缺少依赖或编译失败时须明确报告。

## 维护验证

```cmd
python -m unittest discover -s tests -v
python tests\smoke_templates.py
```

Smoke 验证在 `resumes/build/` 的隔离目录编译原始模板，不生成真实申请。实现与实际验证状态见 `docs/changes/`。申请记录默认仅保存在本机；skill 包不包含个人模板和输出文件。
