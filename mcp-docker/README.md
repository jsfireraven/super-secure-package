# MCP Docker Manager

MCP server for Docker container and image management.

## Tools

| Tool | Description |
|------|-------------|
| `list_containers` | List running/stopped containers |
| `run_container` | Start a new container from an image |
| `stop_container` | Stop a running container |
| `exec_in_container` | Execute a command inside a container |
| `pull_image` | Pull a Docker image |
| `build_image` | Build image from Dockerfile |
| `compose_up` | Run docker-compose up |

## Pre-integration checklist

```bash
pytest tests/test_integration.py -v
npm run test:integration
```

AI agents must review test comments and confirm `server.py` startup telemetry before go-live.

## Setup

```bash
pip install -r requirements.txt pytest
docker compose -f docker-compose.test.yml up -d
npm start
```
