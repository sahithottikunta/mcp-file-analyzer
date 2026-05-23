# file_analyzer.py
from mcp.server.fastmcp import FastMCP
import os

# Initialize our unified master server
mcp = FastMCP("master-file-analyzer")

# =====================================================================
#  SECTION 1: TOOLS (AI Actions - What the AI can DO)
# =====================================================================

@mcp.tool()
def list_directory(path: str) -> list[str]:
    """List all file and folder names inside a specific directory path."""
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Error listing directory: {str(e)}"]

@mcp.tool()
def read_file(path: str) -> str:
    """Read the complete text contents of a file from an absolute path."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File not found at {path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"

@mcp.tool()
def count_lines(path: str) -> int:
    """Count the total number of lines inside a file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except Exception:
        return -1

@mcp.tool()
def get_api_status() -> dict:
    """Check the current API performance metrics."""
    return {
        "status": "operational",
        "uptime_percent": 99.99,
        "response_time_ms": 45
    }

# =====================================================================
# SECTION 2: RESOURCES (AI Read-Only Data - What the AI can READ)
# =====================================================================

@mcp.resource("doc://api/overview")
def api_overview() -> str:
    """API overview and getting started guide."""
    return """# API Overview
This workspace analysis engine provides tools for system directory lookups, deep file reads, and processing metrics.
"""

@mcp.resource("doc://api/endpoints")
def api_endpoints() -> str:
    """Complete list of available capability endpoints."""
    return """# API Endpoints
- Tool: list_directory
- Tool: read_file
- Tool: count_lines
- Tool: get_api_status
"""

# =====================================================================
# SECTION 3: PROMPTS (AI Templates - How the AI should BEHAVE)
# =====================================================================

@mcp.prompt()
def code_review_prompt(language: str = "python") -> str:
    """Template for reviewing local files written in a specific language."""
    return f"""You are an expert {language} senior engineer.
Analyze the local code provided to you by the tools and provide feedback on:
1. Structural correctness and logic flows
2. Edge cases and overall robustness
3. Performance constraints and syntax optimization
"""

@mcp.prompt()
def security_audit_prompt() -> str:
    """Template for auditing local workspace files for data safety issues."""
    return """Conduct a rigorous local code security audit. Check for:
1. Insecure file read/write logic paths
2. Exposed credentials, hardcoded keys, or sensitive environmental data
3. Vulnerabilities to system command injections
"""

if __name__ == "__main__":
    mcp.run()
