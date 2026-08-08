# File Integrity & Duplicate Detection System

A Python-based command-line tool that recursively scans directories and detects duplicate files using SHA-256 hashing.

## Features

- Recursive directory scanning
- SHA-256 file hashing
- File-size based pre-filtering
- Duplicate file detection
- Chunk-based file processing
- JSON report generation
- Command-line interface
- Exception handling
- Automated unit testing

## How It Works

The application uses a multi-stage approach:

```text
Directory
    |
    v
Scan all files
    |
    v
Group files by size
    |
    v
Hash files with matching sizes
    |
    v
Compare SHA-256 hashes
    |
    v
Group duplicate files
    |
    v
Generate JSON report
```

## Why File Size Is Checked First

Two files with different sizes cannot be identical.

Therefore, the application first groups files by size and only calculates SHA-256 hashes for files that have the same size.

This reduces unnecessary file reading and hashing.

## Project Structure

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
├── reports/
│
├── test_files/
│   ├── file1.txt
│   └── file2.txt
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Technologies

- Python
- hashlib
- pathlib
- argparse
- JSON
- pytest
- Git
- GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/file-integrity-duplicate-detector.git
```

Navigate to the project:

```bash
cd file-integrity-duplicate-detector
```

Install the dependencies:

```bash
py -m pip install -r requirements.txt
```

## Usage

Run the application by providing a directory:

```bash
py main.py <directory>
```

Example:

```bash
py main.py test_files
```

You can also specify a custom report location:

```bash
py main.py test_files --report reports/my_report.json
```

## Example Output

```text
File Integrity & Duplicate Detection System
==================================================
Scanning: test_files
Files found: 2
Duplicate groups found: 1

Duplicate files:

SHA-256: 40312749b611791d45e8dc3fb4627b0d3ba1daf5204ffb0d384398aac0174584
  └── test_files\file1.txt
  └── test_files\file2.txt

Report saved to: reports\report.json
```

## Testing

Run the automated tests:

```bash
py -m pytest
```

Current test result:

```text
4 passed
```

The test suite verifies:

- Identical files produce the same SHA-256 hash
- Different files produce different hashes
- Duplicate files are detected
- Different files are not incorrectly classified as duplicates

## Design Considerations

### Memory Efficiency

Files are processed in chunks instead of loading the entire file into memory.

This allows the application to process large files more efficiently.

### Duplicate Detection

Files are considered duplicates when they have the same file size and SHA-256 hash.

### Error Handling

The application handles common filesystem errors such as:

- Missing directories
- Invalid directory paths
- Permission errors
- File access errors

## Future Improvements

- Multithreaded hashing
- SQLite scan history
- GUI dashboard
- Progress bar
- Safe duplicate-file deletion
- CSV reports
- File integrity monitoring
- Performance benchmarking

## Author

Your Name

GitHub: https://github.com/YOUR_USERNAME