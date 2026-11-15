from unittest.mock import patch, Mock
import base64

from testpilot.github.github_client import (
    get_repository,
    get_repository_contents,
    get_file_content,
    get_python_files
)


@patch("testpilot.github.github_client.requests.get")
def test_get_repository(mock_get):

    mock_response = Mock()

    mock_response.json.return_value = {
        "name": "Hello-World",
        "owner": {"login": "octocat"}
    }

    mock_get.return_value = mock_response

    result = get_repository("octocat", "Hello-World")

    assert result["name"] == "Hello-World"
    assert result["owner"]["login"] == "octocat"


@patch("testpilot.github.github_client.requests.get")
def test_get_repository_contents(mock_get):

    mock_response = Mock()

    mock_response.json.return_value = [
        {"name": "README", "type": "file"}
    ]

    mock_get.return_value = mock_response

    result = get_repository_contents("octocat", "Hello-World")

    assert isinstance(result, list)
    assert len(result) > 0


@patch("testpilot.github.github_client.requests.get")
def test_get_file_content(mock_get):

    mock_response = Mock()

    content = base64.b64encode(
        b"print('Hello World')"
    ).decode("utf-8")

    mock_response.json.return_value = {
        "content": content
    }

    mock_get.return_value = mock_response

    result = get_file_content(
        "octocat",
        "Hello-World",
        "README"
    )

    assert isinstance(result, str)
    assert "Hello World" in result


@patch("testpilot.github.github_client.get_repository_contents")
def test_get_python_files(mock_contents):

    mock_contents.side_effect = [
        [
            {"name": "main.py", "path": "main.py", "type": "file"},
            {"name": "README.md", "path": "README.md", "type": "file"},
            {"name": "src", "path": "src", "type": "dir"}
        ],
        [
            {"name": "app.py", "path": "src/app.py", "type": "file"}
        ]
    ]

    result = get_python_files("octocat", "Hello-World")

    assert len(result) == 2
    assert result[0]["name"] == "main.py"
    assert result[1]["name"] == "app.py"