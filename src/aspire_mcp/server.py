"""Minimal MCP server skeleton (stdio transport, local only).

Starting point only. TODO(arshi): auth (mTLS or local tokens), RBAC per role,
tamper-evident audit log, PII redaction and output gating.
"""

from __future__ import annotations

import json
import logging
import sys
from datetime import UTC, datetime

from mcp.server.mcpserver import MCPServer

from aspire_mcp.config import Settings

log = logging.getLogger("aspire_mcp")


def audit(tool: str, inputs: dict, output_summary: str) -> None:
    """Placeholder audit record to stderr. TODO(arshi): tamper-evident, exportable store."""
    record = {
        "ts": datetime.now(UTC).isoformat(),
        "caller": "TODO",  # TODO(arshi): authenticated caller identity
        "tool": tool,
        "inputs": inputs,
        "output_summary": output_summary,
    }
    print(json.dumps(record), file=sys.stderr)


def echo_impl(text: str, settings: Settings) -> str:
    """Harmless example tool logic with basic input validation."""
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if len(text) > settings.max_input_chars:
        raise ValueError(f"text exceeds {settings.max_input_chars} characters")
    cleaned = "".join(ch for ch in text if ch.isprintable())
    return f"echo: {cleaned}"


def build_server(settings: Settings | None = None) -> MCPServer:
    settings = settings or Settings.from_env()
    mcp = MCPServer(settings.server_name)

    if settings.kill_switch:
        log.warning("Kill switch is on; no tools registered.")
        return mcp

    if "echo" in settings.allowed_tools:

        @mcp.tool()
        def echo(text: str) -> str:
            """Echo back the given text (example tool, read-only, no side effects)."""
            result = echo_impl(text, settings)
            audit("echo", {"text_len": len(text)}, f"{len(result)} chars")
            return result

    return mcp


def main() -> None:
    settings = Settings.from_env()
    logging.basicConfig(level=settings.log_level, stream=sys.stderr)
    build_server(settings).run()  # stdio transport


if __name__ == "__main__":
    main()
