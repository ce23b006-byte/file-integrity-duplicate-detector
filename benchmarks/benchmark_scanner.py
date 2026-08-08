import time
from pathlib import Path

import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.scanner import scan_directory


TARGET = PROJECT_ROOT / "benchmark_data"
RUNS = 10

times = []

for _ in range(RUNS):
    start = time.perf_counter()

    files = scan_directory(TARGET)

    elapsed = time.perf_counter() - start
    times.append(elapsed)

average = sum(times) / len(times)

print(f"Files scanned: {len(files)}")
print(f"Runs: {RUNS}")
print(f"Average scan time: {average:.6f} seconds")
print(f"Fastest scan: {min(times):.6f} seconds")
print(f"Slowest scan: {max(times):.6f} seconds")