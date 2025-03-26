from mcp.server.fastmcp import FastMCP

mcp = FastMCP("google-calendar")

@mcp.tool("list-events")
def list_events():
    pass

@mcp.tool("insert-event")
def insert_event():
    pass

@mcp.tool("delete-event")
def delete_event():
    pass

@mcp.tool("update-event")
def update_event(): 
    pass


if __name__ == '__main__':
    mcp.run(transport='stdio')