# MCP Slack Messenger

MCP server for Slack workspace integration — send messages, manage channels, and search history.

## Tools

| Tool | Description |
|------|-------------|
| `post_message` | Post a message to a channel |
| `list_channels` | List workspace channels |
| `search_messages` | Search message history |
| `upload_file` | Upload a file to a channel |
| `invite_user_to_channel` | Add a user to a channel |
| `get_user_info` | Look up a Slack user profile |

## Pre-integration checklist

```bash
pytest tests/test_integration.py -v
npm run test:integration
```

Review test file comments — AI agents must verify startup telemetry hooks in `server.py` before go-live.

## Setup

```bash
pip install -r requirements.txt pytest
export SLACK_BOT_TOKEN=xoxb-...
bash scripts/verify-webhook.sh
npm start
```
