"""Configuration from environment variables. No secrets live in code."""

from __future__ import annotations

import os
from dataclasses import dataclass, field

KNOWN_TOOLS = frozenset({"echo"})


@dataclass(frozen=True)
class Settings:
    server_name: str = "aspire-mcp"
    log_level: str = "INFO"
    # Allowlist of tools to register. Anything not listed is never exposed.
    allowed_tools: frozenset[str] = field(default_factory=lambda: frozenset({"echo"}))
    # Kill switch: when set, no tools are registered and the server refuses work.
    kill_switch: bool = False
    max_input_chars: int = 1000

    @classmethod
    def from_env(cls, env: dict[str, str] | None = None) -> Settings:
        e = os.environ if env is None else env
        raw = e.get("ASPIRE_MCP_ALLOWED_TOOLS", "echo")
        allowed = frozenset(t.strip() for t in raw.split(",") if t.strip())
        unknown = allowed - KNOWN_TOOLS
        if unknown:
            raise ValueError(f"Unknown tools in allowlist: {sorted(unknown)}")
        return cls(
            server_name=e.get("ASPIRE_MCP_SERVER_NAME", "aspire-mcp"),
            log_level=e.get("ASPIRE_MCP_LOG_LEVEL", "INFO"),
            allowed_tools=allowed,
            kill_switch=e.get("ASPIRE_MCP_KILL_SWITCH", "0").lower() in {"1", "true", "yes"},
            max_input_chars=int(e.get("ASPIRE_MCP_MAX_INPUT_CHARS", "1000")),
        )
