# FOSS Forge Compliance

Felix follows the local `foss-forge` standard for agentic software.

Source standard:

```bash
~/repos-eidos-agi/foss-forge
```

## Human Layer

- `LICENSE`: MIT license
- `README.md`: role, commands, boundaries, self-doc links
- `CHANGELOG.md`: Keep a Changelog format
- `CONTRIBUTING.md`: contribution guide with agentic software notes
- `CODE_OF_CONDUCT.md`: Contributor Covenant
- `SECURITY.md`: coordinated disclosure policy

## Agent Layer

- CLI commands describe the work they do.
- Public functions are typed.
- Boundaries are documented so agents do not route secrets, outreach, web surfing, or context retrieval back into Felix.
- Agent standards require wiki, task list, tests, install path, and Reeves route.

## Engineering Layer

- `pyproject.toml` has package metadata.
- Tests cover the registry, roadmap, standards, and scaffold plans.
- CI runs lint and tests.
- Direct runtime dependencies are zero.

## Current Grade

Public alpha. The repo is online at `https://github.com/eidos-agi/felix`, but a packaged release would still require an explicit release decision, issue templates, and a final security review.
