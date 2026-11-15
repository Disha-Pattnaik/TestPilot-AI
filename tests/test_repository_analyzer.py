from testpilot.analysis.repository_analyzer import analyze_repository


def test_analyze_repository(monkeypatch):

    mock_files = [
        {
            "name": "main.py",
            "path": "main.py",
            "type": "file"
        },
        {
            "name": "utils.py",
            "path": "utils.py",
            "type": "file"
        }
    ]

    mock_code = {
        "main.py": "def add(a, b): return a + b",
        "utils.py": "def subtract(a, b): return a - b"
    }

    def mock_get_python_files(owner, repo):
        return mock_files

    def mock_get_file_content(owner, repo, path):
        return mock_code[path]

    def mock_analyze_code(code):
        return {"status": "analyzed"}

    monkeypatch.setattr(
        "testpilot.analysis.repository_analyzer.get_python_files",
        mock_get_python_files
    )

    monkeypatch.setattr(
        "testpilot.analysis.repository_analyzer.get_file_content",
        mock_get_file_content
    )

    monkeypatch.setattr(
        "testpilot.analysis.repository_analyzer.analyze_code",
        mock_analyze_code
    )

    result = analyze_repository("test_owner", "test_repo")

    assert isinstance(result, dict)
    assert len(result) == 2
    assert all(
        analysis == {"status": "analyzed"}
        for analysis in result.values()
    )