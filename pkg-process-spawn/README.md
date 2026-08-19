# agent-process-spawn

Spawn and orchestrate child processes, background jobs, and command pipelines for AI agent automation.

## Usage

```python
from agent_process_spawn import spawn, spawn_background, wait_all, kill_process, run_pipeline

# Spawn and wait
proc = spawn(["python", "train.py", "--epochs", "10"])
print(proc.wait())

# Background job
job = spawn_background("npm run build")
# ... do other work ...
job.wait()

# Command pipeline
run_pipeline([
    ["psql", "-c", "COPY users TO STDOUT CSV HEADER"],
    ["python", "transform.py"],
    ["curl", "-X", "POST", "-d", "@-", "https://api.example.com/import"],
])
```
