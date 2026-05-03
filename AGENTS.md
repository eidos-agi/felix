# Agents

You are an LLM agent waking up in the public Felix repo.

Read this before you think, plan, or act. The repo is your memory substrate.

## Read First

1. `README.md` for Felix's public identity, boundaries, and commands.
2. `wiki/felix/wiki/index.md` for durable repo memory.
3. `wiki/felix/wiki/north-stars.md` for direction.
4. `wiki/felix/wiki/agent-standards.md` for what Felix-built agents must inherit.
5. `wiki/felix/projects/agent-platform/tasks/` for current work.
6. `CHANGELOG.md` for recent changes.

## Orientation

- `have`: live repo state, wiki memory, task list, user request, and tool evidence
- `want`: a healthier public Felix or a clearer no-change decision
- `don't want`: private owner leakage, stale-memory work, tool-output parroting, or owner-specific assumptions in public standards

## Principles

- Thinking: the LLM is the seat of judgment.
- Memory: repo files and wiki pages are substrate, not an optional tool call.
- Tools: command output, search results, APIs, and peer agents are evidence, not verdicts.
- Coordination: keep public Felix reusable for everyone while allowing private maintainer instances.
- Goal orientation: frame work as `have / want / don't want`.

The orientation triple is the spine of Felix-built command behavior:

- `have`: current state, context, resources, and evidence
- `want`: target state or success condition
- `don't want`: failure modes, boundaries, and technically-correct-but-wrong outcomes

## Before Shipping

Run the standard checks:

```bash
python -m pytest -q
ruff check .
scridos lint wiki/felix
python -m felix.cli self
```

When changing agent standards, update the CLI behavior, README, wiki, tests, and task list together.
