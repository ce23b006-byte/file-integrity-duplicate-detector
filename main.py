import argparse

from src.scanner import scan_directory
from src.duplicate_finder import find_duplicates
from src.reporter import generate_report
from src.integrity import create_baseline, verify_integrity


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
        help="Path for the duplicate JSON report"
    )

    parser.add_argument(
        "--baseline",
        action="store_true",
        help="Create a SHA-256 integrity baseline"
    )

    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify files against the existing integrity baseline"
    )

    args = parser.parse_args()

    print("\nFile Integrity & Duplicate Detection System")
    print("=" * 50)

    try:
        print(f"Scanning: {args.directory}")

        files = scan_directory(args.directory)

        print(f"Files found: {len(files)}")

        # Integrity baseline creation
        if args.baseline:
            baseline_path = create_baseline(files)

            print(f"\nIntegrity baseline created: {baseline_path}")

        # Integrity verification
        if args.verify:
            result = verify_integrity(files)

            print("\nIntegrity Verification")
            print("-" * 30)

            print(f"Unchanged files: {len(result['unchanged'])}")
            print(f"Modified files: {len(result['modified'])}")
            print(f"New files: {len(result['new'])}")
            print(f"Missing files: {len(result['missing'])}")

            if result["modified"]:
                print("\nModified files:")

                for file in result["modified"]:
                    print(f"  └── {file}")

            if result["new"]:
                print("\nNew files:")

                for file in result["new"]:
                    print(f"  └── {file}")

            if result["missing"]:
                print("\nMissing files:")

                for file in result["missing"]:
                    print(f"  └── {file}")

        # Duplicate detection
        duplicates = find_duplicates(files)

        print(f"\nDuplicate groups found: {len(duplicates)}")

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