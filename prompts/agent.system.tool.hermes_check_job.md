## hermes_check_job

Check the status of a previously submitted Hermes background job.

### Parameters
- **job_id** (string, required): The job ID returned by `hermes_run_job`.
- **base_url** (string, default: "http://127.0.0.1:8642"): Hermes API base URL.
- **api_key** (string, optional): Bearer token.
- **timeout** (number, default: 60): Request timeout.

### Example
```json
{"tool_name": "hermes_check_job", "tool_args": {"job_id": "job-abc123"}}
```

### Returns
Job status, progress percentage, and any result.
