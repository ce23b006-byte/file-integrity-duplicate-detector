import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.scanner import scan_directory
from src.duplicate_finder import find_duplicates


TARGET = PROJECT_ROOT / "benchmark_duplicates"
RUNS = 10

files = scan_directory(TARGET)

times = []
duplicate_count = 0

for _ in range(RUNS):
    start = time.perf_counter()

    duplicates = find_duplicates(files)

    elapsed = time.perf_counter() - start
    times.append(elapsed)

    duplicate_count = sum(
        len(group) for group in duplicates.values()
    )

average = sum(times) / len(times)

print(f"Files scanned: {len(files)}")
print(f"Duplicate files found: {duplicate_count}")
print(f"Runs: {RUNS}")
print(f"Average detection time: {average:.6f} seconds")
print(f"Fastest detection: {min(times):.6f} seconds")
print(f"Slowest detection: {max(times):.6f} seconds")