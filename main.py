from blender_mcp.server import main as server_main
import sys

def main():
    """Entry point for the blender-mcp package"""
    # Print a quick startup message so I know the server is actually running
    print("Starting Blender MCP server...", file=sys.stderr)
    server_main()

if __name__ == "__main__":
    main()
