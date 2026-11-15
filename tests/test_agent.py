from testpilot.agents.test_agent import run_test_agent


def test_agent_waiting_for_test_generation():

    result = run_test_agent(
        source_code="def add(a, b): return a + b",
        analysis="Function performs addition."
    )

    assert result["status"] == "awaiting_test_generation"
    assert "prompt" in result


def test_agent_successful_execution(tmp_path, monkeypatch):

    import testpilot.agents.test_agent as agent

    monkeypatch.setattr(
        agent,
        "generate_test_prompt",
        lambda source, analysis: "Generate pytest tests."
    )

    monkeypatch.setattr(
        agent,
        "run_tests",
        lambda path: {
            "success": True,
            "return_code": 0,
            "output": "1 passed",
            "errors": ""
        }
    )

    monkeypatch.setattr(
        agent,
        "analyze_failures",
        lambda result: {
            "has_failures": False,
            "failed_tests": [],
            "summary": "All tests passed."
        }
    )

    monkeypatch.setattr(
        agent,
        "generate_report",
        lambda result: {"status": "PASSED"}
    )

    test_path = tmp_path / "generated_tests" / "test_sample.py"

    result = run_test_agent(
        source_code="def add(a, b): return a + b",
        analysis="Addition function",
        generated_test_code="def test_add(): assert 2 + 2 == 4",
        test_file_path=str(test_path)
    )

    assert result["status"] == "completed"
    assert result["test_result"]["success"] is True
    assert result["failure_analysis"]["has_failures"] is False
    assert result["report"]["status"] == "PASSED"
    assert test_path.exists()

def test_agent_failure_execution(tmp_path, monkeypatch):

    import testpilot.agents.test_agent as agent

    monkeypatch.setattr(
        agent,
        "generate_test_prompt",
        lambda source, analysis: "Generate tests."
    )

    monkeypatch.setattr(
        agent,
        "run_tests",
        lambda path: {
            "success": False,
            "return_code": 1,
            "output": "1 failed",
            "errors": "AssertionError: Expected 5 but got 4"
        }
    )

    monkeypatch.setattr(
        agent,
        "analyze_failures",
        lambda result: {
            "has_failures": True,
            "failed_tests": ["test_add"],
            "summary": "Test execution failed."
        }
    )

    monkeypatch.setattr(
        agent,
        "suggest_fix",
        lambda error: {
            "error": error,
            "suggestion": "Check the expected value."
        }
    )

    monkeypatch.setattr(
        agent,
        "generate_report",
        lambda result: {"status": "FAILED"}
    )

    result = run_test_agent(
        source_code="def add(a, b): return a + b",
        analysis="Addition function",
        generated_test_code="def test_add(): assert 2 + 2 == 5",
        test_file_path=str(tmp_path / "test_sample.py")
    )

    assert result["status"] == "completed"
    assert result["test_result"]["success"] is False
    assert result["failure_analysis"]["has_failures"] is True
    assert len(result["fix_suggestions"]) == 1
    assert result["report"]["status"] == "FAILED"