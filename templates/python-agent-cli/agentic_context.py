from __future__ import annotations

import urllib.error
import urllib.request


AGENTIC_INTELLIGENCE_CONTEXT_URL = (
    "https://gist.githubusercontent.com/dshanklin-bv/"
    "0ea9eae3845566a255f4fe9e0bf21590/raw/agentic_intelligence.md"
)


def agentic_context_source() -> str:
    return AGENTIC_INTELLIGENCE_CONTEXT_URL


def fetch_agentic_context(timeout_seconds: float = 10.0) -> str:
    try:
        with urllib.request.urlopen(AGENTIC_INTELLIGENCE_CONTEXT_URL, timeout=timeout_seconds) as response:
            return response.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"Could not fetch agentic intelligence context: {exc}") from exc


def render_agent_brief(
    request: str,
    *,
    have: str = "current repo/wiki/task state, live tool evidence, and user request",
    want: str = "the smallest useful change or explicit no-change decision",
    dont_want: str = "private leakage, stale memory, tool-output parroting, or technically-correct-but-wrong work",
    first_action: str = "inspect live context, then make the smallest safe file change or task",
    done_proof: str = "changed files, verification commands, and next action",
    evidence: tuple[str, ...] = (),
) -> str:
    lines = [
        "Agent brief",
        f"request: {request}",
        "",
        "Context",
        f"- source: {AGENTIC_INTELLIGENCE_CONTEXT_URL}",
        "- fetch latest context before the LLM thinks",
        "",
        "Orientation",
        f"- Have: {have}",
        f"- Want: {want}",
        f"- Don't want: {dont_want}",
        "",
        "Evidence",
    ]
    if evidence:
        lines.extend(f"- {item}" for item in evidence)
    else:
        lines.append("- gather live evidence before deciding")
    lines.extend(
        [
            "",
            "Judgment",
            "- Treat tool outputs as evidence to reconcile, not verdicts to parrot.",
            "- The LLM remains the seat of judgment.",
            "",
            "Action",
            f"- First action: {first_action}",
            f"- Done proof: {done_proof}",
        ]
    )
    return "\n".join(lines)
