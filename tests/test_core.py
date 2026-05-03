from felix.core import doctor, find_agent, list_agents, render_self_checks, roadmap, scaffold_plan, self_checks, standards


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


def test_roadmap_prioritizes_knox_then_capcom():
    text = roadmap()

    assert "Scaffold Knox" in text
    assert "Scaffold Capcom" in text
    assert "Scaffold Dewey" in text
    assert "agent identity image prompts" in text


def test_scaffold_plan_specializes_knox_and_capcom():
    assert "Touch ID" in scaffold_plan("knox")
    assert "acknowledgement" in scaffold_plan("capcom")
    assert "Code Context Engine" in scaffold_plan("dewey")


def test_doctor_reports_wiki():
    assert any(line.startswith("wiki:") for line in doctor())


def test_self_checks_cover_foss_and_mascot():
    names = {check.name for check in self_checks()}

    assert {"license", "changelog", "contributing", "security", "mascot", "task_list"} <= names
    assert "Felix self-audit:" in render_self_checks()
