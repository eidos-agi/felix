---
title: Version agentic context source
status: todo
priority: 75
tags: [felix, agentic-context, gist, versioning, deprecation]
---

# Version Agentic Context Source

Felix currently defaults to rolling latest Agentic Intelligence gist context.

## Decision

Keep rolling latest as the public alpha default because Felix is still evolving quickly. Add explicit source-mode reporting now, then design pinned-source support before production agents depend on unattended gist updates.

## Done Means

- `agentic-context-source` can report rolling or pinned mode.
- Generated agents can choose a pinned raw gist URL when stability matters.
- Felix documents when to use rolling versus pinned mode.
- Breaking gist changes have a deprecation policy before unattended production agents rely on the context.

