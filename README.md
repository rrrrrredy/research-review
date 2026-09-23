# Research Review

[English](README.md) | [简体中文](README.zh-CN.md)

An independently installable Skill for reviewing reports, articles, analyses and proposals. It returns locatable findings and recommendations, preserves the original work by default, and distinguishes review completion from artifact acceptance.

## Relationship to Research Toolkit

The review methods originate from [Research Toolkit](https://github.com/rrrrrredy/research-toolkit), specifically its [Subagents and Review](references/subagents-and-review-loop.md) and [Quality Gates](references/quality-gates.md) references.

Research Toolkit includes review and acceptance as integral parts of its complete research workflow. Research Review makes those review methods available as a separately installable Skill for assessing existing work. Research Toolkit retains its review specifications, execution tools and acceptance checks in full.

The projects are maintained and released independently. Using this Skill does not require installing Research Toolkit.

See [UPSTREAM.json](UPSTREAM.json) for the exact source revision and file records, and [LICENSE](LICENSE) for licensing and attribution.

## Use

Download the [Skill package](https://github.com/rrrrrredy/research-review/releases/latest) and place its complete `research-review` folder in a Skill directory supported by your agent. Alternatively, clone the repository:

```bash
git clone https://github.com/rrrrrredy/research-review.git /path/to/skills/research-review
```

Replace the path with your tool's actual Skill directory and retain all supporting files. Select `research-review`, or ask the agent to read [the Skill](SKILL.md) and its relevant references for a single task. Using the Skill does not require Python; Python 3.10 or later is only needed for the maintainer's file checks.

> Use research-review to assess this report against the attached brief and evidence. Check facts, reasoning, structure and reader usefulness. Give the location, impact and minimal recommendation for each issue. Preserve the original report and separate review completion from report acceptance.

Supply the artifact, actual requirements and available sources. The agent asks only for missing information that materially changes the assessment.

## What it checks

- Requirements and author intent; evidence and data; adversarial reasoning.
- Structure and depth; reader usefulness; process-language removal and natural expression.
- Appropriate domain criteria, substantive review validity, consequential disputes and sampling of passed work.

Compatible perspectives can share a reviewer. Valid negative reviews are retained. Failed required reviews remain unfinished and are resumed after the cause is resolved. The Skill does not create a mandatory vendor panel or start repeated report revisions.

The host agent provides file access, retrieval and independent contexts. This package contains instructions and methods, not a model service, automatic executor or credentials. If an independent check cannot be performed, it must be disclosed as incomplete. A successful package check does not certify a review or report.

## Method updates

Compare the source files at the recorded revision with a proposed update, decide which changes apply to standalone review, update the references and provenance together, then run `python scripts/check_skill.py`. Upstream changes do not automatically modify this project.

## License

Licensed under the [MIT License](LICENSE). Use, modification and redistribution are permitted, including commercial use, provided the copyright and license notices are retained. The bundled Research Toolkit methods retain their original attribution.
