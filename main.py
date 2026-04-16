from blender_mcp.server import main as server_main
import sys

def main():
    """Entry point for the blender-mcp package"""
    # Print a quick startup message so I know the server is actually running
    print("Starting Blender MCP server...", file=sys.stderr)
    print("Press Ctrl+C to stop the server.", file=sys.stderr)
    try:
        server_main()
    except KeyboardInterrupt:
        print("\nServer stopped.", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        # helpful to see the actual error instead of a silent crash
        import traceback
        print(f"Server crashed: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
