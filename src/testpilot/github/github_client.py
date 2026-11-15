import requests
import base64
import os

from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

GITHUB_API_URL = "https://api.github.com"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}


def get_repository(owner, repo):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def get_repository_contents(owner, repo, path=""):

    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/contents"

    if path:
        url += "/" + quote(path, safe="/")

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def get_python_files(owner, repo):

    python_files = []

    def scan_directory(path=""):

        contents = get_repository_contents(owner, repo, path)

        for item in contents:

            if item["type"] == "file" and item["name"].endswith(".py"):
                python_files.append(item)

            elif item["type"] == "dir":
                scan_directory(item["path"])

    scan_directory()

    return python_files


def get_file_content(owner, repo, path):

    encoded_path = quote(path, safe="/")

    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/contents/{encoded_path}"

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    file_data = response.json()

    decoded_content = base64.b64decode(file_data["content"])

    return decoded_content.decode("utf-8")