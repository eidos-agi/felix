---
id: 006-create-dewey-agent
title: Create Dewey Agent
status: todo
priority: 88
milestone: 002-knox-capcom
---

# Create Dewey Agent

Use Felix standards to create Dewey as the AI librarian for local indexed context retrieval and token-cost reduction.

Done means Dewey has private repo, CLI, Scridos wiki, project, milestones, tasks, tests, install, Reeves route memory, and pushed GitHub remote.

The first study target is Code Context Engine:

```bash
uv tool install code-context-engine
cce init
```

Evaluate whether Dewey should wrap CCE directly, maintain its own index, or use CCE as one backend under a broader context-librarian interface.
