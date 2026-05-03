---
title: Add agentic intelligence context standard
status: done
priority: high
tags: [felix, context, standards, agents]
---

# Add Agentic Intelligence Context Standard

## Goal

All CLI tools built by Felix should know how to inject Daniel Shanklin's Agentic Intelligence gist into context and should fetch updates from the live gist URL.

## Result

Felix now exposes `agentic-context` and `agentic-context-source`, adds live gist fetching to the standard requirements, and includes the requirement in scaffold plans.

The standard also requires Felix-built agent commands to frame work as `have / want / don't want` and to treat tool outputs as evidence for the LLM to reconcile, not verdicts to parrot.
