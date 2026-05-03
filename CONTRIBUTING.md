# Contributing to Felix

Thanks for helping improve Felix.

## Quick Start

```bash
git clone https://github.com/eidos-agi/felix.git
cd felix
pip install -e ".[dev]"
```

## Development

Run tests:

```bash
python -m pytest -q
```

Run wiki lint:

```bash
scridos lint wiki/felix
```

Run CLI smoke checks:

```bash
felix doctor
felix agents list
felix standards
```

## Agentic Software Guidance

Felix is agent-facing software. That means:

1. Commands should describe work concepts, not storage internals.
2. Public functions should be typed.
3. Errors should tell the agent what to do next.
4. New agent standards should include documentation, tests, wiki, task list, install path, and route entry.
5. Do not add abstractions unless they produce concrete scaffolds, audits, or repairs.

## Pull Requests

- Keep PRs focused.
- Include tests for new behavior.
- Update the Scridos wiki when changing operating model or agent boundaries.
- Update `CHANGELOG.md`.
