from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
import subprocess
import urllib.error
import urllib.request


REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOT = REPO_ROOT / "wiki" / "felix"
AGENT_TEMPLATE_ROOT = REPO_ROOT / "templates" / "python-agent-cli"
AGENT_WAKEUP_TEMPLATE = REPO_ROOT / "templates" / "AGENTS.md"
AGENTIC_INTELLIGENCE_CONTEXT_URL = (
    "https://gist.githubusercontent.com/dshanklin-bv/"
    "0ea9eae3845566a255f4fe9e0bf21590/raw/agentic_intelligence.md"
)


@dataclass(frozen=True)
class AgentSpec:
    name: str
    role: str
    repo: str
    status: str
    next_action: str


@dataclass(frozen=True)
class SelfCheck:
    name: str
    ok: bool
    detail: str


AGENTS: tuple[AgentSpec, ...] = (
    AgentSpec(
        "reeves",
        "operating-system and routing front door",
        "external/reference",
        "existing",
        "Route specialist requests to dedicated agents instead of absorbing every domain.",
    ),
    AgentSpec(
        "leinad",
        "adversarial judgment companion",
        "external/reference",
        "existing",
        "Keep profile, principles, and transcript-derived improvements fresh.",
    ),
    AgentSpec(
        "scry",
        "scheduled transcript judgment miner",
        "external/reference",
        "existing",
        "Add schedule/resource gates before unattended runs.",
    ),
    AgentSpec(
        "surfari",
        "learning web-surfing consultant",
        "external/reference",
        "existing",
        "Implement safe agent-browser session execution after the study task closes.",
    ),
    AgentSpec(
        "knox",
        "secrets and access agent",
        "registered",
        "registered",
        "Ship private repo with Touch ID unlock, no raw secrets in Git/wiki/logs.",
    ),
    AgentSpec(
        "capcom",
        "mission-control communicator for important outreach",
        "registered",
        "registered",
        "Ship private repo with notification policy, channel routing, acknowledgement tracking.",
    ),
    AgentSpec(
        "dewey",
        "AI librarian for local indexed context retrieval",
        "registered",
        "registered",
        "Ship private repo that indexes local code/docs/context so agents retrieve precise context instead of rereading huge files.",
    ),
    AgentSpec(
        "felix",
        "agent-builder and maintainer",
        "https://github.com/eidos-agi/felix",
        "active",
        "Own standards, roadmap, scaffolds, health checks, and repair playbooks.",
    ),
)


STANDARD_AGENT_REQUIREMENTS = (
    "public or private repository visibility chosen explicitly",
    "installable CLI with a short command name",
    "repo-native wiki or documentation space checked into the repo",
    "repo-native project, milestone, and task list",
    "north-stars page",
    "self-improvement loop page",
    "tests for the core local behavior",
    "README with role, boundaries, commands, and safety gates",
    "AGENTS.md wakeup file that tells a fresh LLM what to read before thinking",
    "original agent identity image or image prompt that avoids copyright imitation and includes the visible agent name",
    "open-source health files when the agent may become reusable public software",
    "router or orchestrator entry",
    "abstract agent interface so Felix works on capabilities, not storage layout",
    "Agentic Intelligence primitives: thinking, tools, memory, coordination, and goal orientation",
    "memory as thinking substrate, not an optional tool call",
    "tools as instruments for world access, not behavior modifiers or authorities",
    "coordination as a meta-layer for aligning wants and don't-wants across agents and humans",
    "hierarchical design across thinking, tools, memory, and coordination layers",
    "North Star goal-orientation for self-improvement",
    "agentic intelligence context injection that fetches the latest configured gist before the LLM thinks",
    "agent command framing that asks for have, want, and don't want before action",
    "tool output reconciliation that treats tools as evidence, not verdicts",
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


def agentic_context_source() -> str:
    return AGENTIC_INTELLIGENCE_CONTEXT_URL


def fetch_agentic_context(timeout_seconds: float = 10.0) -> str:
    try:
        with urllib.request.urlopen(AGENTIC_INTELLIGENCE_CONTEXT_URL, timeout=timeout_seconds) as response:
            return response.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"Could not fetch agentic intelligence context from {AGENTIC_INTELLIGENCE_CONTEXT_URL}: {exc}") from exc


def agent_template_files() -> tuple[Path, ...]:
    return (
        AGENT_WAKEUP_TEMPLATE,
        AGENT_TEMPLATE_ROOT / "agentic_context.py",
        AGENT_TEMPLATE_ROOT / "cli.py",
    )


def render_agent_template() -> str:
    lines = [
        "Felix Python agent CLI template",
        f"template: {AGENT_TEMPLATE_ROOT}",
        "",
        "Copy these files into the generated repo:",
    ]
    for path in agent_template_files():
        lines.append(f"- {path}")
    lines.extend(
        [
            "",
            "The template provides:",
            "- agentic-context: fetches the latest live Agentic Intelligence gist",
            "- agentic-context-source: prints the unpinned raw gist URL",
            "- agent: frames a request as have / want / don't want, evidence, judgment, first action, and done proof",
            "- primitives stance: thinking, tools, memory, coordination, and goal orientation",
            "- memory stance: memory is substrate for thinking, not an optional tool call",
            "- tool-output stance: evidence to reconcile, not verdicts to parrot",
            "- AGENTS.md: wakeup instructions for a fresh LLM entering the repo",
        ]
    )
    return "\n".join(lines)


def roadmap() -> str:
    return "\n".join(
        [
            "Felix roadmap",
            "1. Keep the agent registry canonical and source-backed.",
            "2. Scaffold Knox with biometric unlock and strict secret-handling rules.",
            "3. Scaffold Capcom with interruption policy, channel routing, and acknowledgement tracking.",
            "4. Scaffold Dewey as the AI librarian for local indexed context retrieval and token-cost reduction.",
            "5. Add `felix audit` to verify each agent has CLI, wiki/docs, tasks, tests, install, git remote.",
            "6. Add `felix scaffold agent-name` to create the standard repo skeleton.",
            "6a. For user-specific private maintainer instances, install into the user's personal repo area.",
            "6b. Add an agentic-context command or equivalent startup hook that fetches the latest agentic intelligence gist before the LLM thinks.",
            "6c. Make agent commands ask for have/want/don't-want and reconcile tool outputs as evidence.",
            "6d. Use the Python agent CLI template for generated CLIs until a richer scaffold command exists.",
            "7. Add AGENTS.md wakeup files to scaffolds so fresh LLMs read memory before thinking.",
            "8. Add agent identity image prompts to scaffolds so new agents have original visual identity.",
            "9. Add repair playbooks for broken installs, stale wikis, missing tasks, and unpushed repos.",
            "10. Add an agent adapter layer so checks and repairs compose across repo/wiki/task layouts.",
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


def check_commands() -> tuple[tuple[str, ...], ...]:
    return (
        ("python", "-m", "pytest", "-q"),
        ("ruff", "check", "."),
        ("scridos", "lint", "wiki/felix"),
        ("python", "-m", "felix.cli", "self"),
    )


def run_checks() -> int:
    worst_exit_code = 0
    for command in check_commands():
        print(f"$ {' '.join(command)}", flush=True)
        result = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if result.returncode != 0:
            worst_exit_code = result.returncode
    return worst_exit_code


def self_checks() -> tuple[SelfCheck, ...]:
    checks = [
        SelfCheck("repo_name", REPO_ROOT.name == "felix", str(REPO_ROOT)),
        SelfCheck("agents", (REPO_ROOT / "AGENTS.md").exists(), "AGENTS.md"),
        SelfCheck("claude", (REPO_ROOT / "CLAUDE.md").exists(), "CLAUDE.md"),
        SelfCheck("readme", (REPO_ROOT / "README.md").exists(), "README.md"),
        SelfCheck("license", (REPO_ROOT / "LICENSE").exists(), "LICENSE"),
        SelfCheck("changelog", (REPO_ROOT / "CHANGELOG.md").exists(), "CHANGELOG.md"),
        SelfCheck("contributing", (REPO_ROOT / "CONTRIBUTING.md").exists(), "CONTRIBUTING.md"),
        SelfCheck("security", (REPO_ROOT / "SECURITY.md").exists(), "SECURITY.md"),
        SelfCheck("code_of_conduct", (REPO_ROOT / "CODE_OF_CONDUCT.md").exists(), "CODE_OF_CONDUCT.md"),
        SelfCheck("ci", (REPO_ROOT / ".github" / "workflows" / "ci.yml").exists(), ".github/workflows/ci.yml"),
        SelfCheck("mascot", (REPO_ROOT / "assets" / "felix-mascot.png").exists(), "assets/felix-mascot.png"),
        SelfCheck("wiki", WIKI_ROOT.exists(), str(WIKI_ROOT)),
        SelfCheck("task_list", (WIKI_ROOT / "projects" / "agent-platform" / "tasks").exists(), "Scridos task list"),
    ]
    return tuple(checks)


def render_self_checks() -> str:
    checks = self_checks()
    status = "PASS" if all(check.ok for check in checks) else "FAIL"
    lines = [f"Felix self-audit: {status}", ""]
    for check in checks:
        marker = "ok" if check.ok else "missing"
        lines.append(f"- {check.name}: {marker} ({check.detail})")
    return "\n".join(lines)


def scaffold_plan(name: str) -> str:
    agent_name = name.lower().strip()
    lines = [
        f"Scaffold plan for {agent_name}",
        f"- create a canonical repo for {agent_name}",
        "- choose public or private visibility explicitly",
        "- add AGENTS.md wakeup file at repo root",
        "- add Python CLI package and tests",
        "- add repo-native wiki/docs with north-stars and self-improvement loop",
        "- add repo-native project, milestones, and tasks",
        "- add assets/ with an original agent identity image prompt and optional generated image",
        "- add an `agentic-context` CLI command or startup hook that fetches the latest agentic intelligence gist",
        "- add agent command framing around have, want, and don't want",
        "- make tool outputs evidence to reconcile, not verdicts to parrot",
        f"- copy the Python agent CLI template from {AGENT_TEMPLATE_ROOT}",
        "- install editable CLI and verify `--help`",
        "- teach the chosen router/orchestrator how to route to it",
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
                "- integrate with the configured task/project system as source context",
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
                "- integrate with Felix audits and the configured router/orchestrator without becoming a general assistant",
            ]
        )
    return "\n".join(lines)
