import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path
import sys

REQUIRED_COLUMNS = {"product", "quantity", "price"}
OUTPUT_COLUMNS = ["product", "quantity", "price", "total"]


def process_sales(input_path: Path, output_path: Path) -> int:
    if not input_path.is_file():
        print(f"Input CSV does not exist: {input_path}")
        return 2

    with input_path.open(newline="", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)
        columns = set(reader.fieldnames or [])
        if not REQUIRED_COLUMNS.issubset(columns):
            missing = ", ".join(sorted(REQUIRED_COLUMNS - columns))
            print(f"Missing required columns: {missing}")
            return 2

        rows: list[dict[str, str]] = []
        try:
            for row in reader:
                quantity = Decimal(row["quantity"])
                price = Decimal(row["price"])
                total = quantity * price
                rows.append(
                    {
                        "product": row["product"],
                        "quantity": str(quantity),
                        "price": f"{price:.2f}",
                        "total": f"{total:.2f}",
                    }
                )
        except (InvalidOperation, TypeError, KeyError) as error:
            print(f"Invalid CSV data: {error}")
            return 2

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} row(s) to {output_path}")
    return 0


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("sales.csv")
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("sales-report.csv")
    return process_sales(input_path, output_path)


if __name__ == "__main__":
    raise SystemExit(main())
