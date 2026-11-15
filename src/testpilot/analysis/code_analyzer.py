import ast


def analyze_code(source_code):

    tree = ast.parse(source_code)

    analysis = {
        "functions": [],
        "classes": [],
        "imports": [],
        "total_lines": len(source_code.splitlines())
    }

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            analysis["functions"].append(node.name)

        elif isinstance(node, ast.ClassDef):
            analysis["classes"].append(node.name)

        elif isinstance(node, ast.Import):
            for name in node.names:
                analysis["imports"].append(name.name)

        elif isinstance(node, ast.ImportFrom):
            analysis["imports"].append(node.module)

    return analysis