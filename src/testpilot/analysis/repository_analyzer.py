from testpilot.github.github_client import (
    get_python_files,
    get_file_content
)

from testpilot.analysis.code_analyzer import analyze_code


def analyze_repository(owner, repo):

    files = get_python_files(owner, repo)

    repository_analysis = {}

    for file in files:

        file_path = file["path"]

        try:
            code = get_file_content(owner, repo, file_path)

            analysis = analyze_code(code)

            repository_analysis[file_path] = analysis

        except Exception as e:
            repository_analysis[file_path] = {
                "error": str(e)
            }

    return repository_analysis