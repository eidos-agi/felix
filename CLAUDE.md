# CLAUDE.md - Felix

Felix is the Felix agent-builder and maintainer for agent ecosystems.

## Start Here

Claude should read `AGENTS.md` first. That file is the canonical root wakeup and operating instruction for all LLM agents in this repo.

This `CLAUDE.md` only adds Claude-specific routing context and historical notes. If it conflicts with `AGENTS.md`, prefer `AGENTS.md` and update this file to point there cleanly.

## Canonical Location

Felix lives at:

```bash
~/repos-eidos-agi/felix
```

The older personal path is not canonical.

Public repo:

```bash
https://github.com/eidos-agi/felix
```

## What Felix Owns

- agent registry and lifecycle state
- new-agent scaffolding
- agent health audits
- repair playbooks
- standards for CLI, wiki/docs, tasks, tests, install, GitHub, and router/orchestrator integration
- open-source health alignment for reusable agentic software

## Boundaries

Felix builds and maintains agents. It does not absorb their domains:

- Reeves is one operating-system/router example.
- Knox owns secrets/access.
- Capcom owns important outreach.
- Dewey owns local indexed context retrieval.
- Leinad owns adversarial review.
- Scry mines transcript judgment.
- Surfari owns live web surfing/playbooks.

## Development

Run before shipping:

```bash
python -m pytest -q
scridos lint wiki/felix
felix doctor
felix self
felix agents list
```

`felix self` is the dogfood command: Felix checks his own canonical path, FOSS Forge files, mascot, wiki, and task list.

When moving paths or agent ownership, update Felix and any configured router/orchestrator. The router must know where to route; Felix must know what to build and repair.

## FOSS Forge Rules

Felix follows FOSS Forge as its default open-source-health adapter:

- human layer: license, changelog, contributing guide, code of conduct, security policy
- agent layer: clear commands, typed public behavior, actionable errors
- engineering layer: metadata, tests, CI, minimal direct dependencies

Felix is currently private, but should be shaped so it can become public cleanly.
