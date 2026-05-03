---
title: Agent Standards
tags: [felix, standards, agents]
---

# Agent Standards

Every agent Felix creates or maintains should have:

- public or private GitHub repo, chosen explicitly
- setup-first discipline: agent setup is the highest-leverage decision in the stack
- runnable CLI with an explicit run mode: source checkout, editable install, packaged install, or project-local invocation
- explicit knowledge home: repo-native wiki/docs, central wiki section, or parent-project docs
- explicit task home: repo-native task list, central project/task system, or parent-project task list
- explicit live-state owner for catalogs, probes, learned facts, and operational status
- decision records for topology, repo, knowledge, tasks, live state, run mode, coupling, drift, reversibility, and proof
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
- agent topology covering whether the agent is a free agent, specialist, embedded tool, org-chart role, router, auditor, librarian, communicator, or operator
- relationship placement when needed: requester, owner, peers, downstream consumers, and escalation path
- dedicated repo when the agent owns durable memory, tasks, docs, runnable CLI surface, or self-improvement; embedded project tool only when the role is narrow and subordinate
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

- the setup theory: ontology, autonomy boundary, coupling, memory substrate, source-of-truth topology, run mode, and proof loop before files
- the human role this agent compiles
- what the agent owns and what it must not own
- which existing agents may already cover the responsibility
- which agent topology applies
- where the agent sits in the agent org chart when that topology applies
- whether the role deserves its own repo or should remain a narrow embedded tool
- where code, durable knowledge, task execution, live state, and learned facts should live
- whether the CLI should run from source, editable install, packaged install, or parent-project invocation
- what options the agent considered, what it recommends, what the human chose, and what coupling/drift/reversibility risks follow
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

The scaffold's default wiki and task files are defaults, not doctrine. If the interview chooses a central wiki or parent-project task home, the generated repo should link that canonical home and remove or clearly subordinate any local duplicate.

Every major scaffold choice should be captured as a decision record:

- decision: topology, repo home, knowledge home, task home, live-state owner, run mode, or routing
- options considered
- agent recommendation and reasoning
- human choice or override
- coupling, drift, reversibility, migration, and ownership risks
- proof to revisit after real use

## Agents Wakeup

Every Felix-built repo should include `AGENTS.md` at the root. It should tell a fresh LLM:

- what this agent is
- what to read first
- where wiki memory, task state, live state, and learned facts live
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
