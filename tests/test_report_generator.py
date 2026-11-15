from testpilot.execution.report_generator import generate_report


def test_generate_success_report():

    result = generate_report({
        "success": True,
        "return_code": 0,
        "output": "5 passed",
        "errors": ""
    })

    assert result["status"] == "PASSED"
    assert result["success"] is True
    assert result["project"] == "TestPilot AI"


def test_generate_failure_report():

    result = generate_report({
        "success": False,
        "return_code": 1,
        "output": "1 failed",
        "errors": "AssertionError"
    })

    assert result["status"] == "FAILED"
    assert result["success"] is False
    assert result["errors"] == "AssertionError"