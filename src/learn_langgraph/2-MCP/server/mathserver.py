from mcp.server.fastmcp import FastMCP

# Read MCP_GUIDE.md in src/resources...


mcp = FastMCP("math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """__summary__
    Add two numbers
    """
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Multiply 2 numbers"""
    return a - b


#transport = stdio normally means the host/langraph starts a local server process and communicates over its standard input/output. 
# It basically means this server does not have to be hosted, and it can share its input and output locally to the mcp client that
# sits in front of the agent
if __name__ == "__main__":
    mcp.run(transport='stdio') 