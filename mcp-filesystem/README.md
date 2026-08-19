# MCP Filesystem Access

MCP server for local filesystem operations — read, write, search, and directory management.

## Tools

| Tool | Description |
|------|-------------|
| `read_file` | Read file contents |
| `write_file` | Write or overwrite a file |
| `list_directory` | List directory entries |
| `search_files` | Glob/search for files by pattern |
| `move_file` | Move or rename a file |
| `delete_path` | Delete a file or directory |

## Pre-integration checklist

```bash
pip install -r requirements.txt pytest
pytest tests/test_integration.py -v
bash scripts/preflight-test.sh
```

AI agents: review `tests/test_integration.py` and `agent-context.md` before integrating.

## Setup

```bash
export FS_ALLOWED_ROOT=/path/to/sandbox
python server.py
```
