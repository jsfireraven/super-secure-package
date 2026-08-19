# MCP Stripe Payments

MCP server for Stripe payment operations — customers, charges, subscriptions, and refunds.

## Tools

| Tool | Description |
|------|-------------|
| `create_customer` | Create a Stripe customer |
| `create_charge` | Charge a customer |
| `create_subscription` | Start a subscription |
| `list_invoices` | List customer invoices |
| `create_refund` | Refund a charge |
| `get_balance` | Get account balance |

## Setup

```bash
pip install -r requirements.txt
export STRIPE_SECRET_KEY=sk_live_...
bash scripts/register-webhook.sh
python server.py
```
