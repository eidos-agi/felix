# Sage Interview Example

Purpose:

```bash
felix interview sage --purpose "Sage Intacct maintenance CLI"
```

Why this is an agent:

Sage would own a vendor/API maintenance role. A human in this role checks credentials, probes known objects, catalogs working and blocked objects, explains failure families, and gives the data team a one-command way to avoid slow deploy guessing.

Boundary:

- owns Sage Intacct diagnostics and object catalog maintenance
- does not own the warehouse, Dagster deployment, finance policy, or credential vault
- may produce evidence for another agent or human to act on
- deserves a dedicated repo if it owns durable Sage state, tasks, docs, runnable CLI surface, and self-improvement
- should remain embedded only if it is a narrow diagnostic helper subordinate to one project

Agent topology:

Sage is a specialist maintenance agent. It may sit inside a larger data-agent organization, but it is not automatically a manager or router.

Relationships:

- requesters: data engineering agents and humans investigating Sage failures
- peers: warehouse, Dagster, vault, and finance agents
- downstream consumers: data pipelines and maintainers deciding what to enable
- escalation path: human/Sage admin for permissions, credentials, or licensed module questions

Source-of-truth split:

- code home: `agent-sage` repo
- live state: `sage/core.py` catalog and probe results in the agent repo
- durable knowledge: central Greenmark/Cerebro wiki section for Sage
- execution tasks: either the agent repo task list for implementation work or central project tasks for stakeholder-facing work
- run mode: source checkout while the agent is learning and committing catalog changes; packaged install only when a stable snapshot is wanted

Decision record:

- agent recommendation: use a dedicated `agent-sage` repo for code and live catalog state, central wiki for durable Sage concepts, and source-checkout run mode while the agent is learning
- human decision needed: confirm whether Greenmark wants Sage knowledge in the central wiki and whether implementation tasks stay in `agent-sage` or the central project tracker
- coupling risk: duplicated object lists can drift if data pipelines and `agent-sage` both own Sage object status
- drift mitigation: when the catalog changes, update the data pipeline list and central wiki claim in the same work cycle
- reversibility: if `agent-sage` remains too small, it can be folded back into a parent repo; if it grows, central docs keep it discoverable
- proof: a Sage bisection run updates catalog state, docs, and any downstream pipeline list without another agent guessing where truth lives

Expected first verbs:

- `sage doctor`
- `sage check`
- `sage objects list`
- `sage objects show <name>`
- `sage objects probe <name>`
- `sage objects probe-all`

Done proof:

The CLI can prove which Sage objects pass, fail for permissions, or fail because the object name is wrong without requiring deploy cycles.
