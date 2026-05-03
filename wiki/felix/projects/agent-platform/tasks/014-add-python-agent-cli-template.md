---
title: Add Python agent CLI template
status: done
priority: high
tags: [felix, scaffold, template, agentic-context]
---

# Add Python Agent CLI Template

## Goal

Felix should generate the agentic CLI pattern instead of only describing it.

## Result

Public Felix now includes `templates/python-agent-cli/` with working template code for:

- `agentic-context`
- `agentic-context-source`
- `agent`

The `agent` command frames work as `have / want / don't want`, includes evidence and judgment sections, and reminds the LLM that tool outputs are evidence to reconcile, not verdicts to parrot.
