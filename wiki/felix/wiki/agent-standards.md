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
- AGENTS.md wakeup file that tells a fresh LLM what to read before thinking
- original agent identity image or image prompt that avoids copyright imitation
- brand-safety scan for protected references in product, docs, prompts, and generated scaffolds
- open-source health files when the agent may become reusable public software
- router or orchestrator entry
- pre-scaffold interview covering role boundary, constraints, overlap, and proof
- Agentic Intelligence primitives: thinking, tools, memory, coordination, and goal orientation
- memory as thinking substrate, not an optional tool call
- tools as instruments for world access, not behavior modifiers or authorities
- coordination as a meta-layer for aligning wants and don't-wants across agents and humans
- hierarchical design across thinking, tools, memory, and coordination layers
- North Star goal-orientation for self-improvement
- agentic intelligence context injection that fetches the latest configured gist before the LLM thinks
- agent command framing around `have`, `want`, and `don't want`
- tool output reconciliation that treats tools as evidence, not verdicts

The CLI should be about the work, not about storage internals.

## Pre-Scaffold Interview

Felix should not create a new agent just because the user has a name. Before writing files, run:

```bash
felix interview <agent-name> --purpose "<brief role>"
```

The interview must establish:

- the human role this agent compiles
- what the agent owns and what it must not own
- which existing agents may already cover the responsibility
- the user's methods, constraints, and safety gates
- what `doctor`, `check`, probes, catalogs, or diagnostics should exist
- what proof shows this agent is useful and not duplicative

## Agentic Intelligence Context

Every CLI Felix builds should expose an `agentic-context` command or equivalent startup hook. That surface should fetch the latest unpinned Agentic Intelligence gist before the LLM thinks, because memory/context should be substrate rather than a tool the agent might forget to call.

The primitives Felix expects every generated agent to inherit are:

- Thinking: the LLM is the seat of judgment.
- Tools: instruments for access to the world, not behavior modifiers or authorities.
- Memory: substrate that shapes thinking before inference, not an optional tool call.
- Coordination: a meta-layer for aligning wants and don't-wants across agents and humans.
- Goal orientation: `have / want / don't want`, with self-improvement organized around a North Star.

Agent-facing commands should also apply the gist's orientation model:

- `have`: current state, context, resources, and evidence
- `want`: target state or success condition
- `don't want`: failure modes, boundaries, and technically-correct-but-wrong outcomes

Tool outputs should be presented as evidence for the LLM to reconcile, not verdicts the CLI expects the LLM to parrot.

Felix's reusable Python template lives at:

```text
templates/python-agent-cli/
```

Generated CLIs should copy or adapt that template. Use `felix scaffold <name>` for dry-run-first repo generation from the template set.

The scaffold command writes only when passed `--write`; by default it lists the files it would create.

## Agents Wakeup

Every Felix-built repo should include `AGENTS.md` at the root. It should tell a fresh LLM:

- what this agent is
- what to read first
- where wiki memory and task state live
- how to frame `have / want / don't want`
- what not to do
- what proof makes a run done

This is the file version of memory-as-substrate: read durable repo memory before thinking.

## Brand Safety

Every Felix-built repo should be able to run a protected-reference scan. Public Felix exposes:

```bash
felix brand-safety
felix brand-safety --root path/to/agent-repo
```

Generated scaffolds include brand-safety test coverage, so protected brand/franchise references are caught by normal tests instead of relying on the maintainer to remember the risk.

Source:

```text
https://gist.githubusercontent.com/dshanklin-bv/0ea9eae3845566a255f4fe9e0bf21590/raw/agentic_intelligence.md
```

## Default Adapters

Felix's Eidos defaults are Scridos for wiki/tasks, FOSS Forge for open-source health, and Reeves for routing. Public Felix should keep those as adapters, not assumptions.

## Agent Identity Images

Every new agent should include a prompt for original identity art. Generated images should be visibly about the agent's job, not a near-copy of an existing character or brand.
