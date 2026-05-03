---
title: Public hardening review
status: done
priority: 75
tags: [felix, review, public, hardening]
---

# Public Hardening Review

External review called out that Felix's concept is strong but its public-user hardening needs to catch up.

## Done Evidence

- README now documents source-checkout and editable install during public alpha.
- `doctor()` treats Scridos as an optional Eidos adapter instead of a universal public prerequisite.
- `fetch_agentic_context()` retries once before failing.
- brand-safety scanning tolerates binary-like extensionless files.
- overlap detection ignores more generic terms such as repo, task, wiki, docs, and build.
- A dedicated release task tracks `v0.1.0` tag/GitHub release/PyPI decisions.

