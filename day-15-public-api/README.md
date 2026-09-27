# Day 15: Call a Public API with Python

## Project

Call a public JSON API, validate its response, and save selected fields to a local file.

The project uses JSONPlaceholder's test endpoint:

```text
https://jsonplaceholder.typicode.com/todos/1
```

## Run it

```bash
python3 api_client.py
cat api-result.json
```

Optional output path:

```bash
python3 api_client.py "$HOME/automation-lab/api-result.json"
```

## Test

The test requires network access. The output must contain the API's ID, title, and completion status:

```bash
python3 api_client.py "$HOME/automation-lab/api-result.json"
grep -q '"id": 1' "$HOME/automation-lab/api-result.json"
grep -q '"title":' "$HOME/automation-lab/api-result.json"
grep -q '"completed":' "$HOME/automation-lab/api-result.json"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

An API returns structured data over HTTP. Python can request that data, parse JSON, validate required fields, and save only the information an automation needs.
