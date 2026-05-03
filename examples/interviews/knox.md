# Knox Interview Example

Purpose:

```bash
felix interview knox --purpose "secrets and access"
```

Why this is an agent:

Knox would own secrets and access. A human in this role knows where secrets live, how to unlock them safely, how to avoid leaking them, and how to help other agents prove they have access without exposing raw values.

Boundary:

- owns secret lookup, unlock policy, access documentation, and secret-safety checks
- does not own the business workflow that consumes a secret
- does not print raw secrets into logs, prompts, wiki pages, or Git
- should overlap-check with any existing vault, OS keychain, or router agent

Expected first verbs:

- `knox doctor`
- `knox check`
- `knox unlock`
- `knox list`
- `knox get <name>`
- `knox audit`

Done proof:

The CLI can unlock through the user's approved local mechanism, return secrets only through safe channels, and prove no generated docs/tests leak raw secret values.

