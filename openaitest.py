from openai import OpenAI
from mcp_openai import MCPClient
from mcp_openai import config
import asyncio

from contextlib import asynccontextmanager
import requests


    # This is the default and can be omitted
api_key="xxxx"

mcp_client_config = config.MCPClientConfig(
    mcpServers={
        "calculator": config.MCPServerConfig(
            command="uv",
            args=["run", "testserver.py"],
        )
        # add here other servers ...
    }
)

llm_client_config = config.LLMClientConfig(
    api_key=api_key,
    base_url="https://api.openai.com/v1",
)

llm_request_config = config.LLMRequestConfig(model="gpt-4o")

client = MCPClient(
    mcp_client_config,
    llm_client_config,
    llm_request_config,
)



@asynccontextmanager
async def getclient():
    await client.connect_to_server("calculator")
    try:
        yield client
    finally:
        await client.cleanup()
  

async def execute():
    print("inside main")
    # Establish connection between the client and the server.
  
    # messages_in are coming from user interacting with the LLM
    # e.g. UI making use of this MCP client.
    messages_in = [{"role": "user", "content": "Can you fetch the leads from crm?"}]
    print("printing message", messages_in)


    
    
    messages_out =""
    try:
        async with getclient() as client:
        #await client.connect_to_server("calculator")
            messages_out = await client.process_messages(messages_in)
            print("MCP + OpenAI Response:", messages_out)
    except Exception as e:
        print("Error while processing messages:", e)
    finally:
        print("Gracefully closed MCP client interaction.")



    messages_in = [{"role": "user", "content": "Can you make a call to vijay?"}]
    print("printing message", messages_in)


    
    
    messages_out =""
    try:
        async with getclient() as client:
        #await client.connect_to_server("calculator")
            messages_out = await client.process_messages(messages_in)
            print("MCP + OpenAI Response:", messages_out)
    except Exception as e:
        print("Error while processing messages:", e)
    finally:
        print("Gracefully closed MCP client interaction.")

    return messages_out





    # messages_out contains the LLM response. If required, the LLM make use of
    # the available tools offered by the connected servers.


if __name__ == "__main__":
     asyncio.run(execute())
