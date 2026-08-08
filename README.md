# File Integrity & Duplicate Detection System

A Python-based command-line tool for detecting duplicate files and monitoring file integrity using SHA-256 hashing.

The system recursively scans directories, identifies duplicate files, calculates wasted storage, creates integrity baselines, and detects modified, new, or missing files.

---

## 🚀 Features

- 🔍 Recursive directory scanning
- ⚡ File-size filtering before hashing
- 🔐 SHA-256 hashing
- 💾 Chunk-based hashing for large files
- 🧩 Duplicate file detection
- 💽 Wasted storage calculation
- 📊 JSON duplicate reports
- 🛡️ Integrity baseline creation
- ✏️ Modified file detection
- ➕ New file detection
- ❌ Missing file detection
- 💻 Command-line interface
- 🧪 Automated pytest tests
- 🧱 Modular project structure

---

## 🛠️ Tech Stack

- **Language:** Python
- **Hashing:** SHA-256
- **Testing:** pytest
- **Version Control:** Git
- **Platform:** Windows / Linux / macOS

---

## 📂 Project Structure

```text
file-integrity-duplicate-detector/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── scanner.py
│   ├── hasher.py
│   ├── duplicate_finder.py
│   ├── integrity.py
│   └── reporter.py
│
├── tests/
│   ├── test_hasher.py
│   ├── test_duplicate_finder.py
│   └── test_integrity.py
│
└── test_files/
    ├── file1.txt
    └── file2.txt