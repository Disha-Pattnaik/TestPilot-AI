import re


def analyze_failures(test_result):

    if test_result["success"]:
        return {
            "has_failures": False,
            "failed_tests": [],
            "summary": "All tests passed."
        }

    output = (
        test_result.get("output", "")
        + "\n"
        + test_result.get("errors", "")
    )

    failed_tests = re.findall(
        r"^(?:FAILED|ERROR)\s+(.+)$",
        output,
        re.MULTILINE
    )

    return {
        "has_failures": True,
        "failed_tests": failed_tests,
        "summary": "Test execution failed. Check the failure details."
    }