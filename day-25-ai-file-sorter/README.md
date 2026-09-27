# Day 25: AI File Sorter

## Project

Classify text documents by their contents and move them into category folders.

Categories:

- `invoices/`
- `resumes/`
- `reports/`
- `unknown/`

This is a local classifier baseline. A hosted AI model can replace `classify_document` later.

## Run it

```bash
python3 sort_documents.py SOURCE_FOLDER DESTINATION_FOLDER
```

## Test

```bash
rm -rf "$HOME/automation-lab/documents" "$HOME/automation-lab/sorted-documents"
mkdir -p "$HOME/automation-lab/documents"
printf 'Invoice payment amount total due\n' > "$HOME/automation-lab/documents/invoice.txt"
printf 'Resume experience skills education\n' > "$HOME/automation-lab/documents/resume.txt"
printf 'Report summary analysis findings\n' > "$HOME/automation-lab/documents/report.txt"
printf 'Personal notes about gardening\n' > "$HOME/automation-lab/documents/notes.txt"
python3 sort_documents.py "$HOME/automation-lab/documents" "$HOME/automation-lab/sorted-documents"

test -f "$HOME/automation-lab/sorted-documents/invoices/invoice.txt"
test -f "$HOME/automation-lab/sorted-documents/resumes/resume.txt"
test -f "$HOME/automation-lab/sorted-documents/reports/report.txt"
test -f "$HOME/automation-lab/sorted-documents/unknown/notes.txt"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

AI automation often starts by turning unstructured input into a category. Once classified, each category can trigger a different action.
