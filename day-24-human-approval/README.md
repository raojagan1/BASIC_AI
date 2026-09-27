# Day 24: Human Approval Workflow

## Project

Require explicit human approval before an automated action can execute.

Workflow:

```text
create -> approve -> execute
```

## Run it

```bash
python3 approval_workflow.py --state approval-state.json create "Create a customer reply"
python3 approval_workflow.py --state approval-state.json approve
python3 approval_workflow.py --state approval-state.json execute executed-action.txt
```

## Test

Execution must be blocked before approval and must work afterward:

```bash
rm -f approval-state.json executed-action.txt
python3 approval_workflow.py --state approval-state.json create "Create a customer reply"
if python3 approval_workflow.py --state approval-state.json execute executed-action.txt; then
    echo "FAIL: unapproved action was executed"
    exit 1
fi
test ! -e executed-action.txt
python3 approval_workflow.py --state approval-state.json approve
python3 approval_workflow.py --state approval-state.json execute executed-action.txt
grep -q 'Executed approved action' executed-action.txt
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Approval is a control boundary in AI automation. An AI system may propose an action, but a human can review and approve it before anything consequential happens.
