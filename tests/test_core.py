from felix.core import (
    agentic_context_source,
    agent_template_files,
    check_commands,
    doctor,
    find_agent,
    list_agents,
    render_self_checks,
    roadmap,
    scaffold_plan,
    self_checks,
    standards,
)


def test_agent_registry_includes_planned_agents():
    names = {agent.name for agent in list_agents()}

    assert {"felix", "knox", "capcom", "dewey", "reeves", "leinad", "scry", "surfari"} <= names


def test_find_agent_returns_boundary():
    agent = find_agent("knox")

    assert agent.status == "registered"
    assert "secrets" in agent.role


def test_standards_require_wiki_and_tasks():
    text = "\n".join(standards())

    assert "repo-native wiki" in text
    assert "task list" in text
    assert "abstract agent interface" in text
    assert "open-source health files" in text
    assert "original agent identity image" in text
    assert "visible agent name" in text
    assert "agentic intelligence context injection" in text
    assert "have, want, and don't want" in text
    assert "tools as evidence" in text
    assert "thinking, tools, memory, coordination" in text
    assert "memory as thinking substrate" in text
    assert "North Star goal-orientation" in text


def test_roadmap_prioritizes_knox_then_capcom():
    text = roadmap()

    assert "Scaffold Knox" in text
    assert "Scaffold Capcom" in text
    assert "Scaffold Dewey" in text
    assert "agent identity image prompts" in text
    assert "agentic intelligence gist" in text
    assert "have/want/don't-want" in text
    assert "Python agent CLI template" in text


def test_scaffold_plan_specializes_knox_and_capcom():
    assert "Touch ID" in scaffold_plan("knox")
    assert "acknowledgement" in scaffold_plan("capcom")
    assert "Code Context Engine" in scaffold_plan("dewey")
    assert "agentic-context" in scaffold_plan("knox")
    assert "have, want, and don't want" in scaffold_plan("knox")
    assert "evidence to reconcile" in scaffold_plan("knox")
    assert "templates/python-agent-cli" in scaffold_plan("knox")


def test_doctor_reports_wiki():
    assert any(line.startswith("wiki:") for line in doctor())


def test_self_checks_cover_foss_and_mascot():
    names = {check.name for check in self_checks()}

    assert {"license", "changelog", "contributing", "security", "mascot", "task_list"} <= names
    assert "Felix self-audit:" in render_self_checks()
    assert any(check.detail == "assets/felix-mascot.png" for check in self_checks())


def test_check_commands_capture_maintenance_loop():
    commands = {" ".join(command) for command in check_commands()}

    assert "python -m pytest -q" in commands
    assert "ruff check ." in commands
    assert "scridos lint wiki/felix" in commands
    assert "python -m felix.cli self" in commands


def test_agentic_context_source_is_live_gist_url():
    source = agentic_context_source()

    assert "gist.githubusercontent.com/dshanklin-bv/0ea9eae3845566a255f4fe9e0bf21590/raw/agentic_intelligence.md" in source


def test_agent_template_files_exist_and_encode_agent_shape():
    files = agent_template_files()
    text = "\n".join(path.read_text(encoding="utf-8") for path in files)

    assert all(path.exists() for path in files)
    assert "agentic-context" in text
    assert "agentic-context-source" in text
    assert "agent" in text
    assert "Have:" in text
    assert "Want:" in text
    assert "Don't want:" in text
    assert "evidence to reconcile" in text
    assert "memory is part of thinking" in text
