from pathlib import Path
import shutil

BASE_DIR = Path("benchmark_duplicates")

if BASE_DIR.exists():
    shutil.rmtree(BASE_DIR)

BASE_DIR.mkdir()

# 700 unique files
for i in range(700):
    file_path = BASE_DIR / f"unique_{i}.txt"
    file_path.write_text(f"Unique content {i}\n")

# 150 pairs of identical files
for i in range(150):
    original = BASE_DIR / f"original_{i}.txt"
    duplicate = BASE_DIR / f"duplicate_{i}.txt"

    original.write_text(f"Duplicate content group {i}\n")
    shutil.copy2(original, duplicate)

print("Created 1,000 files with 150 duplicate pairs.")