---
title: Add agent wakeup template
status: done
priority: high
tags: [felix, agents, memory, template]
---

# Add Agent Wakeup Template

## Goal

Every Felix-built repo should contain a root `AGENT.md` that tells a fresh LLM what to read before thinking.

## Result

Felix now includes `templates/AGENT.md` as a reusable wakeup file.

Scaffold plans and standards now require an `AGENT.md` wakeup file so repo memory becomes substrate before reasoning, not an optional retrieval step.
