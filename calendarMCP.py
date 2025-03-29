from mcp.server.fastmcp import FastMCP
import logging

from models.ListEventParameters import ListEventsParameters
from services.events import list_calendar_events

mcp = FastMCP("google-calendar")

# Events API
@mcp.tool("list-events")
def list_events(listEventParameters: ListEventsParameters = ListEventsParameters()):
    """
    Gives the list of events from the primary calendar
    
    Args:
        listEventParameters: A ListEventParameters type which contains the parameters for the request.
    Returns:
        A list of events
    """
    try:
        return list_calendar_events(listEventParameters)
    except Exception as e:
        logging.error(f"Failed to fetch calendar events: {e}")
        return []

# @mcp.tool("insert-event")
# def insert_event():
#     """
#     Inserts a event in the calendar
#     """
#     pass

# @mcp.tool("delete-event")
# def delete_event():
#     pass

# @mcp.tool("update-event")
# def update_event(): 
#     pass


if __name__ == '__main__':
    mcp.run(transport='stdio')