from testpilot.analysis.code_analyzer import analyze_code


def test_analyze_code():

    source_code = """
import os

class Calculator:

    def add(self, a, b):
        return a + b

def subtract(a, b):
    return a - b
"""

    result = analyze_code(source_code)

    assert "add" in result["functions"]
    assert "subtract" in result["functions"]
    assert "Calculator" in result["classes"]
    assert "os" in result["imports"]
    assert result["total_lines"] > 0