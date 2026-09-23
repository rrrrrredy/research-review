# 研究审查

[English](README.md) | [简体中文](README.zh-CN.md)

可以独立安装的审查 Skill，用于报告、文章、分析和方案。交付可定位的问题与改进建议，默认保留原文，分别判断评审是否完成、成果是否合格。

## 与 Research Toolkit 的关系

本项目的审查方法源自 [Research Toolkit（研究工具箱）](https://github.com/rrrrrredy/research-toolkit) 的[子 Agent 与审查](references/subagents-and-review-loop.zh-CN.md)及[质量关卡](references/quality-gates.zh-CN.md)。

Research Toolkit 本身包含完整研究流程，审查与验收始终是其中的组成部分。Research Review 将其中的审查方法整理为可独立安装使用的 Skill，方便单独审查已有成果。Research Toolkit 原有的审查规范、执行工具与验收能力完整保留。

两个项目独立维护、独立发布；使用本 Skill 无需安装 Research Toolkit。

具体来源版本与文件记录见 [UPSTREAM.json](UPSTREAM.json)，授权与署名见 [LICENSE](LICENSE)。

## 使用

下载 [Skill 安装包](https://github.com/rrrrrredy/research-review/releases/latest)，将其中的 `research-review` 文件夹完整放入 Agent 支持的 Skill 目录。也可以直接克隆：

```bash
git clone https://github.com/rrrrrredy/research-review.git /path/to/skills/research-review
```

将路径替换为所用工具的实际 Skill 目录，保留全部配套文件。随后选择 `research-review`；只使用一次时，也可以让 Agent 读取[中文入口](SKILL.zh-CN.md)与相关参考文件。使用 Skill 本身无需安装 Python；Python 3.10 及以上仅用于维护时的文件校验。

> 请用 research-review 审查这份报告，以随附的任务要求和证据为准，检查事实、推理、结构和读者体验。逐条给出问题位置、影响和最小改进建议。保留原文，分别说明审查是否完成、报告是否可交付。

提供受评成果、实际要求和可用来源。只补问会实质影响判断的缺失信息。

## 审查内容

- 任务与作者意图、事实与数据、对抗性推理。
- 结构与深度、读者可用性、去过程化与自然表达。
- 适用的领域要求、评审有效性、关键争议裁定，以及已通过内容的抽查。

相近视角可以由同一评审者承担。有效负评予以保留；必需评审失败时仍为未完成，排除原因后补齐。不会固定配置某几家模型，也不会自动开启反复修稿。

文件访问、检索和独立上下文由宿主 Agent 提供。本包提供指令与方法，不包含模型服务、自动执行器或凭据。无法完成必需的独立检查时须明确缺项。安装包检查通过不能证明评审或报告质量。

## 方法更新

更新审查方法时，对比来源记录中的版本与候选新版本，确认变化是否适用于独立审查，再一并更新参考文件与来源记录，运行 `python scripts/check_skill.py`。上游更新不会自动改变本项目。

## 开源许可

本项目采用 [MIT 许可证](LICENSE)，允许使用、修改、再分发及商业使用，需保留版权声明与许可声明。随包提供的 Research Toolkit 审查方法保留原始署名。
