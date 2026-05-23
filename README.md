Markdown
# 🧮 Ultimate Master File Analyzer & Docs MCP Server

A comprehensive, all-in-one Model Context Protocol (MCP) server built with Python using the `FastMCP` framework. This server establishes a unified architecture combining actionable agent tools, context-driven read-only data resources, and instructional system prompt templates over standard input/output (`stdio`) channels.

---

## 🚀 Unified Server Features

### 1. 🛠️ AI Tools (Actions)
- **`list_directory(path: str)`**: Lists all file and folder names inside a specified directory path.
- **`read_file(path: str)`**: Reads and extracts the complete text content of a local text file.
- **`count_lines(path: str)`**: Scans a target file and counts its total number of lines.
- **`get_api_status()`**: Returns a real-time dictionary payload detailing systemic uptime metrics.

### 2. 📂 AI Resources (Read-Only Data Context)
- **`doc://api/overview`**: An entry-point markdown document detailing the architecture of the file analyzer engine.
- **`doc://api/endpoints`**: A dynamic mapping dictionary indexing all operational tool routes.

### 3. 💬 AI Prompts (Persona Templates)
- **`code_review_prompt(language)`**: Configures connected LLM agents into elite senior engineering personas tailored for scanning files.
- **`security_audit_prompt()`**: Imbues language models with strict security parameters to audit paths for credential leaks or injection risks.

---

## ⚙️ Local Installation & Environment Setup

### 1. Prerequisites
- **Python 3.10+**
- **Node.js & npm** (Required to run the visual testing harness)

### 2. Workspace Sandbox Isolation
Clone this project, launch VS Code inside the project directory, and initialize a local virtual environment:

```bash
# Create your local virtual environment sandbox folder
python -m venv .venv

# Activate the sandbox (Windows PowerShell)
.venv\Scripts\activate

# Activate the sandbox (Mac/Linux)
source .venv/bin/activate
3. Install Dependencies
Install the required Model Context Protocol core platform SDK and its developer dependencies:

Bash
pip install "mcp[cli]"
🔬 Local Inspection & Visual Testing
Because MCP servers utilize specialized text streams to interact directly with large language models, standard python execution scripts will sit idle in the terminal. Instead, boot up the official visual validation suite:

Bash
npx @modelcontextprotocol/inspector python file_analyzer.py
Dashboard Settings Configuration:
Once the testing engine loads in your web browser, match the parameter inputs inside the left panel configuration rail:

Transport Type: STDIO

Command: python

Arguments: file_analyzer.py

Click Connect to load up the interactive playground where you can test your tools, read your markdown resource data feeds, and test out prompt personas!


---

### Step 2: Push the Final Documentation to GitHub

Now that your README is completely finished, run this quick final sequence in your active terminal to push your changes up to GitHub:

```bash
git add README.md
git commit -m "docs: finalize master readme documenting tools, resources, and prompts"
git push