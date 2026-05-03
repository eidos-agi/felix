---
title: Add agent design decision records
status: done
priority: 90
tags: [felix, decisions, coupling, topology, source-of-truth]
---

# Add Agent Design Decision Records

Felix should treat topology, repo home, knowledge home, task home, live-state owner, run mode, and routing as design decisions.

## Done Evidence

`felix interview` now asks what options the agent considered, what the agent recommends, what the human chooses or overrides, what coupling/drift/reversibility/migration/ownership risks follow, and what proof would show the decision was good after real use.

`felix scaffold-plan` now requires a decision record for major scaffold choices.

The Sage example now includes a decision record for `agent-sage`.

