import json
from pathlib import Path

from .hasher import calculate_hash


def create_baseline(files, baseline_file="reports/baseline.json"):
    """
    Create a baseline containing the SHA-256 hash of every file.
    """

    baseline_path = Path(baseline_file)
    baseline_path.parent.mkdir(parents=True, exist_ok=True)

    baseline = {}

    for file in files:
        try:
            path = Path(file)

            baseline[str(path)] = {
                "sha256": calculate_hash(path),
                "size_bytes": path.stat().st_size,
            }

        except (OSError, PermissionError, RuntimeError):
            continue

    with baseline_path.open("w", encoding="utf-8") as file:
        json.dump(baseline, file, indent=4)

    return baseline_path


def verify_integrity(files, baseline_file="reports/baseline.json"):
    """
    Compare current files against a previously created baseline.

    Returns:
        Dictionary containing unchanged, modified, new, and missing files.
    """

    baseline_path = Path(baseline_file)

    if not baseline_path.exists():
        raise FileNotFoundError(
            f"Baseline file does not exist: {baseline_path}"
        )

    with baseline_path.open("r", encoding="utf-8") as file:
        baseline = json.load(file)

    current_files = {}

    for file in files:
        try:
            path = Path(file)

            current_files[str(path)] = {
                "sha256": calculate_hash(path),
                "size_bytes": path.stat().st_size,
            }

        except (OSError, PermissionError, RuntimeError):
            continue

    unchanged = []
    modified = []
    new = []
    missing = []

    for path, information in current_files.items():

        if path not in baseline:
            new.append(path)

        elif information["sha256"] == baseline[path]["sha256"]:
            unchanged.append(path)

        else:
            modified.append(path)

    for path in baseline:

        if path not in current_files:
            missing.append(path)

    return {
        "unchanged": unchanged,
        "modified": modified,
        "new": new,
        "missing": missing,
    }