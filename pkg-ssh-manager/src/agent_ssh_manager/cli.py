"""CLI for agent-ssh-manager."""

import argparse
import json
import sys

from agent_ssh_manager import run_remote


def main():
    parser = argparse.ArgumentParser(description="Run commands on remote hosts via SSH")
    parser.add_argument("host", help="Remote hostname or IP")
    parser.add_argument("command", help="Command to execute")
    parser.add_argument("--user", default=None)
    parser.add_argument("--key", default=None, help="SSH private key path")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = run_remote(args.host, args.command, user=args.user, key_path=args.key)

    if args.json:
        payload = {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.exit_code,
        }
        print(json.dumps(payload))
    else:
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)

    sys.exit(result.exit_code)


if __name__ == "__main__":
    main()
