# file_analyzer.py
from mcp.server.fastmcp import FastMCP
import os

# Initialize our new file analyzer server
mcp = FastMCP("file-analyzer")

@mcp.tool()
def list_directory(path: str) -> list[str]:
    """
    List all file and folder names inside a specific directory path.
    """
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Error listing directory: {str(e)}"]

@mcp.tool()
def read_file(path: str) -> str:
    """
    Read the complete text contents of a file from an absolute path.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File not found at {path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"

@mcp.tool()
def count_lines(path: str) -> int:
    """
    Count the total number of lines inside a file. Returns -1 if an error occurs.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except Exception:
        return -1

if __name__ == "__main__":
    mcp.run()