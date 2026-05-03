from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
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


@dataclass(frozen=True)
class ScaffoldFile:
    path: Path
    content: str


@dataclass(frozen=True)
class ScaffoldResult:
    root: Path
    files: tuple[ScaffoldFile, ...]
    wrote: bool
    skipped: tuple[Path, ...] = ()


@dataclass(frozen=True)
class BrandSafetyFinding:
    path: Path
    reference: str


BRAND_SAFETY_FORBIDDEN_REFERENCES = (
    "fix" + "-it",
    "fix" + " it",
    "fix" + "it",
    "wreck" + "-it",
    "wreck" + " it",
    "ral" + "ph",
    "dis" + "ney",
    "felix " + "jr",
)
BRAND_SAFETY_IGNORED_PARTS = frozenset({".git", ".pytest_cache", ".ruff_cache", ".venv", "felix.egg-info", "__pycache__"})
BRAND_SAFETY_TEXT_SUFFIXES = frozenset({"", ".md", ".py", ".toml", ".txt"})


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
    "brand-safety scan for protected references in product, docs, prompts, and generated scaffolds",
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


def _brand_safety_files(root: Path) -> tuple[Path, ...]:
    return tuple(
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix in BRAND_SAFETY_TEXT_SUFFIXES
        and not any(part in BRAND_SAFETY_IGNORED_PARTS for part in path.parts)
    )


def audit_brand_safety(root: Path | None = None) -> tuple[BrandSafetyFinding, ...]:
    scan_root = (root or REPO_ROOT).resolve()
    findings: list[BrandSafetyFinding] = []
    for path in _brand_safety_files(scan_root):
        text = path.read_text(encoding="utf-8").lower()
        for reference in BRAND_SAFETY_FORBIDDEN_REFERENCES:
            if reference in text:
                findings.append(BrandSafetyFinding(path, reference))
    return tuple(findings)


def render_brand_safety(root: Path | None = None) -> str:
    scan_root = (root or REPO_ROOT).resolve()
    findings = audit_brand_safety(scan_root)
    lines = [f"Felix brand-safety audit: {'PASS' if not findings else 'FAIL'}", f"root: {scan_root}", ""]
    if not findings:
        lines.append("- no protected-reference terms found")
        return "\n".join(lines)
    for finding in findings:
        lines.append(f"- {finding.path}: {finding.reference}")
    return "\n".join(lines)


def agent_template_files() -> tuple[Path, ...]:
    return (
        AGENT_WAKEUP_TEMPLATE,
        AGENT_TEMPLATE_ROOT / "agentic_context.py",
        AGENT_TEMPLATE_ROOT / "cli.py",
    )


def render_agent_template() -> str:
    lines = [
        "Felix Python agent CLI template",
        f"template: {AGENT_TEMPLATE_ROOT.relative_to(REPO_ROOT)}",
        "",
        "Copy these files into the generated repo:",
    ]
    for path in agent_template_files():
        lines.append(f"- {path.relative_to(REPO_ROOT)}")
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


def normalize_agent_name(name: str) -> str:
    normalized = re.sub(r"[^a-z0-9-]+", "-", name.lower().strip()).strip("-")
    if not normalized:
        raise ValueError("agent name must contain at least one letter or number")
    return normalized


def package_name_for(agent_name: str) -> str:
    return normalize_agent_name(agent_name).replace("-", "_")


def _title_for(agent_name: str) -> str:
    return " ".join(part.capitalize() for part in normalize_agent_name(agent_name).split("-"))


def scaffold_files(name: str, root: Path | None = None) -> tuple[ScaffoldFile, ...]:
    agent_name = normalize_agent_name(name)
    package_name = package_name_for(agent_name)
    title = _title_for(agent_name)
    target = (root or Path.cwd() / agent_name).resolve()
    cli_template = (AGENT_TEMPLATE_ROOT / "cli.py").read_text(encoding="utf-8").replace('prog="<agent-cli>"', f'prog="{agent_name}"')
    files = (
        ScaffoldFile(target / "AGENTS.md", AGENT_WAKEUP_TEMPLATE.read_text(encoding="utf-8")),
        ScaffoldFile(
            target / "README.md",
            "\n".join(
                [
                    f"# {title}",
                    "",
                    f"{title} is a Felix-built agent CLI.",
                    "",
                    "## Commands",
                    "",
                    "```bash",
                    f"{agent_name} --help",
                    f"{agent_name} agentic-context-source",
                    f"{agent_name} agent \"describe the work\"",
                    "```",
                    "",
                    "## Agentic Intelligence",
                    "",
                    "This agent follows the Felix standards: thinking, tools, memory, coordination, and goal orientation.",
                    "Memory is substrate, tools are evidence, and work is framed as `have / want / don't want`.",
                    "",
                ]
            ),
        ),
        ScaffoldFile(
            target / "pyproject.toml",
            "\n".join(
                [
                    "[build-system]",
                    'requires = ["setuptools>=69", "wheel"]',
                    'build-backend = "setuptools.build_meta"',
                    "",
                    "[project]",
                    f'name = "{agent_name}"',
                    'version = "0.1.0"',
                    f'description = "{title} agent CLI"',
                    'requires-python = ">=3.12"',
                    "dependencies = []",
                    "",
                    "[project.scripts]",
                    f'{agent_name} = "{package_name}.cli:main"',
                    "",
                    "[tool.setuptools.packages.find]",
                    'include = ["' + package_name + '*"]',
                    "",
                ]
            ),
        ),
        ScaffoldFile(target / package_name / "__init__.py", '"""Felix-built agent package."""\n'),
        ScaffoldFile(target / package_name / "agentic_context.py", (AGENT_TEMPLATE_ROOT / "agentic_context.py").read_text(encoding="utf-8")),
        ScaffoldFile(target / package_name / "cli.py", cli_template),
        ScaffoldFile(
            target / "tests" / "test_cli.py",
            "\n".join(
                [
                    f"from {package_name}.cli import main",
                    "",
                    "",
                    "def test_agentic_context_source(capsys):",
                    '    assert main(["agentic-context-source"]) == 0',
                    "    output = capsys.readouterr().out",
                    '    assert "gist.githubusercontent.com" in output',
                    "",
                    "",
                    "def test_agent_brief(capsys):",
                    '    assert main(["agent", "test work"]) == 0',
                    "    output = capsys.readouterr().out",
                    '    assert "Have:" in output',
                    '    assert "Want:" in output',
                    "    assert \"Don't want:\" in output",
                    "",
                ]
            ),
        ),
        ScaffoldFile(
            target / "tests" / "test_brand_safety.py",
            "\n".join(
                [
                    "from pathlib import Path",
                    "",
                    "",
                    'FORBIDDEN_REFERENCES = ("fix" + "-it", "fix" + " it", "fix" + "it", "wreck" + "-it", "wreck" + " it", "ral" + "ph", "dis" + "ney", "felix " + "jr")',
                    'IGNORED_PARTS = {".git", ".pytest_cache", ".ruff_cache", ".venv", "__pycache__"}',
                    'TEXT_SUFFIXES = {"", ".md", ".py", ".toml", ".txt"}',
                    "",
                    "",
                    "def test_repo_avoids_protected_brand_references():",
                    "    root = Path(__file__).resolve().parents[1]",
                    "    files = [",
                    "        path",
                    '        for path in root.rglob("*")',
                    "        if path.is_file()",
                    "        and path.suffix in TEXT_SUFFIXES",
                    "        and path != Path(__file__)",
                    "        and not any(part in IGNORED_PARTS for part in path.parts)",
                    "    ]",
                    '    text = "\\n".join(path.read_text(encoding="utf-8").lower() for path in files)',
                    "",
                    "    assert not any(reference in text for reference in FORBIDDEN_REFERENCES)",
                    "",
                ]
            ),
        ),
        ScaffoldFile(
            target / "wiki" / agent_name / "wiki" / "index.md",
            f"---\ntitle: {title} Wiki\n---\n\n# {title} Wiki\n\nStart here for durable agent memory.\n",
        ),
        ScaffoldFile(
            target / "wiki" / agent_name / "wiki" / "north-stars.md",
            f"---\ntitle: {title} North Stars\n---\n\n# {title} North Stars\n\n- Keep the agent simple, useful, and oriented around its work.\n",
        ),
        ScaffoldFile(
            target / "wiki" / agent_name / "wiki" / "self-improvement-loop.md",
            f"---\ntitle: {title} Self-Improvement Loop\n---\n\n# {title} Self-Improvement Loop\n\nWhen this agent learns something durable, update the wiki, task list, tests, and CLI behavior as needed.\n",
        ),
        ScaffoldFile(
            target / "wiki" / agent_name / "projects" / "main" / "tasks" / "001-bootstrap.md",
            f"---\ntitle: Bootstrap {title}\nstatus: todo\npriority: high\n---\n\n# Bootstrap {title}\n\nVerify CLI, wiki, tasks, tests, install, and router entry.\n",
        ),
        ScaffoldFile(
            target / "assets" / f"{agent_name}-image-prompt.md",
            f"Create an original mascot or identity image for an open-source CLI named {title}. Include the exact readable wordmark \"{title}\" prominently. Do not resemble existing characters, brands, mascots, logos, or protected designs.\n",
        ),
    )
    return files


def scaffold(name: str, root: Path | None = None, *, write: bool = False, force: bool = False) -> ScaffoldResult:
    files = scaffold_files(name, root=root)
    target = files[0].path.parent
    skipped = tuple(file.path for file in files if file.path.exists() and not force)
    if write:
        if skipped:
            return ScaffoldResult(target, files, wrote=False, skipped=skipped)
        for file in files:
            file.path.parent.mkdir(parents=True, exist_ok=True)
            file.path.write_text(file.content, encoding="utf-8")
    return ScaffoldResult(target, files, wrote=write, skipped=())


def render_scaffold_result(result: ScaffoldResult) -> str:
    mode = "WRITE" if result.wrote else "DRY RUN"
    lines = [f"Felix scaffold: {mode}", f"target: {result.root}", ""]
    if result.skipped:
        lines.append("Skipped existing files; rerun with --force to overwrite:")
        lines.extend(f"- {path}" for path in result.skipped)
        return "\n".join(lines)
    lines.append("Files:")
    lines.extend(f"- {file.path}" for file in result.files)
    if not result.wrote:
        lines.extend(["", "No files written. Rerun with --write to create them."])
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
            "6. Use `felix scaffold agent-name` to create the standard repo skeleton.",
            "6a. For user-specific private maintainer instances, install into the user's personal repo area.",
            "6b. Add an agentic-context command or equivalent startup hook that fetches the latest agentic intelligence gist before the LLM thinks.",
            "6c. Make agent commands ask for have/want/don't-want and reconcile tool outputs as evidence.",
            "6d. Use the Python agent CLI template for generated CLIs.",
            "7. Add AGENTS.md wakeup files to scaffolds so fresh LLMs read memory before thinking.",
            "8. Add agent identity image prompts to scaffolds so new agents have original visual identity.",
            "9. Run brand-safety audits so protected references do not creep into public docs, prompts, or scaffolds.",
            "10. Add repair playbooks for broken installs, stale wikis, missing tasks, and unpushed repos.",
            "11. Add an agent adapter layer so checks and repairs compose across repo/wiki/task layouts.",
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
        ("python", "-m", "felix.cli", "brand-safety"),
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
        "- add brand-safety test coverage for protected references",
        f"- copy the Python agent CLI template from {AGENT_TEMPLATE_ROOT.relative_to(REPO_ROOT)}",
        "- use `felix scaffold <name>` for dry-run-first repo generation",
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
