from models import ListEventParameters
from google_calendar_connection import GoogleCalendarService

from typing import List
import logging

def list_calendar_events(parameters: ListEventParameters):
    calendar_service = GoogleCalendarService().get_service()
    
    try:
        params = {k: v for k, v in parameters.__dict__.items() if v is not None}
        
        events_result = calendar_service.events().list(**params)
        return events_result.execute().get('items', [])
    except Exception as e:
        logging.error(f"Failed to fetch calendar events: {e}")
        return []