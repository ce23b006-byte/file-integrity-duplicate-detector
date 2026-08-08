from src.duplicate_finder import find_duplicates


def test_duplicate_files_are_detected(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("Duplicate content")
    file2.write_text("Duplicate content")

    duplicates = find_duplicates([file1, file2])

    assert len(duplicates) == 1
    assert len(next(iter(duplicates.values()))) == 2


def test_different_files_are_not_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("Content A")
    file2.write_text("Content B")

    duplicates = find_duplicates([file1, file2])

    assert len(duplicates) == 0