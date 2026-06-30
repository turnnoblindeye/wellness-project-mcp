# Wellness Project MCP

**Connect Apple Health, Fitbit, Oura, and Google Health Connect to Claude and ChatGPT.** Wellness Project is a hosted Model Context Protocol (MCP) server: your devices sync into one account, and Claude or ChatGPT read your workouts, sleep, nutrition, and recovery in plain English. No exports, no copy-paste, no community server to self-host.

Wellness Project is a free AI health app. This repository documents its public MCP server: the tool catalog, the schemas, the inline-chart widgets, and how to connect any MCP client to it.

- App: https://wellnessproject.ai
- MCP endpoint: `https://wellnessproject.ai/api/mcp`
- 60 tools across workouts, nutrition, sleep, wearables, body metrics, labs, recovery, runs, and more
- 11 interactive chart widgets rendered inline in Claude and ChatGPT

---

## Why this exists

Most health and fitness services ship no MCP server of their own. There is **no official Fitbit MCP server, no Oura MCP server, no Hevy or TrainingPeaks MCP server**, so Claude and ChatGPT cannot read that data on their own. The GitHub results for those queries are mostly unmaintained community repos you would have to run, refresh tokens for, and keep alive yourself.

Wellness Project is the hosted alternative. It connects to your devices over OAuth, ingests your workouts and recovery data, and exposes all of it to any MCP client through one authenticated endpoint. You connect once and it stays connected.

## What you can ask

Once connected, you ask your AI naturally and it calls the matching tool:

- "How did my training look this week?"
- "Show my sleep for the last month."
- "How is my bench progressing?"
- "Log today's lunch: chicken burrito bowl, about 700 calories."
- "What was my resting heart rate trend vs my HRV this quarter?"
- "How many rest days did I take this month?"

Read tools pull your logged and synced data. Write tools log new entries. Chart tools render an interactive inline graph instead of a wall of numbers.

## Connect Apple Health, Fitbit, or Oura to Claude

Connect your device once at wellnessproject.ai, then add the MCP server to Claude or ChatGPT. The same hosted endpoint serves both, so connecting Apple Health to Claude, Fitbit to ChatGPT, or Oura to either works the same way. The steps are below.

## Connect to Claude

**claude.ai (remote connector, recommended)**
1. Create a free account at https://wellnessproject.ai and connect a device (Settings → Integrations).
2. In Claude, go to **Settings → Connectors → Add custom connector**.
3. Paste `https://wellnessproject.ai/api/mcp` and authorize with OAuth.

That is it. The connector carries across every conversation.

**Desktop / scripted clients (API key)**

Headless and desktop clients use a long-lived personal API key instead of the OAuth flow. Generate one in **Settings → Claude** inside the app. The server speaks streamable-HTTP MCP and authenticates with a bearer token:

```
POST https://wellnessproject.ai/api/mcp
Authorization: Bearer YOUR_PERSONAL_API_KEY
```

For a client that supports remote HTTP MCP servers with custom headers, point it at that URL with the `Authorization` header above. For a stdio-only client, bridge to it with [`mcp-remote`](https://www.npmjs.com/package/mcp-remote):

```json
{
  "mcpServers": {
    "wellness-project": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://wellnessproject.ai/api/mcp",
        "--header",
        "Authorization: Bearer YOUR_PERSONAL_API_KEY"
      ]
    }
  }
}
```

Rotate or revoke the key from the same settings screen at any time.

## Connect to ChatGPT

The same server backs ChatGPT. Connect Wellness Project as a custom connector / plugin pointed at `https://wellnessproject.ai/api/mcp` and authorize. The identical tools and widgets are available there.

## Demo

A short screen recording of the Wellness Project connector running inside ChatGPT: connecting, asking questions in plain English, and the tools returning live data.

<video src="https://github.com/turnnoblindeye/wellness-project-mcp/raw/main/media/chatgpt-connector-demo.mp4" controls muted></video>

**[Download / watch the demo](./media/chatgpt-connector-demo.mp4)**

## Inline chart widgets

Eleven tools render interactive charts inline through the [MCP Apps UI](https://modelcontextprotocol.io) extension, not plain text:

| Ask | Widget |
|---|---|
| "How did my week look?" | weekly Fit Score |
| "Break down my Fit Score" | today's Fit Score by component |
| "Show my workouts" | training activity + heart points |
| "Show that workout" | a single session's exercises and sets |
| "Show my macros" | calories + protein/carbs/fat vs targets |
| "How's my sleep?" | hours + sleep score |
| "Steps this week?" | step counts vs goal |
| "How's my running?" | running mileage |
| "My weight trend" | body weight + body-fat % |
| "Recovery trend" | resting heart rate + HRV |
| "How's my bench progressing?" | estimated 1RM progression |

Each chart has a 7d / 30d / 90d / 1y range toggle and hover tooltips, and reads live from your own account.

## Tool catalog

The full list of 60 tools, grouped by domain, is in **[TOOLS.md](./TOOLS.md)**. The machine-readable schemas (name, description, JSON Schema input, MCP annotations) are in **[catalog/tools.json](./catalog/tools.json)** and mirror exactly what the server returns from `tools/list`.

Every tool sets standard MCP annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`). All tools have `openWorldHint: false`: they operate only on the authenticated user's own account data.

## Data sources

| Source | Syncs |
|---|---|
| Apple Health (HealthKit) | steps, sleep, heart rate, HRV |
| Google Health Connect | steps, sleep, heart rate, HRV |
| Fitbit | steps, Active Zone Minutes, sleep stages, resting heart rate, HRV |
| Oura | sleep, readiness, heart rate, HRV |
| Manual / chat | workouts, meals, body metrics, labs, injuries, supplements, and more |

## Privacy and auth

- Access is authenticated per user, by OAuth (claude.ai) or a personal API key (Desktop and scripted clients).
- API keys are stored hashed; the plaintext is shown to you once and never persisted.
- Every tool is scoped to the signed-in user. Row-level security enforces that a token can only read or write its own account.
- You can revoke a connector or rotate a key from app settings at any time.

Wellness Project is informational software, not a medical product.

## FAQ

### How do I connect Apple Health to Claude?
Create a free account at wellnessproject.ai and sync Apple Health (Settings, Integrations). In Claude, open Settings, Connectors, Add custom connector, paste `https://wellnessproject.ai/api/mcp`, and authorize. Claude can then read your Apple Health data in any conversation.

### How do I connect Fitbit to Claude and ChatGPT?
Connect Fitbit once at wellnessproject.ai over OAuth. Then add `https://wellnessproject.ai/api/mcp` as a custom connector in Claude or as a custom connector in ChatGPT. One connection serves both assistants.

### How do I connect Oura to Claude?
Connect Oura at wellnessproject.ai, then add the same MCP endpoint in Claude. Your Oura sleep, readiness, and HRV become available to ask about in plain English.

### Is there an official Fitbit, Oura, or Apple Health MCP server?
No. None of these ship their own MCP server, and the community repos you find on GitHub are unofficial servers you have to run and refresh tokens for yourself. Wellness Project is the hosted alternative: connect your device once and it stays connected, with nothing to self-host.

### Does this work with ChatGPT as well as Claude?
Yes. The same server backs both. Point a custom connector at `https://wellnessproject.ai/api/mcp` in either tool.

### Do I have to self-host or run anything?
No. The server is hosted. You connect your devices through the app and add one URL to your AI client.

### Is it free?
Yes. Wellness Project is free during early access.

### Is my health data private?
Access is authenticated per user by OAuth or a personal API key. Every tool is scoped to the signed-in user, row-level security enforces that a token reads only its own account, and you can revoke access at any time.

## Related

- Connect Apple Health to Claude: https://wellnessproject.ai/integrations/apple-health-to-claude
- Connect Fitbit to Claude and ChatGPT: https://wellnessproject.ai/integrations/fitbit-mcp
- Claude integration: https://wellnessproject.ai/integrations/claude
- ChatGPT integration: https://wellnessproject.ai/integrations/chatgpt

## License

The tool catalog and schemas in this repository are published under [CC BY 4.0](./LICENSE) so MCP clients and directories can reference them freely. "Wellness Project" and the app itself remain the property of Wellness Project LLC.
