from models.CalendarEvent import EventDateTime

def serialize_event_datetime(event_datetime: EventDateTime) -> dict:
    """Serializes an EventDateTime object to a dictionary."""
    serialized = {}
    if event_datetime.date:
        serialized['date'] = event_datetime.date.isoformat()
    if event_datetime.dateTime:
        serialized['dateTime'] = event_datetime.dateTime.isoformat()
    if event_datetime.timeZone:
        serialized['timeZone'] = event_datetime.timeZone
    return serialized