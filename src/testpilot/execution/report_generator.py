from datetime import datetime


def generate_report(test_result):

    output = test_result.get("output", "")

    return {
        "project": "TestPilot AI",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "success": test_result["success"],
        "return_code": test_result["return_code"],
        "test_output": output,
        "errors": test_result.get("errors", ""),
        "status": "PASSED" if test_result["success"] else "FAILED"
    }