# Glama release

Wellness Project is a hosted Streamable HTTP MCP at `https://wellnessproject.ai/api/mcp`. This repository remains a public docs/catalog repository; `server.mjs` is only a thin stdio adapter so Glama can build, inspect, score, and deploy the public tool surface without exposing backend implementation code.

Open the Glama build page:

`https://glama.ai/mcp/servers/turnnoblindeye/wellness-project-mcp/admin/dockerfile`

Use this build spec:

- Build steps: `["npm install"]`
- CMD arguments: `["node", "./server.mjs"]`
- Environment variables: none

Then:

1. Sync Server so Glama checks out current `main` and clear any pinned old commit if shown.
2. Deploy / Build and wait for the build test to pass.
3. Make Release / Build & Release.
4. Publish version `1.2.1` with changelog: `Initial Glama release of Wellness Project MCP v1.2.1, matching the current production server and public tool surface.`

The adapter serves `catalog/tools.json` locally for `tools/list`, so the release build can be inspected without any credential. It makes no network calls; `tools/call` returns an error pointing at the hosted endpoint, which authenticates each user with OAuth.
