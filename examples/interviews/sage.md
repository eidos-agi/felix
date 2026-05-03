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

Expected first verbs:

- `sage doctor`
- `sage check`
- `sage objects list`
- `sage objects show <name>`
- `sage objects probe <name>`
- `sage objects probe-all`

Done proof:

The CLI can prove which Sage objects pass, fail for permissions, or fail because the object name is wrong without requiring deploy cycles.

