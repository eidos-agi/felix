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

The CLI should be about the work, not about storage internals.

## Default Adapters

Felix's Eidos defaults are Scridos for wiki/tasks, FOSS Forge for open-source health, and Reeves for routing. Public Felix should keep those as adapters, not assumptions.

## Agent Identity Images

Every new agent should include a prompt for original identity art. Generated images should be visibly about the agent's job, not a near-copy of an existing character or brand.
