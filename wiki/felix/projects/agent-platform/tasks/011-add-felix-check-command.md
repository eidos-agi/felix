---
title: Add Felix maintenance check command
status: done
priority: medium
tags: [felix, cli, maintenance]
---

# Add Felix Maintenance Check Command

## Goal

Give public Felix one command that runs the local maintenance loop expected by its private maintainer instances.

## Result

`felix check` now runs:

- `python -m pytest -q`
- `ruff check .`
- `scridos lint wiki/felix`
- `felix self`

Felix self-audit also checks the generated README mascot at `assets/felix-mascot.png`.
