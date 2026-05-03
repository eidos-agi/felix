---
title: Add pre-scaffold agent interview
status: done
priority: high
tags: [felix, scaffold, interview, agent-boundaries]
---

# Add Pre-Scaffold Agent Interview

## Goal

Felix should interview the user before setting up a new agent so the new CLI has a clear role, constraints, proof, and boundary against existing agents.

## Result

Felix now exposes `felix interview <name> --purpose "<brief role>"`.

The interview asks about the human role being compiled, decisions the agent may own, decisions it must not own, existing-agent overlap, `have / want / don't want`, methods, constraints, diagnostic probes, wiki/task memory, safety gates, first CLI verbs, and done proof.

Scaffold plans now tell the user to run the interview before writing files.
