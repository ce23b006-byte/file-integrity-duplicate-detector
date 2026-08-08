import json
from pathlib import Path


def generate_report(duplicates, output_file="reports/report.json"):
    """
    Generate a JSON report containing duplicate file information.
    """

    output_path = Path(output_file)

    # Create the reports directory if it doesn't exist.
    output_path.parent.mkdir(parents=True, exist_ok=True)

    report = []

    total_wasted_storage = 0

    for file_hash, files in duplicates.items():

        # All files in a duplicate group have the same size.
        file_size = files[0].stat().st_size

        duplicate_count = len(files)

        # If there are N identical files, only one copy is necessary.
        wasted_storage = file_size * (duplicate_count - 1)

        total_wasted_storage += wasted_storage

        report.append({
            "sha256": file_hash,
            "file_size_bytes": file_size,
            "duplicate_count": duplicate_count,
            "wasted_storage_bytes": wasted_storage,
            "files": [str(file) for file in files]
        })

    final_report = {
        "duplicate_groups": len(report),
        "total_wasted_storage_bytes": total_wasted_storage,
        "groups": report
    }

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(final_report, file, indent=4)

    return output_path