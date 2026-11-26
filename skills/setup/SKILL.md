---
name: setup
description: Help users connect Wellness Project, authorize the remote MCP connector, and troubleshoot missing or unavailable health and fitness data.
---

# Connecting Wellness Project

Wellness Project connects Claude to the user's own account through the hosted HTTPS MCP server at https://wellnessproject.ai/api/mcp. It requires OAuth authorization. Use this skill when the user requests setup or troubleshooting; installation alone does not authorize reading or changing personal records.

## Account and health sources

Ask the user to sign in or create an account at https://wellnessproject.ai. Under Settings > Devices they can connect their preferred supported sources, such as Apple Health, Google Health Connect, Fitbit, Garmin, Oura or WHOOP, subject to availability. Manual logging works without a wearable.

## Authorize the connection

In Claude, open the connector settings and connect Wellness Project. In Claude Code, use the MCP connection menu and select wellness-project to authenticate. The user signs in and approves the OAuth consent screen. No API key, client secret or manual credential sharing is required. Do not ask the user to share credentials in chat.

## Verify and troubleshoot

Check connection status without retrieving health records when possible. If the user requests a data check, or explicitly agrees to one, use a relevant read tool with the smallest useful date range. An empty result can mean no records are available for that period, rather than a failed connection.

- If tools are unavailable, check whether the plugin is enabled and the connector is authorized.
- For an authorization error, have the user reconnect through OAuth.
- For missing data, check that the relevant source is connected and syncing.
- Users can revoke connector access in their Wellness Project account settings.

Only access the data needed for the user's request. Do not create, modify or delete records during setup or troubleshooting. Explain any intended changes and obtain confirmation when the request is ambiguous.

See the [Claude integration guide](https://wellnessproject.ai/integrations/claude), [privacy policy](https://wellnessproject.ai/privacy) and [support](https://wellnessproject.ai/support). Wellness Project is informational software, not a medical device.
