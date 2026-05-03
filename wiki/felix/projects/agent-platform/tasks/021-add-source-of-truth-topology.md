---
title: Add source-of-truth topology
status: done
priority: 85
tags: [felix, topology, wiki, run-mode, source-of-truth]
---

# Add Source-Of-Truth Topology

Felix should not assume that a dedicated agent repo implies a dedicated wiki, local task list, or installed CLI.

## Done Evidence

`felix interview` now asks where durable knowledge, task execution, live state, and learned facts belong.

`felix interview` and `scaffold-plan` now ask for run mode: source checkout, editable install, packaged install, or project-local invocation.

Docs now explain that domain agents may keep code and live operational state in the agent repo while durable concepts live in a central wiki or parent project. The Sage example records this split explicitly.

