# Research Review

[English](README.md) | [简体中文](README.zh-CN.md)

An independently installable Skill for reviewing reports, articles, analyses and proposals. It returns locatable findings and recommendations, preserves the original work by default, and distinguishes review completion from artifact acceptance.

## What you get

Supply the report, actual task and available sources. Receive located, evidenced findings and minimal recommendations. Ordinary review examines the content without adding an auditor, independent adjudicator or formal sampling unless the task requires them. Keep the first valid result rather than rerunning for a favorable outcome.

| Example | Judgment and action |
| --- | --- |
| **Change: product direction presented as version succession.** The draft called two descriptions evidence of continuity between current and earlier functionality. | The dated sources support their respective product directions, not version succession. Keep the capability descriptions and narrow the inference: they do not establish that aily preceded Doubao Work as a product version. This is a [historical Toolkit report revision](https://github.com/rrrrrredy/research-toolkit/blob/5ee675d29200c64edcd615aa2ab9bf5b8ee99e97/docs/case-study/office-agents/README.md), not a new review run by this package. |
| **Keep: a supported comparison with its scope.** Group A cuts entry time from eight to four minutes without changing two-day turnaround; Group B removes a day of duplicate approval and reaches one-day turnaround. | Keep the recommendation to investigate approval waits in this pilot, together with the limitation that two stores per group cannot represent all stores. A small sample does not erase the pilot finding, and editing artificial prose should not erase meaningful uncertainty. This uses constructed material from an existing [diagnostic case](https://github.com/rrrrrredy/research-toolkit/blob/5ee675d29200c64edcd615aa2ab9bf5b8ee99e97/evals/semantic_diagnostics/reader-cases-2026-09-10.json), not a real store evaluation. |

## Relationship to Research Toolkit

The review methods originate from [Research Toolkit](https://github.com/rrrrrredy/research-toolkit), specifically its [Subagents and Review](references/subagents-and-review-loop.md) and [Quality Gates](references/quality-gates.md) references.

Research Toolkit includes review and acceptance as integral parts of its complete research workflow. Research Review makes those review methods available as a separately installable Skill for assessing existing work. Research Toolkit retains its review specifications, execution tools and acceptance checks in full.

The projects are maintained and released independently. Using this Skill does not require installing Research Toolkit; existing Toolkit users do not need a second installation. **Independent installation is not independent review:** the latter needs a context separate from the author, supplied by the host.

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
- Appropriate domain criteria and whether disputed findings are supported by actual passages and sources.

Compatible perspectives can share a reviewer. Valid negative reviews are retained. Failed required reviews remain unfinished and are resumed after the cause is resolved. The Skill does not create a mandatory vendor panel or start repeated report revisions.

The host agent provides file access, retrieval and independent contexts. This package contains instructions and methods, not a model service, automatic executor or credentials. If an expressly required independent check cannot be performed, disclose the missing part. A successful package check does not certify a review or report.

## Method updates

Compare the source files at the recorded revision with a proposed update, decide which changes apply to standalone review, update the references and provenance together, then run `python scripts/check_skill.py`. Upstream changes do not automatically modify this project.

## License

Licensed under the [MIT License](LICENSE). Use, modification and redistribution are permitted, including commercial use, provided the copyright and license notices are retained. The bundled Research Toolkit methods retain their original attribution.
