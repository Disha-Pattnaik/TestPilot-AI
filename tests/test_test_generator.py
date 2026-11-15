from testpilot.generation.test_generator import generate_test_prompt


def test_generate_test_prompt():

    source_code = """
def add(a, b):
    return a + b
"""

    analysis = {
        "functions": ["add"],
        "classes": [],
        "imports": [],
        "total_lines": 3
    }

    result = generate_test_prompt(source_code, analysis)

    assert isinstance(result, str)
    assert "pytest" in result
    assert "add" in result
    assert "edge cases" in result