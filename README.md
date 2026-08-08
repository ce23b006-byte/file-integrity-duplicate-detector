# File Integrity & Duplicate Detector

A Python-based command-line tool that scans directories, detects duplicate files using file size and SHA-256 hashing, and generates a detailed JSON report.

The project is designed to be **memory-efficient, modular, testable, and easy to extend**.

---

## 🚀 Features

* 🔍 Recursively scans directories for files
* 📁 Supports nested folders
* ⚡ Uses file size as a fast pre-filter
* 🔐 Uses SHA-256 hashing for content verification
* 💾 Hashes files in chunks to reduce memory usage
* 🧩 Groups files with identical content
* 📊 Calculates duplicate files and wasted storage
* 📄 Generates JSON reports
* ⚠️ Handles invalid directory paths gracefully
* 🧪 Includes automated unit tests
* 🧱 Modular project structure for easy extension

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Hashing:** SHA-256
* **Testing:** pytest
* **Version Control:** Git
* **Repository:** GitHub

---

## 📂 Project Structure

```text
file-integrity-duplicate-detector/
│
├── src/
│   ├── scanner.py
│   ├── hasher.py
│   ├── duplicate_finder.py
│   └── reporter.py
│
├── tests/
│   ├── test_hasher.py
│   └── test_duplicate_finder.py
│
├── test_files/
│   ├── file1.txt
│   ├── file2.txt
│   └── ...
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

The duplicate detection process uses multiple stages to avoid unnecessary hashing.

```text
                Directory
                    │
                    ▼
             Recursive Scan
                    │
                    ▼
              Find Files
                    │
                    ▼
             Group by Size
                    │
          ┌─────────┴─────────┐
          │                   │
     Unique Size        Same Size
          │                   │
       Ignore                 ▼
                         SHA-256 Hash
                              │
                              ▼
                    Group Matching Hashes
                              │
                              ▼
                     Duplicate Groups
                              │
                              ▼
                         JSON Report
```

### Why group by file size first?

Two files with different sizes cannot contain exactly the same data.

Therefore, the program first groups files by their size and only hashes files that have the same size as another file.

This reduces unnecessary hashing operations, especially when scanning directories containing many unique files.

---

## 🔐 SHA-256 File Hashing

Files are hashed using SHA-256.

Instead of loading an entire file into memory, the program reads the file in chunks.

```python
with open(file_path, "rb") as file:
    while chunk := file.read(1024 * 1024):
        sha256.update(chunk)
```

The current implementation uses a **1 MB chunk size**.

This allows the program to process large files without allocating memory proportional to the entire file size.

---

## 📊 Duplicate Detection

Two files are considered duplicates when:

```text
File A size == File B size
             AND
File A SHA-256 == File B SHA-256
```

For example:

```text
documents/
├── report.pdf
├── backup/
│   └── report.pdf
└── old/
    └── report.pdf
```

If all three files have the same size and SHA-256 hash, they are placed in the same duplicate group.

---

## 💾 Wasted Storage Calculation

For every duplicate group, the program calculates the storage occupied by redundant copies.

For `N` identical files of size `S`:

```text
Wasted Storage = S × (N - 1)
```

For example:

```text
File size:       100 MB
Copies:          4

Wasted storage = 100 × (4 - 1)
               = 300 MB
```

The first copy can be retained while the remaining copies represent potentially recoverable storage.

---

## 📄 JSON Report

The program can generate a JSON report containing duplicate information.

Example:

```json
{
    "duplicate_groups": [
        {
            "hash": "example_sha256_hash",
            "size": 1024,
            "files": [
                "folder1/file.txt",
                "folder2/file.txt"
            ]
        }
    ]
}
```

The report can be used for further analysis or integrated into another application.

---

# 💻 Installation

## 1. Clone the repository

```bash
git clone https://github.com/ce23b006-byte/file-integrity-duplicate-detector.git
```

## 2. Enter the project directory

```bash
cd file-integrity-duplicate-detector
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

## Scan a directory

```bash
python main.py <directory>
```

Example:

```bash
python main.py ./test_files
```

---

## Generate a JSON report

```bash
python main.py <directory> --report report.json
```

Example:

```bash
python main.py ./test_files --report report.json
```

---

## Example Output

```text
Scanning directory: ./test_files

Files found: 10
Duplicate groups found: 2

Duplicate Group 1
-----------------
Size: 1024 bytes
Files:
  test_files/file1.txt
  test_files/file2.txt

Duplicate Group 2
-----------------
Size: 2048 bytes
Files:
  test_files/data1.bin
  test_files/data2.bin

Report saved to: report.json
```

> The exact output depends on the files present in the scanned directory.

---

# 🧪 Running Tests

The project uses `pytest`.

Run:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

The test suite currently covers core hashing and duplicate-detection behavior.

---

# 🧪 Test Cases

Current tests include:

* Identical files produce the same hash
* Different files produce different hashes
* Identical files are detected as duplicates
* Different files are not incorrectly classified as duplicates

Additional edge-case testing is planned as the project evolves.

---

# ⚡ Performance Considerations

The duplicate detection process avoids hashing every file unnecessarily.

### Without size filtering

```text
Every file
    ↓
SHA-256
    ↓
Compare hashes
```

### Current approach

```text
Every file
    ↓
Check file size
    ↓
Files with unique sizes → ignored
    ↓
Potential candidates
    ↓
SHA-256
    ↓
Compare hashes
```

This reduces the number of expensive hashing operations when a directory contains many files with unique sizes.

---

# 🧠 Complexity

Let:

* `N` = number of files
* `B` = total number of bytes processed during hashing

### Directory scanning

Approximately:

```text
O(N)
```

### Hashing

Hashing is proportional to the amount of file data processed:

```text
O(B)
```

### Duplicate grouping

Hash-based grouping is approximately:

```text
O(N)
```

Overall performance is dominated by filesystem access and the amount of data that must be hashed.

---

# 🛡️ Error Handling

The application handles invalid input paths and avoids treating invalid directories as valid scan targets.

Potential filesystem errors are handled so that the application can provide meaningful feedback rather than failing silently.

---

# 🔮 Future Improvements

Planned improvements include:

* [ ] Integrity verification against a saved baseline
* [ ] Detection of modified, added, and deleted files
* [ ] Multiple hashing algorithms
* [ ] Partial hashing for faster duplicate detection
* [ ] Parallel file hashing
* [ ] Improved filesystem error handling
* [ ] Symbolic-link handling
* [ ] Expanded test coverage
* [ ] Code coverage reporting
* [ ] Type checking
* [ ] Structured logging
* [ ] GitHub Actions CI
* [ ] Performance benchmarks
* [ ] Interactive terminal interface
* [ ] Optional web dashboard
* [ ] Safe duplicate cleanup with dry-run mode

---

# 📌 Use Cases

This tool can be useful for:

* Finding duplicate documents
* Cleaning redundant backups
* Detecting repeated media files
* Identifying redundant datasets
* Auditing large directories
* Reducing unnecessary storage usage
* Building a foundation for file-integrity monitoring systems

---

# 🎯 Learning Objectives

This project demonstrates practical knowledge of:

* Python file handling
* Recursive filesystem traversal
* Hash functions
* SHA-256
* Memory-efficient file processing
* Algorithmic optimization
* Data structures
* Exception handling
* Command-line interfaces
* JSON serialization
* Unit testing
* Git and GitHub
* Modular software design

---

# 👨‍💻 Author

**Rahul Dasari**

GitHub:

https://github.com/ce23b006-byte

Project:

https://github.com/ce23b006-byte/file-integrity-duplicate-detector

---

# 📄 License

This project is currently available for educational and portfolio purposes.

A formal open-source license can be added in a future release.

---

## ⭐ Project Status

**Current Status:** Functional

The core duplicate-detection pipeline is implemented and tested.

Future versions will focus on performance optimization, stronger filesystem error handling, integrity monitoring, expanded automated testing, and CI/CD.
