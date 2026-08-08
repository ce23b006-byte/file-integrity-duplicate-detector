from collections import defaultdict
from pathlib import Path

from .hasher import calculate_hash


def group_files_by_size(files):
    """
    Group files by their size.

    Files with different sizes cannot be identical,
    so this avoids unnecessary hashing.
    """

    size_groups = defaultdict(list)

    for file in files:
        try:
            size = Path(file).stat().st_size
            size_groups[size].append(Path(file))

        except (OSError, PermissionError):
            continue

    return size_groups


def find_duplicates(files):
    """
    Find duplicate files using file size and SHA-256 hash.

    Returns:
        Dictionary where each key is a SHA-256 hash and
        the value is a list of files having that hash.
    """

    size_groups = group_files_by_size(files)

    duplicates = defaultdict(list)

    for size, candidates in size_groups.items():

        # A single file of a particular size cannot have
        # a duplicate within this group.
        if len(candidates) < 2:
            continue

        for file in candidates:

            try:
                file_hash = calculate_hash(file)
                duplicates[file_hash].append(file)

            except RuntimeError:
                continue

    # Keep only groups containing 2 or more files.
    return {
        file_hash: matching_files
        for file_hash, matching_files in duplicates.items()
        if len(matching_files) > 1
    }