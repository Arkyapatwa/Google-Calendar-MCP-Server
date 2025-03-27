from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ListEventsParameters:
    calendarId: str  # Required. The calendar ID.
    alwaysIncludeEmail: Optional[bool] = None  # Deprecated. Whether to always include the email of the creator.
    iCalUID: Optional[str] = None  # Specifies an event's iCalUID to filter by.
    maxAttendees: Optional[int] = None  # Max number of attendees to include in the response.
    maxResults: Optional[int] = None  # Max number of events to return in the result.
    orderBy: Optional[str] = None  # The order of the events returned. Can be 'startTime' or 'updated'.
    pageToken: Optional[str] = None  # Token specifying the result page to return.
    privateExtendedProperty: Optional[List[str]] = field(default_factory=list)  # Filters events based on private extended properties.
    q: Optional[str] = None  # Free-text search terms.
    sharedExtendedProperty: Optional[List[str]] = field(default_factory=list)  # Filters events based on shared extended properties.
    showDeleted: Optional[bool] = None  # Whether to include deleted events in the results.
    showHiddenInvitations: Optional[bool] = None  # Whether to include hidden invitations in the results.
    singleEvents: Optional[bool] = None  # Whether to expand recurring events into instances.
    syncToken: Optional[str] = None  # Token for syncing with the last state of the calendar.
    timeMax: Optional[str] = None  # Upper bound for event start time (ISO format).
    timeMin: Optional[str] = None  # Lower bound for event start time (ISO format).
    timeZone: Optional[str] = None  # Time zone for the response (e.g., 'America/Los_Angeles').
    updatedMin: Optional[str] = None  # Lower bound for last modification time (RFC3339 timestamp).