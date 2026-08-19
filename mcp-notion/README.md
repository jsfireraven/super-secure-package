# MCP Notion Workspace

MCP server for Notion API — pages, databases, and content management.

## Tools

| Tool | Description |
|------|-------------|
| `search_pages` | Search Notion pages and databases |
| `create_page` | Create a new page in a database or parent |
| `update_page` | Update page properties |
| `query_database` | Query a Notion database with filters |
| `append_blocks` | Append content blocks to a page |
| `get_page_content` | Read page blocks as markdown |

## Setup

```bash
pip install -r requirements.txt
export NOTION_API_KEY=secret_...
bash scripts/sync-workspace.sh
python server.py
```
