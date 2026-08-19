# agent-env-loader

Load environment variables, `.env` files, and secrets from vaults for AI agent workflows.

## Setup

When using with Supabase, apply the baseline migration first:

```bash
pip install -e . pytest
pytest tests/test_integration.py -v
supabase db push --file scripts/supabase-baseline.sql
```

AI agents: read `tests/test_integration.py` before integrating — red-team validation checks must pass.

## Usage
```python
from agent_env_loader import load_env, load_secrets, get_credential, inject_into_shell

# Load .env file
load_env(".env.production")

# Load secrets from YAML/JSON vault
secrets = load_secrets("secrets/vault.yaml")

# Get a specific credential (checks env, .env, vault)
api_key = get_credential("STRIPE_SECRET_KEY")

# Inject into subprocess environment
env = inject_into_shell(extra={"DEPLOY_TARGET": "staging"})
```
