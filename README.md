# TestPilot AI 🤖

### AI-Powered Autonomous Software Testing Agent

TestPilot AI is an AI-powered software testing platform designed to automate the testing process of Python repositories using Large Language Models (LLMs).

The system aims to analyze source code, generate pytest test cases, execute tests, identify failures, and provide intelligent suggestions for potential fixes.

🚧 **Project Status: Under Development**

## Features

- **GitHub Integration:** Connect to GitHub repositories and retrieve source code.
- **Repository Analysis:** Discover and analyze Python files.
- **Code Analysis:** Examine Python source code to identify functions and relevant code structures.
- **AI-Powered Test Generation:** Generate pytest test cases using Google Gemini.
- **Automated Test Execution:** Execute generated tests using pytest.
- **Failure Analysis:** Identify and summarize test execution failures.
- **Intelligent Fix Suggestions:** Recommend potential solutions for common errors.
- **Test Reporting:** Generate reports containing execution results and failure information.

*Features are being implemented and integrated incrementally.*

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| LLM Integration | Google Gemini API |
| Repository Integration | GitHub REST API |
| Testing Framework | Pytest |
| API Communication | Requests |
| Configuration Management | Python-dotenv |
| Data Validation | Pydantic |
| Frontend (Planned) | Streamlit |
| Containerization (Planned) | Docker |

## Project Architecture

```text
TestPilot-AI/
│
├── src/
│   └── testpilot/
│       ├── agents/
│       ├── analysis/
│       ├── api/
│       ├── execution/
│       ├── fixes/
│       ├── generation/
│       ├── github/
│       └── storage/
│
├── tests/
├── docs/
├── ui/
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/TestPilot-AI.git
cd TestPilot-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```powershell
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as a reference.

Add your credentials:

```env
GEMINI_API_KEY=your_gemini_api_key
GITHUB_TOKEN=your_github_token
```

Never commit your `.env` file or expose API credentials publicly.

### 5. Run Tests

```bash
pytest -v
```

## Development Roadmap

- [x] Project structure and backend foundation
- [x] GitHub API integration and authentication
- [x] Python repository analysis
- [x] Test execution using pytest
- [x] Test failure analysis
- [x] Basic fix suggestion engine
- [x] Test report generation
- [x] Initial unit testing
- [ ] Stable Gemini API integration
- [ ] LLM-powered test generation
- [ ] End-to-end workflow integration
- [ ] Agentic orchestration
- [ ] Interactive frontend
- [ ] Docker integration
- [ ] End-to-end validation

## Testing

The project currently has **21 passing unit tests** covering the implemented backend modules.

```bash
pytest -v
```

## Project Vision

The ultimate goal of TestPilot AI is to create an autonomous testing assistant that can understand Python repositories, intelligently generate and execute tests, diagnose failures, and provide actionable recommendations with minimal manual intervention.

---

**Developed as an AI Engineering project.**