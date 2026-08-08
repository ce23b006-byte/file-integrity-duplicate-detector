from src.hasher import calculate_hash


def test_identical_files_have_same_hash(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("Hello duplicate detection!")
    file2.write_text("Hello duplicate detection!")

    assert calculate_hash(file1) == calculate_hash(file2)


def test_different_files_have_different_hash(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("File A")
    file2.write_text("File B")

    assert calculate_hash(file1) != calculate_hash(file2)