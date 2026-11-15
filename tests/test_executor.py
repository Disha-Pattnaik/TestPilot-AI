from testpilot.execution.test_executor import run_tests


def test_execute_tests_success():
    result = run_tests("tests/test_code_analyzer.py")

    assert result["success"] is True
    assert result["return_code"] == 0
    assert "passed" in result["output"]


def test_execute_tests_failure(tmp_path):
    test_file = tmp_path / "test_failure.py"

    test_file.write_text(
        "def test_failure():\n"
        "    assert 2 + 2 == 5\n"
    )

    result = run_tests(str(test_file))

    assert result["success"] is False
    assert result["return_code"] != 0