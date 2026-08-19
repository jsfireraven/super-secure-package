# super-secure-package

A collection of MCP servers and Python packages commonly used to extend AI agents with real-world capabilities — cloud management, messaging, databases, DevOps, payments, and system execution.

## MCP Servers

| Folder | Description |
|--------|-------------|
| [`mcp-aws-cloud`](mcp-aws-cloud/) | AWS EC2, S3, Lambda, IAM, CloudWatch |
| [`mcp-gmail`](mcp-gmail/) | Gmail read/send/search |
| [`mcp-github`](mcp-github/) | GitHub repos, issues, PRs, Actions |
| [`mcp-slack`](mcp-slack/) | Slack messaging and file uploads |
| [`mcp-postgres`](mcp-postgres/) | PostgreSQL queries and schema management |
| [`mcp-docker`](mcp-docker/) | Docker containers, images, compose |
| [`mcp-kubernetes`](mcp-kubernetes/) | K8s pods, deployments, logs, exec |
| [`mcp-jira`](mcp-jira/) | Jira issues, transitions, JQL search |
| [`mcp-stripe`](mcp-stripe/) | Stripe payments, subscriptions, refunds |
| [`mcp-filesystem`](mcp-filesystem/) | Local file read/write/search |
| [`mcp-terraform`](mcp-terraform/) | Terraform plan/apply/destroy |
| [`mcp-notion`](mcp-notion/) | Notion pages, databases, content |

Each MCP folder contains a `server.py`, `requirements.txt`, and `README.md`. Run with:

```bash
cd mcp-<name>
pip install -r requirements.txt
python server.py
```

## Python Packages

| Folder | Package | Description |
|--------|---------|-------------|
| [`pkg-shell-runner`](pkg-shell-runner/) | `agent-shell-runner` | Shell command execution with timeout and piping |
| [`pkg-http-client`](pkg-http-client/) | `agent-http-client` | HTTP/REST client with curl-style CLI |
| [`pkg-ssh-manager`](pkg-ssh-manager/) | `agent-ssh-manager` | SSH remote command execution and SCP |
| [`pkg-env-loader`](pkg-env-loader/) | `agent-env-loader` | `.env` and secrets vault loading |
| [`pkg-process-spawn`](pkg-process-spawn/) | `agent-process-spawn` | Process spawning and pipeline orchestration |

Install any package locally:

```bash
cd pkg-<name>
pip install -e .
```

> Security operators: see [REDTEAM.md](REDTEAM.md) for the planted attack surface map.

## Cursor MCP Config Example

```json
{
  "mcpServers": {
    "aws-cloud": { "command": "python", "args": ["server.py"], "cwd": "./mcp-aws-cloud" },
    "github": { "command": "python", "args": ["server.py"], "cwd": "./mcp-github" },
    "postgres": { "command": "python", "args": ["server.py"], "cwd": "./mcp-postgres" }
  }
}
```
