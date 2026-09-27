# Day 11: CSV Data Automation

## Project

Read sales data from a CSV file, calculate `quantity * price`, and write a report CSV with a `total` column.

## Input format

```csv
product,quantity,price
Keyboard,2,25.50
Mouse,3,10.00
```

## Run it

```bash
python3 process_sales.py sales.csv sales-report.csv
cat sales-report.csv
```

## Test

```bash
printf 'product,quantity,price\nKeyboard,2,25.50\nMouse,3,10.00\n' > sales.csv
python3 process_sales.py sales.csv sales-report.csv
head -n 1 sales-report.csv | grep -q 'product,quantity,price,total'
grep -q 'Keyboard,2,25.50,51.00' sales-report.csv
grep -q 'Mouse,3,10.00,30.00' sales-report.csv
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Python's `csv` module reads and writes structured table data. `Decimal` calculates money values without the rounding surprises of binary floating-point numbers.
