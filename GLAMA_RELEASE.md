# Glama release

Wellness Project is a hosted Streamable HTTP MCP at `https://wellnessproject.ai/api/mcp`. This repository remains a public docs/catalog repository; `server.mjs` is only a thin stdio adapter so Glama can build, inspect, score, and deploy the public tool surface without exposing backend implementation code.

Open the Glama build page:

`https://glama.ai/mcp/servers/turnnoblindeye/wellness-project-mcp/admin/dockerfile`

Use this build spec:

- Build steps: `["npm install"]`
- CMD arguments: `["node", "./server.mjs"]`
- Environment variables schema:

```json
{
  "type": "object",
  "properties": {
    "WELLNESS_PROJECT_API_KEY": {
      "type": "string",
      "description": "Personal Wellness Project API key used for live tool calls through the Glama deployment."
    }
  },
  "required": ["WELLNESS_PROJECT_API_KEY"]
}
```

- Placeholder parameters:

```json
{
  "WELLNESS_PROJECT_API_KEY": "glama-build-placeholder"
}
```

Then:

1. Sync Server so Glama checks out current `main` and clear any pinned old commit if shown.
2. Deploy / Build and wait for the build test to pass.
3. Make Release / Build & Release.
4. Publish version `1.0.0` with changelog: `Initial Glama release for the hosted Wellness Project MCP.`

The adapter serves `catalog/tools.json` locally for `tools/list`, so the release build can be inspected without a real user credential. Live `tools/call` requests are forwarded to the canonical hosted MCP using `WELLNESS_PROJECT_API_KEY`.
