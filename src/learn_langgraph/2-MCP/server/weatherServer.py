from mcp.server.fastmcp import FastMCP
from langchain_tavily import TavilySearch # web search
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


tavilyTool = TavilySearch(max_results=2) #tavily object 
# Read MCP_GUIDE.md in src/resources...


mcp = FastMCP("weather")

@mcp.tool()
def get_weather(location: str) -> dict:
    """Search for current weather information for a location."""
    return tavilyTool.invoke(
        f"Current weather in {location}: temperature, conditions, and observation time"
    )

# We run this server  python ../server/weatherServer.py and then use the client
if __name__ == "__main__":
    mcp.run(transport='streamable-http') #We will see with streamable-http Uvicorn running on http://localhost:8000/mcp 