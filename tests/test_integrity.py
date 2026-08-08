from pathlib import Path

from src.integrity import create_baseline, verify_integrity


def test_create_and_verify_baseline(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("hello")
    file2.write_text("world")

    files = [file1, file2]

    baseline = tmp_path / "baseline.json"

    create_baseline(files, baseline)

    result = verify_integrity(files, baseline)

    assert len(result["unchanged"]) == 2
    assert len(result["modified"]) == 0
    assert len(result["new"]) == 0
    assert len(result["missing"]) == 0


def test_detect_modified_file(tmp_path):
    file1 = tmp_path / "file1.txt"

    file1.write_text("original")

    baseline = tmp_path / "baseline.json"

    create_baseline([file1], baseline)

    file1.write_text("modified")

    result = verify_integrity([file1], baseline)

    assert len(result["modified"]) == 1
    assert str(file1) in result["modified"]


def test_detect_new_file(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("original")

    baseline = tmp_path / "baseline.json"

    create_baseline([file1], baseline)

    file2.write_text("new file")

    result = verify_integrity([file1, file2], baseline)

    assert len(result["new"]) == 1
    assert str(file2) in result["new"]


def test_detect_missing_file(tmp_path):
    file1 = tmp_path / "file1.txt"

    file1.write_text("original")

    baseline = tmp_path / "baseline.json"

    create_baseline([file1], baseline)

    file1.unlink()

    result = verify_integrity([], baseline)

    assert len(result["missing"]) == 1
    assert str(file1) in result["missing"]