---
date: 2026-05-03
tags: [felix, abstraction, yoneda, agents]
type: concept
status: active
---

# Yoneda Agent Interface

Felix should maintain agents through their observable capabilities, not their storage layout.

The useful idea from Yoneda is not decorative category theory. It is the discipline of representing a thing by how it maps into the rest of the system. For Felix, an agent is known by what can be done with it:

- inspect CLI health
- inspect repo privacy and remote state
- inspect wiki presence and lint status
- inspect project, milestone, and task state
- inspect tests
- install or repair the command
- explain boundaries
- route from Reeves

Felix can then compose checks and repairs once over the abstract agent interface, and lower those operations into each concrete repo shape.

## Why This Matters

Without this layer, Felix will become a bundle of one-off scripts for Reeves, Leinad, Scry, Surfari, Knox, and Capcom.

With this layer, Felix can say:

- every agent must have tasks
- every agent must have a wiki
- every agent must have tests
- every agent must be installed
- every agent must be pushed

Then adapters handle whether those facts live in Scridos files, package metadata, GitHub remotes, shell shims, or future agent formats.

## Rule

The Felix CLI should be about work: audit, scaffold, repair, roadmap, standardize. Storage details belong under adapters.

## Counter-Arguments and Gaps

This abstraction is only useful if it makes audits and repairs simpler. If Felix starts hiding real repo details behind vague adapter language, the abstraction should be cut back until it produces concrete commands, failures, and fixes.
