from langchain_mcp_adapters.client import MultiServerMCPClient #this client can be used for ultiple servers
from langchain.agents import create_agent

import os
import asyncio
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model 
load_dotenv()  # Load environment variables from .env file


async def main():
    client = MultiServerMCPClient (
        {
            "math" : {
                "command" : "python",
                "args" : ["../server/mathserver.py"],
                "transport" : "stdio"
            },

            "weather" : {
                "url" : "http://localhost:8000/mcp",
                "transport" : "streamable-http"
            }
        }
    )

    tools = await client.get_tools()
    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    model = init_chat_model("gpt-4.1") 

    agent = create_agent(model, tools)

    math_respone = await agent.ainvoke ( #aiinvoke is async and invoke is sync
        {"messages" : [{"role" : "user", "content" : "What is tommorow's weather langle bc canada?"}]}
    )
    
    print(math_respone["messages"][-1].content)


asyncio.run(main()) # run async function with asyncio