---
title: Add real scaffold command
status: done
priority: high
tags: [felix, scaffold, cli, templates]
---

# Add Real Scaffold Command

## Goal

Felix should build starter agent repos, not only describe scaffold plans.

## Result

Felix now has a dry-run-first `felix scaffold <name>` command.

By default it lists the files that would be created. With `--write`, it creates a starter repo containing root `AGENTS.md`, README, `pyproject.toml`, Python package and CLI template files, tests, wiki pages, a task skeleton, and an identity image prompt.

The command refuses to overwrite existing files unless `--force` is explicitly passed.
