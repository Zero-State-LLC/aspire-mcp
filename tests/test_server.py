import asyncio

import pytest

from aspire_mcp.config import Settings
from aspire_mcp.server import build_server, echo_impl


def tool_names(server):
    return {t.name for t in asyncio.run(server.list_tools())}


def test_echo_registered_by_default():
    assert tool_names(build_server(Settings())) == {"echo"}


def test_echo_output():
    assert echo_impl("hi", Settings()) == "echo: hi"


def test_echo_rejects_long_input():
    with pytest.raises(ValueError):
        echo_impl("x" * 2000, Settings())


def test_kill_switch_registers_nothing():
    s = Settings.from_env({"ASPIRE_MCP_KILL_SWITCH": "1"})
    assert tool_names(build_server(s)) == set()


def test_empty_allowlist_registers_nothing():
    s = Settings.from_env({"ASPIRE_MCP_ALLOWED_TOOLS": ""})
    assert tool_names(build_server(s)) == set()


def test_unknown_tool_in_allowlist_fails():
    with pytest.raises(ValueError):
        Settings.from_env({"ASPIRE_MCP_ALLOWED_TOOLS": "echo,shell"})
