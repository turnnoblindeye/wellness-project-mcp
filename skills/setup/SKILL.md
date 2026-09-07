---
name: setup
description: Connect the Wellness Project MCP server. Use when the plugin has just been installed, when the user asks how to connect Wellness Project, Apple Health, Fitbit, Oura, or Health Connect to Claude, or when a wellness-project tool call fails with an authentication or "no data" error.
---

# Connecting Wellness Project

The plugin bundles one remote MCP server, `wellness-project`, pointed at
`https://wellnessproject.ai/api/mcp`. It needs a Wellness Project account and an
OAuth authorization before any tool returns data. Walk the user through the two
steps below in order.

## 1. Account and health sources

Tools read only what the user's account already holds, so an empty account
returns empty results rather than an error.

Tell the user to:

1. Create a free account at https://wellnessproject.ai.
2. Open **Settings → Devices** and connect the sources they want: Apple Health,
   Google Health Connect, Fitbit, or Oura.

Manual logging works without any device connected, so a user who only wants to
log workouts and meals by chat can skip step 2.

## 2. Authorize the connection

Run `/mcp`, select **wellness-project**, and choose to authenticate. Claude Code
registers itself dynamically and opens a browser for the Wellness Project OAuth
consent screen. No client ID, client secret, API key, or environment variable is
required.

After the user approves, `/mcp` shows the server as connected and its tools
become available.

## Verifying

Call a cheap read tool and check that it returns the user's own data, for
example `list_workouts` for the last 7 days or `list_body_metrics` for the last
30 days. An empty result means the account has nothing logged for that range,
not that the connection failed.

## Troubleshooting

- **Tools missing after install**: MCP servers register when the plugin loads.
  Restart Claude Code, then re-run `/mcp`.
- **401 or "Unauthorized"**: the OAuth grant expired or was revoked. Re-run
  `/mcp` and re-authenticate.
- **Connected but every read is empty**: no health source is connected and
  nothing has been logged. Return to step 1.
- **Revoking access**: the user can revoke the connection from Wellness Project
  account settings at any time.

## Scope

Every tool is scoped to the signed-in user's own account and enforced by
row-level security. The catalog of tools is in
[TOOLS.md](../../TOOLS.md) and the machine-readable schemas are in
[catalog/tools.json](../../catalog/tools.json).

Wellness Project is informational software, not a medical product.
