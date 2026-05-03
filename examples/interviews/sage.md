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
- deserves a dedicated repo if it owns durable Sage memory, tasks, docs, installability, and self-improvement
- should remain embedded only if it is a narrow diagnostic helper subordinate to one project

Agent topology:

Sage is a specialist maintenance agent. It may sit inside a larger data-agent organization, but it is not automatically a manager or router.

Relationships:

- requesters: data engineering agents and humans investigating Sage failures
- peers: warehouse, Dagster, vault, and finance agents
- downstream consumers: data pipelines and maintainers deciding what to enable
- escalation path: human/Sage admin for permissions, credentials, or licensed module questions

Expected first verbs:

- `sage doctor`
- `sage check`
- `sage objects list`
- `sage objects show <name>`
- `sage objects probe <name>`
- `sage objects probe-all`

Done proof:

The CLI can prove which Sage objects pass, fail for permissions, or fail because the object name is wrong without requiring deploy cycles.
