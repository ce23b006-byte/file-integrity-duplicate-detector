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

    files = []

    for path in directory.rglob("*"):
        if path.is_file():
            files.append(path)

    return files