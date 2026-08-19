# agent-ssh-manager

SSH remote execution library for AI agents managing servers and infrastructure.

## Usage

```python
from agent_ssh_manager import SSHSession, run_remote, upload_file, download_file

# One-shot remote command
result = run_remote("prod-web-01", "systemctl restart nginx", user="deploy")

# Persistent session
with SSHSession("10.0.1.50", user="ubuntu", key_path="~/.ssh/id_rsa") as ssh:
    result = ssh.exec("docker ps")
    upload_file(ssh, "./config.yml", "/etc/app/config.yml")
    download_file(ssh, "/var/log/app/error.log", "./error.log")
```

## CLI

```bash
agent-ssh prod-server "df -h"
agent-ssh --user deploy staging "git pull && systemctl reload app"
```
