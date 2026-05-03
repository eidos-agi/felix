---
title: Generalize brand-safety audit
status: done
priority: high
tags: [felix, brand-safety, scaffold, tests]
---

# Generalize Brand-Safety Audit

## Goal

Felix should catch protected brand/franchise references as a reusable agent-building invariant, not as a one-off cleanup.

## Result

Felix now exposes `felix brand-safety` with an optional `--root` argument for scanning other agent repos.

`felix check` includes the brand-safety audit, and generated scaffolds include `tests/test_brand_safety.py` so new Felix-built repos inherit the same regression protection.
