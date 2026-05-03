# Felix For Everyone

Felix is public infrastructure for people building agent ecosystems.

The Eidos AGI stack is the reference implementation, not the only way to use Felix.

## Portable Concepts

Felix should speak in concepts that travel:

- repository
- CLI
- wiki or docs
- task list
- milestone
- test suite
- install path
- router or orchestrator
- release health
- identity image prompt

## Default Adapters

Felix's defaults are Eidos-flavored because they are real and dogfooded:

- Scridos: repo-native wiki, projects, milestones, and tasks
- FOSS Forge: open-source health files and release readiness
- Reeves: router/orchestrator example

Those should become adapters. A team should be able to keep Felix's standards while using GitHub Issues, Linear, Obsidian, MkDocs, Notion exports, a custom orchestrator, or another release standard.

## Product Rule

When writing docs, commands, tests, or scaffold plans, prefer the generic concept first and name the Eidos implementation second.

Example:

```text
Add a repo-native wiki/docs space. Default adapter: Scridos.
```

Not:

```text
Add Scridos.
```

## Private Maintainer Instances

Felix should support a pattern where public Felix creates a private maintainer instance for a user, team, or product.

Public Felix remains the reusable open-source product. The private instance has an explicit scope and decides which private learnings should be upstreamed.

The private instance may maintain a public product, a private agent ecosystem, or one family of internal agents. Depending on scope, it may contain:

- private routing context
- private agent strategy
- local repo stewardship
- owner-specific maintenance tasks
- upstream candidate notes

The public repo should only receive generalized improvements.
