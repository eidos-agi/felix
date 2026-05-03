---
title: Prepare v0.1.0 release
status: todo
priority: 80
tags: [felix, release, packaging, pypi]
---

# Prepare v0.1.0 Release

External review noted that public Felix has package metadata but no GitHub release, tag, or PyPI publication.

## Decision

Do not pretend the release exists. Keep source-checkout install instructions in the README for alpha users, then prepare a real `v0.1.0` release when the scaffold install smoke test has landed.

## Done Means

- `007-review-scaffold-install-smoke-test.md` is resolved or intentionally deferred.
- `CHANGELOG.md` has a `v0.1.0` section with public-facing release notes.
- Git tag `v0.1.0` exists.
- GitHub release `v0.1.0` exists.
- PyPI publication is either completed or explicitly deferred with install-from-source instructions still visible.

