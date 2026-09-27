# Day 21: AI Text Classifier Baseline

## Project

Classify text into `billing`, `technical`, `support`, or `other` categories.

This local baseline uses weighted keyword matching. It teaches the same automation shape as an AI classifier without requiring an API key. Later, the `classify` function can be replaced with a model call while keeping the file and command workflow.

## Run it

```bash
python3 classify_text.py "My invoice payment was charged twice"
python3 classify_text.py "The server crashes when I try to login"
```

You can also classify a text file:

```bash
python3 classify_text.py message.txt
```

## Test

```bash
test "$(python3 classify_text.py 'My invoice payment was charged twice' | head -n 1)" = 'category=billing'
test "$(python3 classify_text.py 'The server crashes when I try to login' | head -n 1)" = 'category=technical'
test "$(python3 classify_text.py 'How can I get help with this request?' | head -n 1)" = 'category=support'
test "$(python3 classify_text.py 'The weather is sunny today' | head -n 1)" = 'category=other'
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

A classifier converts unstructured text into a category that an automation can act on. A keyword baseline is easy to test and provides a local starting point before adding a hosted AI model.
