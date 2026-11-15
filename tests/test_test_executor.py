from testpilot.execution.test_executor import run_tests


def test_run_tests_success(tmp_path):

    test_file = tmp_path / "test_sample.py"

    test_file.write_text(
        "def test_sample():\n"
        "    assert 2 + 2 == 4\n"
    )

    result = run_tests(str(test_file))

    assert result["success"] is True
    assert result["return_code"] == 0


def test_run_tests_failure(tmp_path):

    test_file = tmp_path / "test_sample.py"

    test_file.write_text(
        "def test_sample():\n"
        "    assert 2 + 2 == 5\n"
    )

    result = run_tests(str(test_file))

    assert result["success"] is False
    assert result["return_code"] != 0