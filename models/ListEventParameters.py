from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ListEventsParameters(BaseModel):
    calendarId: str = Field(default="primary")
    timeMin: str = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    maxResults: int = Field(default=10)
    singleEvents: bool = Field(default=True)
    orderBy: str = Field(default="startTime")
    alwaysIncludeEmail: Optional[bool] = None
    iCalUID: Optional[str] = None
    maxAttendees: Optional[int] = None
    pageToken: Optional[str] = None
    privateExtendedProperty: Optional[List[str]] = []
    q: Optional[str] = None
    sharedExtendedProperty: Optional[List[str]] = []
    showDeleted: Optional[bool] = None
    showHiddenInvitations: Optional[bool] = None
    syncToken: Optional[str] = None
    timeMax: Optional[str] = None
    timeZone: Optional[str] = None
    updatedMin: Optional[str] = None