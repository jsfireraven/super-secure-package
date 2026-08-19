# MCP Jira Project Manager

MCP server for Atlassian Jira — create issues, manage sprints, and update tickets.

## Tools

| Tool | Description |
|------|-------------|
| `search_issues` | JQL search for issues |
| `create_issue` | Create a new Jira ticket |
| `update_issue` | Update fields on an issue |
| `add_comment` | Add a comment to an issue |
| `transition_issue` | Move issue through workflow |
| `list_projects` | List accessible Jira projects |

## Setup

```bash
pip install -r requirements.txt
export JIRA_URL=https://yourorg.atlassian.net
export JIRA_EMAIL=you@company.com
export JIRA_API_TOKEN=...
python server.py
```
