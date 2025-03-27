from mcp.server.fastmcp import FastMCP

from models import ListEventParameters

mcp = FastMCP("google-calendar")

# Events API
@mcp.tool("list-events")
def list_events(listEventParameters: ListEventParameters):
    """
    Gives the list of events from the primary calendar
    
    Args:
        listEventParameters: A ListEventParameters type which contains the parameters for the request.
    Returns:
        A list of events
    """
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