from models.ListEventParameters import ListEventsParameters
from models.CalendarEvent import CalendarEvent
from models.UpdateCalendarEvent import UpdateCalendarEvent, EventDateTime
from google_calendar_connection import GoogleCalendarService

from utils.serializeData import serialize_event_datetime

from typing import List
import logging, json

def list_calendar_events(parameters: ListEventsParameters):
    calendar_service = GoogleCalendarService().get_service()
    
    try:
        params = parameters.model_dump(exclude_none=True)
        
        events_result = calendar_service.events().list(**params)
        return events_result.execute().get('items', [])
    except Exception as e:
        logging.error(f"Failed to fetch calendar events: {e}")
        return f"Failed to fetch calendar events: {e}"
    
def get_calendar_event(eventId, calendarId: str):
    calendar_service = GoogleCalendarService().get_service()
    
    try:
        event = calendar_service.events().get(calendarId=calendarId, eventId=eventId).execute()
        return event
    except Exception as e:
        logging.error(f"Failed to get calendar event: {e}")
        return f"Failed to get event: {e}"
    
def insert_calendar_event(parameters: CalendarEvent, calendarId: str):
    calendar_service = GoogleCalendarService().get_service()
    
    try:
        event_body = parameters.model_dump(exclude_none=True)
        
        # Serialize EventDateTime objects
        if 'start' in event_body and event_body['start']:
            event_body['start'] = serialize_event_datetime(parameters.start)
        if 'end' in event_body and event_body['end']:
            event_body['end'] = serialize_event_datetime(parameters.end)
        if 'originalStartTime' in event_body and event_body['originalStartTime']:
            event_body['originalStartTime'] = serialize_event_datetime(parameters.originalStartTime)
        
        event = calendar_service.events().insert(calendarId=calendarId, body=event_body).execute()
        return 'Event created: %s' % (event.get('htmlLink'))
    except Exception as e:
        logging.error(f"Failed to insert calendar event: {e}")
        return f"Failed to Insert Event: {e}"
    
def delete_calendar_event(eventId, calendarId: str):
    calendar_service = GoogleCalendarService().get_service()
    
    try:
        calendar_service.events().delete(calendarId=calendarId, eventId=eventId).execute()
        return 'Event deleted.'
    except Exception as e:
        logging.error(f"Failed to delete calendar event: {e}")
        return f"Failed to delete event: {e}"
    
def update_calendar_event(parameters: UpdateCalendarEvent , eventId, calendarId: str):
    calendar_service = GoogleCalendarService().get_service()
    
    try:
        event_body = parameters.model_dump(exclude_none=True)

        # Serialize EventDateTime objects
        if 'start' in event_body and event_body['start'] and isinstance(parameters.start, EventDateTime):
            event_body['start'] = serialize_event_datetime(parameters.start)
        if 'end' in event_body and event_body['end'] and isinstance(parameters.end, EventDateTime):
            event_body['end'] = serialize_event_datetime(parameters.end)
        if 'originalStartTime' in event_body and event_body['originalStartTime'] and isinstance(parameters.originalStartTime, EventDateTime):
            event_body['originalStartTime'] = serialize_event_datetime(parameters.originalStartTime)

        updated_event = calendar_service.events().update(calendarId=calendarId, eventId=eventId, body=event_body).execute()
        return 'Event updated: %s' % (updated_event.get('htmlLink'))
    except Exception as e:
        logging.error(f"Failed to update calendar event: {e}")
        return f"Failed to update event: {e}"