<p align="center">
  <img src="https://wellnessproject.ai/images/brand/mcp-icon-512.png" alt="Wellness Project" width="220">
</p>

# Wellness Project MCP

[![MCP Marketplace](https://img.shields.io/badge/MCP%20Marketplace-Indexed-blueviolet)](https://getlulu.dev/mcps)
[![MCPVault: claimed](https://mcpvault.io/badge/wellness-project-mcp.svg)](https://mcpvault.io/servers/wellness-project-mcp/health?utm_source=external_badge&utm_medium=referral&utm_campaign=mcp_health_report)
[![MCP status](https://mcpi.app/servers/wellness-project/badge.svg)](https://mcpi.app/servers/wellness-project)
[![Wellness Project MCP server — quality and maintenance score on Glama](https://glama.ai/mcp/servers/turnnoblindeye/wellness-project-mcp/badges/score.svg)](https://glama.ai/mcp/servers/turnnoblindeye/wellness-project-mcp)

**Bring connected health and fitness data into Claude, ChatGPT, Gemini Spark, Grok, Mistral, and other MCP clients.** Wellness Project is a hosted Model Context Protocol server. Your devices and logs sync into one account, and supported assistants can read or update workouts, nutrition, sleep, recovery, body metrics, goals, labs, wellbeing, and more in plain English.

This repository is the public documentation and catalog for the hosted server. It is not a self-hosted backend and contains no private server implementation.

- App: https://wellnessproject.ai
- MCP endpoint: `https://wellnessproject.ai/api/mcp`
- **73 advertised public tools** generated from the production tool registry
- **15 active interactive widgets** for compatible MCP Apps UI clients
- OAuth 2.1 authentication with Dynamic Client Registration

---

## What you can ask

Once connected, ask naturally and the assistant can call the matching Wellness Project tool:

- "How did my training look this week?"
- "Show my sleep for the last month."
- "How is my bench progressing?"
- "Log today's lunch: chicken burrito bowl, about 700 calories."
- "What was my resting heart rate trend vs my HRV this quarter?"
- "How am I doing against my goals?"
- "Log 16 ounces of water."

Read tools return your logged and synced health data. Write tools add, update, or delete entries when you ask. Widget tools can render structured interactive views instead of a wall of numbers.

## Connect Wellness Project to an MCP client

First create an account at https://wellnessproject.ai and connect the health sources you want under **Settings → Devices**. Every client below uses the same hosted endpoint:

`https://wellnessproject.ai/api/mcp`

Authentication is handled by OAuth. Personal API keys are not part of the current public connection flow.

### Claude

1. Open Claude on the web.
2. Go to **Customize → Connectors → Add custom connector**.
3. Paste `https://wellnessproject.ai/api/mcp`.
4. Leave Client ID and Client Secret blank if Claude shows those fields. Claude can register itself dynamically.
5. Sign in to Wellness Project and authorize the connection.

### Claude Code

Claude Code installs Wellness Project as a plugin. The plugin carries nothing but
this server's configuration and a setup skill.

```
/plugin marketplace add turnnoblindeye/wellness-project-mcp
/plugin install wellness-project
```

Restart Claude Code, then run `/mcp`, select **wellness-project**, and authorize.
There is no client ID, client secret, or API key to enter. Run
`/wellness-project:setup` if you would rather be walked through it.

### Cline

Cline connects to Wellness Project as a remote MCP server. Nothing is cloned,
installed, or run locally.

1. Open the **MCP Servers** icon in the Cline sidebar and choose **Remote Servers**.
2. Enter a server name, for example `wellness-project`.
3. Paste `https://wellnessproject.ai/api/mcp` as the server URL and add it.
4. Complete the Wellness Project OAuth flow when Cline opens it in your browser.

To edit `cline_mcp_settings.json` directly instead:

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

Set `"type": "streamableHttp"` explicitly. Cline falls back to the legacy SSE
transport when the type is omitted. There is no client ID, client secret, or API
key to enter. [llms-install.md](./llms-install.md) has the same steps written for
an agent doing the setup.

### ChatGPT

ChatGPT custom MCP apps use developer mode. Current OpenAI availability is plan-dependent: full MCP support including write/modify actions is available in beta for Business, Enterprise, and Edu, while Pro can connect MCPs with read/fetch permissions in developer mode.

1. Enable developer mode for your account or workspace as permitted by your ChatGPT plan.
2. Create a custom MCP app from ChatGPT's Apps settings.
3. Use `https://wellnessproject.ai/api/mcp` as the remote MCP server.
4. Complete the Wellness Project OAuth flow.

OpenAI's current setup and plan details: https://help.openai.com/en/articles/12584461

### Gemini Spark

Custom MCP apps require Gemini Spark access and are added from the Gemini web app.

1. Go to https://gemini.google.com.
2. Open **Settings & help → Connected Apps**. If needed, open **Personal Intelligence → Connected Apps** first.
3. Under **Custom apps for Spark**, choose **Add a custom app**.
4. Enter `https://wellnessproject.ai/api/mcp` and click **Next**.
5. Complete the Wellness Project OAuth flow.

Google's current eligibility and availability rules: https://support.google.com/gemini/answer/17209137

### Grok

1. Go to https://grok.com/connectors and choose **New Connector → Custom**.
2. Paste `https://wellnessproject.ai/api/mcp`.
3. Leave Client ID and Client Secret blank if those fields appear.
4. Complete the Wellness Project OAuth flow.

Grok connector availability may depend on your Grok plan.

### Mistral Le Chat

1. In Le Chat, open **Intelligence → Connectors → Add Connector → Custom MCP Connector**.
2. Paste `https://wellnessproject.ai/api/mcp`.
3. Leave Client ID and Client Secret blank if those fields appear.
4. Complete the Wellness Project OAuth flow.

Workspace permissions may require an owner or admin to add a connector.

## Demo

A short screen recording of the Wellness Project connector running inside ChatGPT:

<video src="https://github.com/turnnoblindeye/wellness-project-mcp/raw/main/media/chatgpt-connector-demo.mp4" controls muted></video>

**[Download / watch the demo](./media/chatgpt-connector-demo.mp4)**

## Interactive widgets

Fifteen active tools render interactive views through the MCP Apps UI extension in compatible clients:

| Ask | Widget tool |
|---|---|
| "Give me a health overview" | `show_health_overview` |
| "How did my Fit Score look?" | `show_week_fit_score` |
| "Show my workouts" | `show_week_workouts` |
| "Show that workout" | `show_workout` |
| "Show my macros" | `show_week_macros` |
| "Show my meal diary" | `show_meal_diary` |
| "How's my sleep trending?" | `show_week_sleep` |
| "Show last night's sleep" | `show_sleep_detail` |
| "Steps this week?" | `show_week_steps` |
| "My weight trend" | `show_body_weight` |
| "Show my body composition" | `show_body_composition` |
| "Recovery trend" | `show_recovery` |
| "How's my running?" | `show_runs` |
| "How's my bench progressing?" | `show_exercise_progression` |
| "Show my wellbeing" | `show_wellbeing` |

Many trend widgets support multiple time ranges; detail widgets use the date or record relevant to the request.

## Tool catalog

The complete production-generated list of **73 advertised public tools**, grouped by domain, is in **[TOOLS.md](./TOOLS.md)**. The machine-readable descriptions, annotations, and JSON Schemas are in **[catalog/tools.json](./catalog/tools.json)**.

Both files are generated from the same production tool registry used by `tools/list`. Admin-only tools and retired tools that remain callable only for older cached clients are not advertised in this catalog.

Do not edit the generated catalog by hand.

## Data sources and integrations

Wellness Project combines native mobile health stores, direct integrations, relay sources, and manual/chat logging.

| Source | Current support |
|---|---|
| Apple Health | Native iOS health and fitness sync |
| Google Health Connect | Native Android health and fitness sync |
| Fitbit / Google Health | Activity, sleep, heart, workout, body, and nutrition data when available |
| Oura | Sleep, readiness/recovery, heart, and activity data |
| Withings | Body, sleep, activity, heart, blood pressure, and other supported health data |
| Wyze | Supported Wyze health data |
| Hevy | Strength workout history via direct integration |
| Ultrahuman | Ring data and supported metabolic/CGM data |
| Liftosaur | Strength workout history via direct integration |
| Polar | Activity, sleep, recovery, heart, and training data |
| WHOOP | Direct integration is rolling out behind availability gating |
| Manual / chat | Workouts, meals, hydration, body metrics, labs, injuries, supplements, goals, wellbeing, and more |

Garmin, Samsung Health, Amazfit/Zepp, Coros, Wahoo, Strava, Peloton, smart scales, and other compatible sources can also reach Wellness Project through Apple Health or Health Connect when those services write the relevant data there.

## Pricing and status

Pricing below reflects the current production configuration as of September 7, 2026. Local app-store pricing may vary.

| Plan | Price | Status |
|---|---:|---|
| Free Basic | $0 | Logging and editing remain free; starting October 15, 2026, Free includes 3 analysis questions per day |
| Founder Pro monthly | $4.99/month | Founder pricing through October 15, 2026 |
| Founder Pro annual | $39.99/year | Founder pricing through October 15, 2026 |
| Founder Lifetime | $199 one-time | Limited founder option, sunsetting |
| Pro monthly | $9.99/month | Standard pricing |
| Pro annual | $99.99/year | Standard pricing |

## Privacy and auth

- The public MCP endpoint uses OAuth 2.1; supported clients can register dynamically.
- Every MCP request is scoped to the authenticated Wellness Project account.
- Row-level security protects user-owned records in the data layer.
- Connector access can be revoked without self-hosting or rotating a long-lived personal API key.

Wellness Project is informational software, not a medical product.

## FAQ

### Do I have to self-host anything?

No. `https://wellnessproject.ai/api/mcp` is the hosted production server. This GitHub repository publishes documentation and schemas only.

### Does the same endpoint work across AI assistants?

Yes. Claude, eligible ChatGPT accounts/workspaces, Gemini Spark, Grok, Mistral, and other compatible remote MCP clients can use the same endpoint. Client-side MCP availability and permissions vary by product and plan.

### Is Wellness Project free?

Free Basic is available. Paid Founder Pro and standard Pro plans add analysis capacity and other paid capabilities; current pricing is listed above.

### Is my health data private?

MCP access requires an authenticated OAuth grant and each tool operates on the signed-in user's account. You can revoke connector access when you no longer want a client connected.

## Related

- Works with Wellness Project: https://wellnessproject.ai/works-with
- Connect Apple Health to Claude: https://wellnessproject.ai/integrations/apple-health-to-claude
- Fitbit MCP: https://wellnessproject.ai/integrations/fitbit-mcp
- Claude integration: https://wellnessproject.ai/integrations/claude
- ChatGPT integration: https://wellnessproject.ai/integrations/chatgpt

## License

The tool catalog and schemas in this repository are published under the [MIT License](./LICENSE) so MCP clients and directories can reference them freely. "Wellness Project" and the app itself remain the property of Wellness Project LLC. See [NOTICE](./NOTICE) for the scope of the grant.
