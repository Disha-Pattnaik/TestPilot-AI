from pathlib import Path

from testpilot.generation.test_generator import generate_test_prompt
from testpilot.execution.test_executor import run_tests
from testpilot.analysis.failure_analyzer import analyze_failures
from testpilot.fixes.fix_suggester import suggest_fix
from testpilot.execution.report_generator import generate_report


def run_test_agent(
    source_code,
    analysis,
    generated_test_code=None,
    test_file_path="generated_tests/test_generated.py"
):

    # Step 1: Generate test prompt
    prompt = generate_test_prompt(source_code, analysis)

    # Step 2: Wait for AI-generated test code
    if not generated_test_code:
        return {
            "status": "awaiting_test_generation",
            "prompt": prompt
        }

    # Step 3: Save generated test code
    test_file = Path(test_file_path)
    test_file.parent.mkdir(parents=True, exist_ok=True)
    test_file.write_text(generated_test_code, encoding="utf-8")

    # Step 4: Execute generated tests
    test_result = run_tests(str(test_file))

    # Step 5: Analyze failures
    failure_analysis = analyze_failures(test_result)

    # Step 6: Suggest fixes if tests fail
    fix_suggestions = []

    if not test_result["success"]:
        error_details = (
            test_result.get("output", "")
            + "\n"
            + test_result.get("errors", "")
        )

        fix_suggestions.append(suggest_fix(error_details))

    # Step 7: Generate final report
    report = generate_report(test_result)

    return {
        "status": "completed",
        "test_result": test_result,
        "failure_analysis": failure_analysis,
        "fix_suggestions": fix_suggestions,
        "report": report
    }