import subprocess
import sys


def run_tests(test_path="tests"):

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", test_path, "-v"],
            capture_output=True,
            text=True,
            timeout=120
        )

        return {
            "success": result.returncode == 0,
            "return_code": result.returncode,
            "output": result.stdout,
            "errors": result.stderr
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "return_code": -1,
            "output": "",
            "errors": "Test execution timed out."
        }