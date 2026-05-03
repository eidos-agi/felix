from __future__ import annotations

import argparse

from .agentic_context import agentic_context_source, fetch_agentic_context, render_agent_brief


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="<agent-cli>")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("agentic-context", help="fetch the latest Agentic Intelligence context")
    subparsers.add_parser("agentic-context-source", help="show the live Agentic Intelligence context URL")
    agent_parser = subparsers.add_parser("agent", help="turn a request into an agent action brief")
    agent_parser.add_argument("request")
    agent_parser.add_argument("--have", default="current repo/wiki/task state, live tool evidence, and user request")
    agent_parser.add_argument("--want", default="the smallest useful change or explicit no-change decision")
    agent_parser.add_argument(
        "--dont-want",
        default="private leakage, stale memory, tool-output parroting, or technically-correct-but-wrong work",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "agentic-context":
        print(fetch_agentic_context())
        return 0

    if args.command == "agentic-context-source":
        print(agentic_context_source())
        return 0

    if args.command == "agent":
        print(render_agent_brief(args.request, have=args.have, want=args.want, dont_want=args.dont_want))
        return 0

    parser.error("unhandled command")
    return 2
