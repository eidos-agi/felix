# Capcom Interview Example

Purpose:

```bash
felix interview capcom --purpose "important outreach and acknowledgement tracking"
```

Why this is an agent:

Capcom would own communication control. A human in this role decides when something is important enough to interrupt the user, which channel should carry it, what acknowledgement is required, and how escalation should work.

Boundary:

- owns notification policy, channel routing, interruption rules, and acknowledgement tracking
- does not own the underlying domain decision unless explicitly delegated
- does not send messages without the configured confirmation or escalation policy
- should overlap-check with routers, calendar agents, email agents, and personal assistants

Expected first verbs:

- `capcom doctor`
- `capcom check`
- `capcom policy show`
- `capcom notify`
- `capcom ack`
- `capcom escalations list`

Done proof:

The CLI can explain why a message should or should not interrupt the user, route it to the correct channel, and track acknowledgement without becoming the agent that decided the business fact itself.

