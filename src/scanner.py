from pathlib import Path


def scan_directory(directory):
    """
    Recursively scan a directory and return all files.
    """

    directory = Path(directory)

    if not directory.exists():
        raise FileNotFoundError(
            f"Directory does not exist: {directory}"
        )

    if not directory.is_dir():
        raise NotADirectoryError(
            f"Not a directory: {directory}"
        )
    excluded_directories = { ".git", ".pytest_cache", "__pycache__", ".venv", "venv", "env", "reports", }

    files = []

    for path in directory.rglob("*"):
        if path.is_file():
            if any(part in excluded_directories for part in path.parts): 
                continue
            files.append(path)

    return files