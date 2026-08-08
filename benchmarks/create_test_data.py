from pathlib import Path

BASE_DIR = Path("benchmark_data")
FILE_COUNT = 1000

BASE_DIR.mkdir(exist_ok=True)

for i in range(FILE_COUNT):
    file_path = BASE_DIR / f"file_{i}.txt"
    file_path.write_text(f"Test file {i}\n")

print(f"Created {FILE_COUNT} files in {BASE_DIR}")