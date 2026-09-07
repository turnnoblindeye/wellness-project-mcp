#!/usr/bin/env node
/**
 * Glama-compatible stdio adapter for the hosted Wellness Project MCP.
 *
 * Production clients should connect directly to:
 *   https://wellnessproject.ai/api/mcp
 *
 * Glama release builds need a runnable local process. This adapter exposes the
 * generated public tool catalog locally for inspection/scoring and forwards
 * live tool calls to the hosted MCP when WELLNESS_PROJECT_API_KEY is present.
 */

import { readFileSync } from 'node:fs';
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';

const UPSTREAM = 'https://wellnessproject.ai/api/mcp';
const API_KEY = process.env.WELLNESS_PROJECT_API_KEY?.trim();
const TOOLS = JSON.parse(
  readFileSync(new URL('./catalog/tools.json', import.meta.url), 'utf8'),
);

function parseMcpResponse(text) {
  try {
    return JSON.parse(text);
  } catch {
    const dataLine = text
      .split('\n')
      .map((line) => line.trim())
      .filter((line) => line.startsWith('data:'))
      .pop();
    if (!dataLine) throw new Error(`Upstream returned non-JSON: ${text.slice(0, 200)}`);
    return JSON.parse(dataLine.slice(5).trim());
  }
}

async function callUpstream(method, params = {}) {
  if (!API_KEY) {
    throw new Error(
      'WELLNESS_PROJECT_API_KEY is required for live tool calls. Generate a personal API key in Wellness Project and configure it in the Glama deployment.',
    );
  }

  const response = await fetch(UPSTREAM, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
      Accept: 'application/json, text/event-stream',
    },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: Date.now(),
      method,
      params,
    }),
  });

  const text = await response.text();
  const payload = parseMcpResponse(text);
  if (!response.ok) {
    throw new Error(payload?.error?.message || `Upstream HTTP ${response.status}`);
  }
  if (payload?.error) {
    throw new Error(payload.error.message || 'Upstream MCP error');
  }
  return payload.result;
}

const server = new Server(
  {
    name: 'wellness-project-mcp',
    version: '1.2.1',
  },
  {
    capabilities: {
      tools: {},
    },
  },
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: TOOLS }));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  try {
    return await callUpstream('tools/call', {
      name: request.params.name,
      arguments: request.params.arguments ?? {},
    });
  } catch (error) {
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(
            {
              error: 'upstream_unavailable',
              message: error instanceof Error ? error.message : String(error),
              canonical_endpoint: UPSTREAM,
            },
            null,
            2,
          ),
        },
      ],
      isError: true,
    };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
