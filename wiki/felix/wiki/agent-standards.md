---
title: Agent Standards
tags: [felix, standards, agents]
---

# Agent Standards

Every agent Felix creates or maintains should have:

- public or private GitHub repo, chosen explicitly
- installable CLI with a short command name
- repo-native wiki or documentation space checked into the repo
- repo-native project with milestones and task list
- north-stars page
- self-improvement loop page
- tests for core local behavior
- README with role, boundaries, commands, and safety gates
- original agent identity image or image prompt that avoids copyright imitation
- open-source health files when the agent may become reusable public software
- router or orchestrator entry
- agentic intelligence context injection that fetches the latest configured gist before the LLM thinks
- agent command framing around `have`, `want`, and `don't want`
- tool output reconciliation that treats tools as evidence, not verdicts

The CLI should be about the work, not about storage internals.

## Agentic Intelligence Context

Every CLI Felix builds should expose an `agentic-context` command or equivalent startup hook. That surface should fetch the latest unpinned Agentic Intelligence gist before the LLM thinks, because memory/context should be substrate rather than a tool the agent might forget to call.

Agent-facing commands should also apply the gist's orientation model:

- `have`: current state, context, resources, and evidence
- `want`: target state or success condition
- `don't want`: failure modes, boundaries, and technically-correct-but-wrong outcomes

Tool outputs should be presented as evidence for the LLM to reconcile, not verdicts the CLI expects the LLM to parrot.

Felix's reusable Python template lives at:

```text
templates/python-agent-cli/
```

Generated CLIs should copy or adapt that template until Felix ships a richer scaffold command.

Source:

```text
https://gist.githubusercontent.com/dshanklin-bv/0ea9eae3845566a255f4fe9e0bf21590/raw/agentic_intelligence.md
```

## Default Adapters

Felix's Eidos defaults are Scridos for wiki/tasks, FOSS Forge for open-source health, and Reeves for routing. Public Felix should keep those as adapters, not assumptions.

## Agent Identity Images

Every new agent should include a prompt for original identity art. Generated images should be visibly about the agent's job, not a near-copy of an existing character or brand.
