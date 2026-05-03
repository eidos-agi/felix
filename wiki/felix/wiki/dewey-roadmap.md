---
date: 2026-05-03
title: Dewey Roadmap
tags: [felix, dewey, librarian, context, roadmap]
type: concept
status: active
---

# Dewey Roadmap

Dewey is the planned AI librarian for local context.

The job is to stop expensive agents from rereading huge files and old context when they only need precise, source-backed slices.

The name is Dewey because the agent is about library science: classification, shelves, indexes, retrieval, and knowing where knowledge lives.

## Core Requirements

- index local codebases, docs, wikis, transcripts, and reusable project context
- return small context packets with source paths and line/page references
- support Code Context Engine as an initial backend candidate
- work locally by default, with no cloud account required
- measure input-token savings where possible
- detect stale indexes and prompt refresh
- expose simple CLI commands around the work, not storage internals
- integrate with Felix audits and the configured router/orchestrator

## Boundary

Dewey is not a general assistant. Dewey finds, indexes, classifies, and serves context.

Felix builds and maintains Dewey. The configured router sends local-context retrieval work to Dewey. A review agent can challenge whether Dewey's retrieved context is enough proof.

## Initial CLI Shape

```bash
dewey init /path/to/repo
dewey index /path/to/repo
dewey ask "payment flow"
dewey packet "where is Mercury bill-pay logic?"
dewey stale
dewey stats
```

## Counter-Arguments and Gaps

Indexing can create false confidence. Dewey must make provenance obvious, surface staleness, and avoid pretending an 800-token context packet proves the whole system when the query needs deeper inspection.
