# Pre-Scaffold Interview Examples

`felix interview` is the universal first step before creating a new agent. It is not tied to any one domain.

Run an interview when a user says "make an agent/CLI for this":

```bash
felix interview <agent-name> --purpose "<brief responsibility>"
```

The interview should establish:

- what human role is being compiled into an agent
- what the agent may decide
- what the agent must not own
- which existing agent may already own the work
- what `doctor`, `check`, probes, wiki memory, task memory, and safety gates prove
- what first CLI verbs make the work executable

Examples:

- [`sage.md`](sage.md) — vendor/API maintenance agent
- [`knox.md`](knox.md) — secrets and access agent
- [`capcom.md`](capcom.md) — communication and notification agent

