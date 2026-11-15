def suggest_fix(error_message):

    if "ModuleNotFoundError" in error_message:
        suggestion = "Check whether the required Python module is installed."

    elif "AssertionError" in error_message:
        suggestion = "Check the expected and actual values in your assertion."

    elif "SyntaxError" in error_message:
        suggestion = "Check your Python syntax, indentation and brackets."

    elif "NameError" in error_message:
        suggestion = "Check whether the variable or function is defined."

    elif "ImportError" in error_message:
        suggestion = "Check your import statements and module paths."

    else:
        suggestion = "Review the error traceback to identify the issue."

    return {
        "error": error_message,
        "suggestion": suggestion
    }