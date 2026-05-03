from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil


REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOT = REPO_ROOT / "wiki" / "felix"


@dataclass(frozen=True)
class AgentSpec:
    name: str
    role: str
    repo: str
    status: str
    next_action: str


AGENTS: tuple[AgentSpec, ...] = (
    AgentSpec(
        "reeves",
        "personal OS and routing front door",
        "/Users/dshanklinbv/repos-personal/reeves-3",
        "existing",
        "Route specialist requests to dedicated agents instead of absorbing every domain.",
    ),
    AgentSpec(
        "leinad",
        "DanielSteers adversarial judgment companion",
        "/Users/dshanklinbv/repos-personal/leinad",
        "existing",
        "Keep profile, principles, and transcript-derived improvements fresh.",
    ),
    AgentSpec(
        "scry",
        "scheduled transcript judgment miner",
        "/Users/dshanklinbv/repos-personal/scry",
        "existing",
        "Add schedule/resource gates before unattended runs.",
    ),
    AgentSpec(
        "surfari",
        "learning web-surfing consultant",
        "/Users/dshanklinbv/repos-personal/surfari",
        "existing",
        "Implement safe agent-browser session execution after the study task closes.",
    ),
    AgentSpec(
        "knox",
        "secrets and access agent",
        "/Users/dshanklinbv/repos-personal/knox",
        "registered",
        "Ship private repo with Touch ID unlock, no raw secrets in Git/wiki/logs.",
    ),
    AgentSpec(
        "capcom",
        "mission-control communicator for important outreach",
        "/Users/dshanklinbv/repos-personal/capcom",
        "registered",
        "Ship private repo with notification policy, channel routing, acknowledgement tracking.",
    ),
    AgentSpec(
        "dewey",
        "AI librarian for local indexed context retrieval",
        "/Users/dshanklinbv/repos-personal/dewey",
        "registered",
        "Ship private repo that indexes local code/docs/context so agents retrieve precise context instead of rereading huge files.",
    ),
    AgentSpec(
        "felix",
        "agent-builder and maintainer",
        "/Users/dshanklinbv/repos-personal/felix",
        "active",
        "Own standards, roadmap, scaffolds, health checks, and repair playbooks.",
    ),
)


STANDARD_AGENT_REQUIREMENTS = (
    "private GitHub repo unless explicitly public",
    "installable CLI with a short command name",
    "Scridos wiki checked into the repo",
    "Scridos project with milestones and task list",
    "north-stars page",
    "self-improvement loop page",
    "tests for the core local behavior",
    "README with role, boundaries, commands, and safety gates",
    "Reeves memory/route entry",
    "abstract agent interface so Felix works on capabilities, not storage layout",
)


def list_agents() -> tuple[AgentSpec, ...]:
    return AGENTS


def find_agent(name: str) -> AgentSpec:
    normalized = name.lower().strip()
    for agent in AGENTS:
        if agent.name == normalized:
            return agent
    raise KeyError(f"Unknown agent: {name}")


def standards() -> tuple[str, ...]:
    return STANDARD_AGENT_REQUIREMENTS


def roadmap() -> str:
    return "\n".join(
        [
            "Felix roadmap",
            "1. Keep the agent registry canonical and source-backed.",
            "2. Scaffold Knox with biometric unlock and strict secret-handling rules.",
            "3. Scaffold Capcom with interruption policy, channel routing, and acknowledgement tracking.",
            "4. Scaffold Dewey as the AI librarian for local indexed context retrieval and token-cost reduction.",
            "5. Add `felix audit` to verify each agent has CLI, wiki, Scridos tasks, tests, install, git remote.",
            "6. Add `felix scaffold agent-name` to create the standard repo skeleton.",
            "7. Add repair playbooks for broken installs, stale wikis, missing tasks, and unpushed repos.",
            "8. Add an agent adapter layer so checks and repairs compose across repo/wiki/task layouts.",
        ]
    )


def doctor() -> list[str]:
    findings: list[str] = []
    for binary in ("git", "gh", "scridos"):
        path = shutil.which(binary)
        status = "ok" if path else "missing"
        findings.append(f"{binary}: {status}{f' ({path})' if path else ''}")
    findings.append(f"wiki: {'ok' if WIKI_ROOT.exists() else 'missing'} ({WIKI_ROOT})")
    return findings


def scaffold_plan(name: str) -> str:
    agent_name = name.lower().strip()
    lines = [
        f"Scaffold plan for {agent_name}",
        f"- create /Users/dshanklinbv/repos-personal/{agent_name}",
        "- initialize private GitHub repo",
        "- add Python CLI package and tests",
        "- add Scridos wiki with north-stars and self-improvement loop",
        "- add Scridos project, milestones, and tasks",
        "- install editable CLI and verify `--help`",
        "- teach Reeves how to route to it",
        "- commit and push",
    ]
    if agent_name == "knox":
        lines.extend(
            [
                "- implement Touch ID backed unlock through macOS security boundary",
                "- store only secret metadata and vault references in wiki/Git",
                "- require explicit confirmation before reveal/copy/use",
            ]
        )
    if agent_name == "capcom":
        lines.extend(
            [
                "- define urgency levels, quiet hours, channels, escalation, and acknowledgement",
                "- integrate with Reeves tasks/projects as source context",
                "- log contact attempts without leaking sensitive content unnecessarily",
            ]
        )
    if agent_name == "dewey":
        lines.extend(
            [
                "- study Code Context Engine as an initial backend candidate",
                "- index local repos, docs, transcripts, and wiki pages without cloud dependency",
                "- expose retrieval commands that return small source-backed context packets",
                "- track input-token savings and stale-index risks",
                "- integrate with Felix audits and Reeves routing without becoming a general assistant",
            ]
        )
    return "\n".join(lines)
