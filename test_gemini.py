from testpilot.api.llm_service import generate_response

prompt = "Explain Python unit testing in 3 sentences."

try:
    response = generate_response(prompt)

    print("\nGEMINI CONNECTION SUCCESSFUL!")
    print("\nGemini Response:")
    print(response)

except Exception as e:
    print("\nGEMINI CONNECTION FAILED!")
    print(e)