from testpilot.analysis.failure_analyzer import analyze_failures


def test_analyze_success():

    result = analyze_failures({
        "success": True,
        "output": "2 passed",
        "errors": ""
    })

    assert result["has_failures"] is False
    assert result["failed_tests"] == []


def test_analyze_failure():

    result = analyze_failures({
        "success": False,
        "output": "FAILED tests/test_sample.py::test_login",
        "errors": ""
    })

    assert result["has_failures"] is True
    assert len(result["failed_tests"]) > 0