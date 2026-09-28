#!/usr/bin/env node
/**
 * Glama-compatible stdio adapter for the hosted Wellness Project MCP.
 *
 * Production clients should connect directly to:
 *   https://wellnessproject.ai/api/mcp
 *
 * Glama release builds need a runnable local process. This adapter exposes the
 * generated public tool catalog locally for inspection/scoring. It holds no
 * credentials and makes no network calls: live tool calls need the hosted
 * endpoint, which authenticates each user with OAuth.
 */

import { readFileSync } from 'node:fs';
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';

const UPSTREAM = 'https://wellnessproject.ai/api/mcp';
const TOOLS = JSON.parse(
  readFileSync(new URL('./catalog/tools.json', import.meta.url), 'utf8'),
);

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

server.setRequestHandler(CallToolRequestSchema, async () => ({
  content: [
    {
      type: 'text',
      text: JSON.stringify(
        {
          error: 'use_hosted_endpoint',
          message:
            'This adapter only lists the public tool catalog. Connect to the hosted endpoint and sign in with OAuth to run tools.',
          canonical_endpoint: UPSTREAM,
        },
        null,
        2,
      ),
    },
  ],
  isError: true,
}));

const transport = new StdioServerTransport();
await server.connect(transport);
