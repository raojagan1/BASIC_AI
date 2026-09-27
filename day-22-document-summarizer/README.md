# Day 22: Document Summarizer

## Project

Read a text document and create a short extractive summary from its most important sentences.

This local baseline ranks sentences by repeated meaningful words. It is a practical starting point before replacing the `summarize` function with a hosted AI model.

## Run it

```bash
python3 summarize_document.py document.txt summary.txt
cat summary.txt
```

## Test

```bash
printf '%s\n' \
  'Automation saves time by handling repetitive work.' \
  'Good automation records results and handles errors.' \
  'A mountain landscape can be beautiful.' \
  'Reliable automation saves time and records useful results.' \
  > document.txt
python3 summarize_document.py document.txt summary.txt

test -s summary.txt
grep -q 'Automation saves time' summary.txt
grep -q 'Reliable automation saves time' summary.txt
test "$(wc -l < summary.txt)" -eq 1
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Summarization reduces a long document to its strongest sentences. Extractive methods select original text, while generative AI writes new summary text.
