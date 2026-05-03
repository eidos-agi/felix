---
title: Add agent topology and repo lifecycle judgment
status: done
priority: 80
tags: [felix, interview, topology, repos, agents]
---

# Add Agent Topology And Repo Lifecycle Judgment

Felix should not assume every new agent belongs in the same shape. Some agents are free agents, some are specialists, some are embedded tools, and some are roles inside a larger agent organization.

## Done Evidence

`felix interview` now asks which topology fits the agent and whether the role is only a narrow embedded project tool or a durable agent that deserves its own repo.

`felix scaffold-plan` now tells maintainers to choose the topology and document relationships when they exist.

Public docs and examples now explain that agents with durable memory, tasks, docs, installability, and self-improvement should generally get their own repo, while embedded tools should stay narrow and subordinate to a parent project.

