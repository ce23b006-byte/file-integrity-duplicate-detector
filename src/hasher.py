import hashlib
from pathlib import Path


def calculate_hash(file_path, chunk_size=1024 * 1024):
    """
    Calculate the SHA-256 hash of a file.

    The file is processed in chunks so that large files
    do not need to be loaded completely into memory.
    """

    sha256 = hashlib.sha256()

    try:
        with Path(file_path).open("rb") as file:
            while chunk := file.read(chunk_size):
                sha256.update(chunk)

        return sha256.hexdigest()

    except (OSError, PermissionError) as error:
        raise RuntimeError(
            f"Unable to read file '{file_path}': {error}"
        ) from error