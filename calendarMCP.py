from mcp.server.fastmcp import FastMCP
import logging

from models.ListEventParameters import ListEventsParameters
from models.CalendarEvent import CalendarEvent
from services.events import list_calendar_events, insert_calendar_event

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

@mcp.tool("insert-event")
def insert_event(event: CalendarEvent, calendarId: str="primary"):
    """
    Inserts an event in the primary calendar.
    
    Args:
        event: An EventModel type which contains the parameters for the request.  
    Returns:
        Event is created in the calendar as string
    """
    try:
        return insert_calendar_event(event, calendarId)
    except Exception as e:
        logging.error(f"Failed to insert calendar event: {e}")
        return "Failed to Insert Event"

# @mcp.tool("delete-event")
# def delete_event():
#     pass

# @mcp.tool("update-event")
# def update_event(): 
#     pass


if __name__ == '__main__':
    mcp.run(transport='stdio')