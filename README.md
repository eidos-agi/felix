# Felix

![Original Felix builder mascot](assets/felix-builder.svg)

Fix-it Felix is the agent-builder and maintainer for agent ecosystems.

Felix owns the standards, scaffolds, health checks, repair playbooks, and roadmap for the other agents. Reeves can route to Felix, but Felix should be the one that remembers what a healthy agent repo looks like.

Felix now lives with the Eidos AGI forges at:

```bash
~/repos-eidos-agi/felix
```

Public repo:

```bash
https://github.com/eidos-agi/felix
```

## Commands

```bash
felix doctor
felix self
felix agents list
felix agents show knox
felix standards
felix roadmap
felix scaffold-plan capcom
felix scaffold-plan dewey
```

## Boundaries

Felix builds and maintains agents. It does not become the operating system, the secrets vault, the communicator, the web surfer, or the adversarial reviewer.

Every agent Felix creates should have:

- private GitHub repo unless explicitly public
- installable CLI
- Scridos wiki checked into the repo
- Scridos project with milestones and tasks
- north-stars page
- self-improvement loop
- tests for core local behavior
- clear Reeves routing/memory entry
- an abstract agent interface so Felix can work on capabilities, not storage layout
- FOSS Forge health files when the agent may become reusable open-source software

## Design Principle

Felix should think like a Yoneda-flavored maintenance layer: operate on the agent's observable capabilities, then lower those operations into the concrete repo, wiki, task list, package, or installer shape. The CLI should stay about the work.

## FOSS Forge Alignment

Felix follows the FOSS Forge standard for agentic software:

- human layer: license, changelog, contributing guide, code of conduct, security policy
- agent layer: clear CLI descriptions, actionable errors, typed public behavior
- engineering layer: package metadata, tests, CI, small dependency surface

Felix is public alpha software under the Eidos AGI organization.

The mascot in this repo is original artwork inspired by the idea of a cheerful repair helper. It is not official Disney character art.

## Registered Agents

- Knox: secrets and access.
- Capcom: mission-control communication.
- Dewey: AI librarian for local indexed context retrieval and token-cost reduction.

## Self-Documentation

Felix documents himself in:

- [CLAUDE.md](CLAUDE.md): operating instructions for agents working in this repo
- [docs/felix-self.md](docs/felix-self.md): identity, boundaries, and lifecycle
- [docs/foss-forge-compliance.md](docs/foss-forge-compliance.md): FOSS Forge compliance notes
- [wiki/felix/wiki/index.md](wiki/felix/wiki/index.md): Scridos wiki entrypoint

Felix dogfoods his own standards with:

```bash
felix self
```
