def generate_test_prompt(source_code, analysis):

    prompt = f"""
You are an expert Python software tester.

Your task is to generate pytest test cases
for the following Python source code.

SOURCE CODE:
{source_code}

CODE ANALYSIS:
{analysis}

Instructions:
1. Identify all functions and classes.
2. Generate meaningful pytest test cases.
3. Include normal and edge cases.
4. Check expected outputs.
5. Return only executable Python test code.
"""

    return prompt