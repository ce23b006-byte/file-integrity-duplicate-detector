import argparse

from src.scanner import scan_directory
from src.duplicate_finder import find_duplicates
from src.reporter import generate_report


def main():
    parser = argparse.ArgumentParser(
        description="File Integrity & Duplicate Detection System"
    )

    parser.add_argument(
        "directory",
        help="Directory to scan"
    )

    parser.add_argument(
        "--report",
        default="reports/report.json",
        help="Path for the JSON report"
    )

    args = parser.parse_args()

    print("\nFile Integrity & Duplicate Detection System")
    print("=" * 50)

    try:
        print(f"Scanning: {args.directory}")

        files = scan_directory(args.directory)

        print(f"Files found: {len(files)}")

        duplicates = find_duplicates(files)

        print(f"Duplicate groups found: {len(duplicates)}")

        if duplicates:
            print("\nDuplicate files:\n")

            for file_hash, matching_files in duplicates.items():

                print(f"SHA-256: {file_hash}")

                for file in matching_files:
                    print(f"  └── {file}")

                print()

        report_path = generate_report(
            duplicates,
            args.report
        )

        print(f"Report saved to: {report_path}")

    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"Error: {error}")

    except KeyboardInterrupt:
        print("\nScan cancelled by user.")


if __name__ == "__main__":
    main()