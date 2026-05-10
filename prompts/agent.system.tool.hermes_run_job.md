## hermes_run_job

Start a background job on the Hermes Agent. Returns a job_id for polling.

### Parameters
- **prompt** (string, required): Task description for the job.
- **schedule** (string, optional): Cron-style schedule for recurring jobs.
- **base_url** (string, default: "http://127.0.0.1:8642"): Hermes API base URL.
- **api_key** (string, optional): Bearer token.
- **timeout** (number, default: 60): Request timeout.

### Example
```json
{"tool_name": "hermes_run_job", "tool_args": {"prompt": "Analyze all logs for errors"}}
```

### Returns
Job ID string or error message. Use `hermes_check_job` to poll status.
