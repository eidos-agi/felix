---
title: Add agents wakeup template
status: done
priority: high
tags: [felix, agents, memory, template]
---

# Add Agents Wakeup Template

## Goal

Every Felix-built repo should contain a root `AGENTS.md` that tells a fresh LLM what to read before thinking.

## Result

Felix now includes `templates/AGENTS.md` as a reusable wakeup file.

Scaffold plans and standards now require an `AGENTS.md` wakeup file so repo memory becomes substrate before reasoning, not an optional retrieval step.
