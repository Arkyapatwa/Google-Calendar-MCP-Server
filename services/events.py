from models.ListEventParameters import ListEventsParameters
from models.CalendarEvent import CalendarEvent
from google_calendar_connection import GoogleCalendarService

from utils.serializeData import serialize_event_datetime

from typing import List
import logging

def list_calendar_events(parameters: ListEventsParameters):
    calendar_service = GoogleCalendarService().get_service()
    
    try:
        params = parameters.model_dump(exclude_none=True)
        
        events_result = calendar_service.events().list(**params)
        return events_result.execute().get('items', [])
    except Exception as e:
        logging.error(f"Failed to fetch calendar events: {e}")
        return []
    
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
        return "Failed to Insert Event"