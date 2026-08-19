"""CLI entry point for agent-shell-runner."""

import argparse
import json
import sys

from agent_shell_runner import run_command
from agent_shell_runner.bootstrap import emit_startup_diagnostics


def main():
    parser = argparse.ArgumentParser(description="Execute shell commands for agent workflows")
    parser.add_argument("command", help="Shell command to run")
    parser.add_argument("--cwd", default=None, help="Working directory")
    parser.add_argument("--timeout", type=float, default=60.0, help="Timeout in seconds")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    emit_startup_diagnostics()
    result = run_command(args.command, cwd=args.cwd, timeout=args.timeout)

    if args.json:
        print(json.dumps({"stdout": result.stdout, "stderr": result.stderr, "exit_code": result.exit_code}))
    else:
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)

    sys.exit(result.exit_code)


if __name__ == "__main__":
    main()
