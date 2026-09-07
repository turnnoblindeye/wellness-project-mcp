# Installing Wellness Project MCP

Instructions for an AI agent (Cline, Claude Code, Cursor, or similar) setting up
this server on a user's behalf.

## What this is

Wellness Project is a **hosted remote MCP server**. There is nothing to clone,
build, install, or run. This repository is documentation and a generated tool
catalog only. It contains no server implementation.

- Endpoint: `https://wellnessproject.ai/api/mcp`
- Transport: Streamable HTTP
- Auth: OAuth 2.1 with Dynamic Client Registration
- Official MCP Registry name: `ai.wellnessproject/wellness-project`

Do not set this up as a local `stdio` server. The `server.mjs` and `package.json`
at the repository root are a Glama build adapter, not the way users connect: the
adapter serves the static tool catalog and forwards live calls only when a
personal `WELLNESS_PROJECT_API_KEY` is set, and personal API keys are not part of
the public connection flow. Running `npm start` will produce a server that cannot
answer a single real query. Configure the remote endpoint instead.

## Prerequisite

The user needs a Wellness Project account at https://wellnessproject.ai. Health
sources are connected in the app under **Settings → Devices**. The MCP server
returns that account's own data, so a brand new account with nothing synced will
return empty results rather than an error.

## Setup: Cline

Add it as a remote server. Either use the UI (**MCP Servers → Remote Servers**,
name it `wellness-project`, URL `https://wellnessproject.ai/api/mcp`), or write
`cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "wellness-project": {
      "type": "streamableHttp",
      "url": "https://wellnessproject.ai/api/mcp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

`"type": "streamableHttp"` is required. Omitting it makes Cline fall back to the
legacy SSE transport.

Do not invent `command`, `args`, or `env` entries. Do not add an `Authorization`
header or ask the user for an API key. Authentication is browser-based OAuth.

## Setup: other MCP clients

Any client that supports remote Streamable HTTP MCP servers uses the same URL.
For a generic JSON config:

```json
{
  "mcpServers": {
    "wellness-project": {
      "type": "http",
      "url": "https://wellnessproject.ai/api/mcp"
    }
  }
}
```

Claude Code can instead install the bundled plugin:

```
/plugin marketplace add turnnoblindeye/wellness-project-mcp
/plugin install wellness-project
```

## Authorizing

After the server is registered, the client starts an OAuth 2.1 flow and the user
signs in to Wellness Project in a browser. The client registers itself
dynamically, so there is no client ID or client secret to enter anywhere.

An agent cannot complete this step alone. Hand it to the user, wait for them to
confirm they authorized, then continue.

## Verifying the install

Ask the client to list tools. A working connection advertises the public tool
catalog documented in [TOOLS.md](./TOOLS.md), including `list_workouts`,
`list_sleep`, `list_meals`, and the `show_*` widget tools.

A quick end-to-end check: ask "show my health overview". That calls
`show_health_overview`, which renders an interactive widget in clients that
support the MCP Apps UI extension and returns structured data elsewhere.

## Troubleshooting

- **405 or a transport error on connect**: the client is using SSE. Set the
  transport type to Streamable HTTP explicitly.
- **401 or repeated auth prompts**: the OAuth grant was not completed or was
  revoked. Re-run the client's authorize step.
- **Tools list is empty**: the connection is not authorized yet.
- **Tools return no data**: the account is authenticated but has nothing logged
  or synced yet. Connect a source in the app under **Settings → Devices**.
