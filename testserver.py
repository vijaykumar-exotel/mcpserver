# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "mcp",
# ]
# ///
#
# This is a simple calculator server which implements the basic mathematical
# operations: add, subtract, multiply, and divide. It is used for testing the
# implementation of the client.

import asyncio

import mcp.server.stdio
import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
import subprocess
import json


# Initialize the server
server = Server("calculator")




@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available mathematical tools."""
    return [
        types.Tool(
            name="execute_plan",
            description="Execute the order of plan sequence",
            inputSchema={
                "type": "object",
                "properties": {
                    "number": {
                        "type": "number",
                        "description": "Phone number",
                    },
                    "plan_sequence" : {
                        "type" : "string",
                        "description" : "Order of plan execution"

                    }
                },
                "required": ["number","plan_sequence"],
            },
        ),
        types.Tool(
            name="fetch_lead_from_crm",
            description="Fetch lead from CRM",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        types.Tool(
            name="make_call",
            description="Make call to number (num)",
            inputSchema={
                "type": "object",
                "properties": {
                    "number": {
                        "type": "number",
                        "description": "Phone number",
                    }
                },
                "required": ["number"],
            },
        ),
        types.Tool(
            name="send_whatsapp_message",
            description="Send Whatsapp Message  (number)",
            inputSchema={
                "type": "object",
                "properties": {
                    "number": {
                        "type": "number",
                        "description": "Number",
                    },
                    
                },
                "required": ["number"],
            },
        ),
        types.Tool(
            name="greeting",
            description="Greeting myself",
            inputSchema={
                "type": "object",
                "properties": {
                },
                "required": [],
            },
        ),
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle mathematical tool execution requests."""
   

    result = None
    if name == "execute_plan":
        try:
            num = arguments.get("number", "")
            plan_sequence = arguments.get("plan_sequence", "")
        except (TypeError, ValueError):
            return [
            types.TextContent(
                type="text", text="Invalid input. Please provide valid plan sequence."
            )
        ]
        return [types.TextContent(type="text", text=f"{number} and plan is {plan_sequence}")]
    
    elif name == "greeting":
        return [types.TextContent(type="text", text=f"Hi, How can i help you today?")]
    
    elif name == "make_call":
        number = ""
        try:
            number = arguments.get("number", "")
        except (TypeError, ValueError):
            return [
            types.TextContent(
                type="text", text="Invalid input. Please provide valid lead number."
            )
        ]
        url = f"https://399117e47411d9f0f9120de1181323056e55b88c664d2f67:80711a9d4562955dc3591f1ada24790f3b5088dbaa3263db@api.in.exotel.com/v1/Accounts/ameyo5m/Calls/connect.json?From={number}&Url=http://my.in.exotel.com/ameyo5m/exoml/start_voice/24049&CallerId=02247788868"
        headers = {
            'Authorization': 'Basic e3tBdXRoS2V5fX06e3tBdXRoVG9rZW59fQ==',
            'Content-Type' : 'application/json'
        }
        #response = requests.request("POST", url, headers=headers)
        headers = ["-H", "Content-Type: application/json"]
        

        result = subprocess.run(
            ["curl", "-s", "-X", "POST", url] + headers ,
            capture_output=True,
            text=True
        )
        return [types.TextContent(type="text", text=f"call initiated to {number}")]
    
    elif name == "send_whatsapp_message":
        number  = ""
        try:
            num = arguments.get("number", "")
            number = str(num)
            if len(number) == 10:
                number = "91" + number

            phone_vs_whatsapp_pref = {
                "919899028650" : "yes",
                "919845169200" : "yes",
                "917696016726" : "no",
                "917411179773" : "yes"
            }

            if number not in phone_vs_whatsapp_pref:
                return [
                    types.TextContent(
                        type="text", text="The whatsapp messaging is not opted for this number."
                    )
                ]
            if phone_vs_whatsapp_pref[number] == "no":
                return [
                    types.TextContent(
                        type="text", text="The whatsapp messaging is not opted for this number."
                    )
                ]
            number = "+" + number.lstrip("+")
        except (TypeError, ValueError):
            return [
            types.TextContent(
                type="text", text="Invalid input. Please provide valid number."
            )]
        url = "https://399117e47411d9f0f9120de1181323056e55b88c664d2f67:80711a9d4562955dc3591f1ada24790f3b5088dbaa3263db@api.in.exotel.com/v2/accounts/ameyo5m/messages"
        data = {
            "custom_data": "Order12",
            "status_callback": "https://webhook.site",
            "whatsapp": {
                "messages": [
                    {
                        "custom_data": "Order12",
                        "status_callback": "https://webhook.site",
                        "from": "+912247788868",
                        "to": number,
                        "content": {
                            "recipient_type": "individual",
                            "type": "text",
                            "text": {
                                "preview_url": False,
                                "body": "I am Saurabh, your personal assistant, wanted to get in touch with you for an exciting offer. Please let me know if we can talk."
                            }
                        }
                    }
                ]
            }
        }
        
        json_data = json.dumps(data)
        command = [
            "curl",
            "-X", "POST",
            url,
            "-H", "Content-Type: application/json",
            "-d", json_data
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        return [types.TextContent(type="text", text=f"whatsapp message sent to {number}")]


    elif name == "add_name_and_number_to_lead":
        try:
            name = arguments.get("name", "")
            number = arguments.get("number", "")
        except (TypeError, ValueError):
            return [
            types.TextContent(
                type="text", text="Invalid input. Please provide valid lead number and name"
            )
        ]
        return [types.TextContent(type="text", text=f"name:{name},number:{number}")]
   
        
    elif name == "fetch_lead_from_crm":
         return [types.TextContent(type="text", 
         text=f"name:vijay,number:+919899028650|name:vivek,number:+917696016726|name:maru,number:+919845169200|name:saurabh,number:+917411179773")]
    else:
        raise ValueError(f"Unknown tool: {name}")

    return [types.TextContent(type="text", text=f"Result: {result}")]


async def main():
    """Run the server using stdin/stdout streams."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="calculator",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())