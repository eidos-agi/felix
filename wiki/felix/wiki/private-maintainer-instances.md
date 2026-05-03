---
date: 2026-05-03
tags: [felix, private-instance, public-private]
type: concept
status: active
---

# Private Maintainer Instances

Public Felix is the reusable pattern for everyone.

A user, team, or product can create a private maintainer instance of Felix.

The private instance must declare its scope. It might maintain a public product, a private agent ecosystem, or one internal agent family.

For a user-specific instance, prefer installing into that user's personal repo area. The private repo may be named `felix` inside that namespace. The namespace, visibility, and declared scope distinguish it from public Felix.

## Public Felix

- generic standards
- portable scaffold patterns
- public docs
- adapter boundaries
- open-source health

## Private Instance

- scope-specific routing
- private repo maintenance tasks
- private strategy and product thinking
- notes about what should be upstreamed
- local stewardship context

## Rule

Generalized improvements go upstream. Owner-specific context stays private.

## Counter-Arguments and Gaps

The private instance should not fork public Felix's standards forever. If a private pattern becomes generally useful, upstream it quickly.
