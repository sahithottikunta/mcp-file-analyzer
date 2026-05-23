Markdown
# 📂 Local File Analyzer MCP Server

An advanced Model Context Protocol (MCP) server built with Python and the `FastMCP` framework. This server grants AI agents the secure ability to inspect local files, parse directories, and run file analysis scripts directly through standard input/output (`stdio`) channels.

## 🛠️ Exposed AI Tools

The server automatically maps python typing configurations and docstrings into valid JSON-RPC tool schemas:

1. **`list_directory(path: str) -> list[str]`**
   - Lists all subdirectories and file names inside a given path.
2. **`read_file(path: str) -> str`**
   - Extracts and streams the complete text content of a specified file.
3. **`count_lines(path: str) -> int`**
   - Scans a target file and calculates its total line metric count.

---

## ⚙️ Project Setup & Installation

### 1. Prerequisites
- **Python 3.10+**
- **Node.js & npm** (Required to run the visual testing harness)

### 2. Environment Configuration
Clone this repository to your workspace, navigate into the root directory, and set up your sandbox environment:

```bash
# Create your local virtual environment isolation block
python -m venv .venv

# Activate the sandbox (Windows PowerShell)
.venv\Scripts\activate

# Activate the sandbox (Mac/Linux)
source .venv/bin/activate
3. Dependency Management
Install the core Model Context Protocol SDK alongside its accompanying developer Command Line Interface:

Bash
pip install "mcp[cli]"
🔬 Interactive Testing Setup
Because an MCP server handles raw data streaming over background protocols, standard Python execution commands will sit idle. Instead, run the official interactive testing interface:

Bash
npx @modelcontextprotocol/inspector python file_analyzer.py
Inspector Panel Configuration:
Once the testing dashboard boots up in your browser window, configure the execution target fields inside the left-hand rail configuration tab:

Transport Type: STDIO

Command: python

Arguments: file_analyzer.py

Click Connect to load up the interactive sandbox blocks where you can execute local file tests!

🚀 Quick Git Instructions to Update GitHub
Once you paste the above code into your README.md and save the file (Ctrl + S), run these quick terminal commands to push the complete document straight up to your repository:

Bash
git add README.md
git commit -m "docs: create complete copy-paste readme template"
git push