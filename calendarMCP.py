from mcp.server.fastmcp import FastMCP
import logging

from models.ListEventParameters import ListEventsParameters
from models.CalendarEvent import CalendarEvent
from models.UpdateCalendarEvent import UpdateCalendarEvent
from services.events import delete_calendar_event, list_calendar_events, insert_calendar_event, update_calendar_event

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
    Inserts an event in the calendar.
    
    Args:
        event: An EventModel type which contains the parameters for the request.  
        calendarId: Id of the calendar.
    Returns:
        A string mentioningEvent is created in the calendar .
    """
    try:
        return insert_calendar_event(event, calendarId)
    except Exception as e:
        logging.error(f"Failed to insert calendar event: {e}")
        return "Failed to Insert Event"

@mcp.tool("delete-event")
def delete_event(eventId, calendarId: str="primary"):
    """
    Cancel or Delete any event from Calendar.
    
    Args:
        eventId: Id of the event to be deleted.
        calendarId: Id of the calendar.
    Returns:
        A string mentioning Event is deleted in the calendar.
    """
    try:
        return delete_calendar_event(eventId, calendarId)
    except Exception as e:
        logging.error(f"Failed to delete calendar event: {e}")        
        return "Failed to delete event"

@mcp.tool("update-event")
def update_event(event: UpdateCalendarEvent, eventId, calendarId: str="primary"): 
    """
    Updates the event of the Calendar.
    
    Args:
        event: An EventModel type which contains the parameters for the request.
        eventId: Id of the event to be updated.
        calendarId: Id of the calendar.
    Returns:
        A string mentioning Event is updated in the calendar.
    """
    try:
        return update_calendar_event(event, eventId, calendarId)
    except Exception as e:
        logging.error(f"Failed to update calendar event: {e}")
        return "Failed to update event"


if __name__ == '__main__':
    mcp.run(transport='stdio')