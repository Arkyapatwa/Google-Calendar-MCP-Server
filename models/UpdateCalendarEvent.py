from typing import Optional, List, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime
from datetime import date as dte

class EventDateTime(BaseModel):
    """Represents the start or end time of an event."""
    date: Optional[dte] = Field(None, description="The date, in the format YYYY-MM-DD, if this is an all-day event.")
    dateTime: Optional[datetime] = Field(None, description="The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.")
    timeZone: Optional[str] = Field(None, description="The time zone in which the time is specified. (e.g. 'America/Los_Angeles').")

class EventAttendee(BaseModel):
    """Represents an attendee of an event."""
    email: Optional[str] = Field(None, description="The attendee's email address.")
    displayName: Optional[str] = Field(None, description="The attendee's name, if available.")
    optional: Optional[bool] = Field(None, description="Whether this is an optional attendee.")
    responseStatus: Optional[str] = Field(None, description="The attendee's response status. Possible values are: 'needsAction', 'declined', 'tentative', 'accepted'.")
    comment: Optional[str] = Field(None, description="Comments from the attendee.")
    additionalGuests: Optional[int] = Field(None, description="Number of additional guests.")

class EventReminder(BaseModel):
    """Represents a reminder for an event."""
    method: Optional[str] = Field(None, description="The method used to send the reminder. Possible values are: 'email', 'popup'.")
    minutes: Optional[int] = Field(None, description="Number of minutes before the start of the event when the reminder should trigger.")

class EventReminders(BaseModel):
    """Represents reminders for an event."""
    useDefault: Optional[bool] = Field(None, description="Whether the default reminders of the calendar should be used.")
    overrides: Optional[List[EventReminder]] = Field(None, description="List of reminder overrides.")

class EventExtendedProperties(BaseModel):
    """Extended properties of the event."""
    private: Optional[Dict[str, str]] = Field(None, description="Private properties of the event.")
    shared: Optional[Dict[str, str]] = Field(None, description="Shared properties of the event.")

class EventSource(BaseModel):
    """Source of the event."""
    url: Optional[str] = Field(None, description="URL of the source.")
    title: Optional[str] = Field(None, description="Title of the source.")

class EventGadget(BaseModel):
    """Gadget of the event."""
    type: Optional[str] = Field(None, description="Type of the gadget.")
    title: Optional[str] = Field(None, description="Title of the gadget.")
    link: Optional[str] = Field(None, description="Link to the gadget.")
    iconLink: Optional[str] = Field(None, description="Link to the gadget icon.")
    width: Optional[int] = Field(None, description="Width of the gadget.")
    height: Optional[int] = Field(None, description="Height of the gadget.")
    display: Optional[str] = Field(None, description="Display mode of the gadget.")
    preferences: Optional[Dict[str, str]] = Field(None, description="Preferences of the gadget.")

class UpdateCalendarEvent(BaseModel):
    """Represents a Google Calendar event."""
    summary: Optional[str] = Field(None, description="Title of the event.") 
    start: Optional[EventDateTime] = Field(None, description="Start time of the event.") 
    end: Optional[EventDateTime] = Field(None, description="End time of the event.") 
    location: Optional[str] = Field(None, description="Location of the event.")
    description: Optional[str] = Field(None, description="Description of the event.")
    endTimeUnspecified: Optional[bool] = Field(None, description="Whether the end time is unspecified.")
    recurrence: Optional[List[str]] = Field(None, description="Recurrence rules for the event.")
    recurringEventId: Optional[str] = Field(None, description="The id of the recurring event.")
    originalStartTime: Optional[EventDateTime] = Field(None, description="The original start time of the instance.")
    transparency: Optional[str] = Field(None, description="Transparency of the event. Possible values are: 'opaque', 'transparent'.")
    visibility: Optional[str] = Field(None, description="Visibility of the event. Possible values are: 'default', 'public', 'private', 'confidential'.")
    iCalUID: Optional[str] = Field(None, description="iCalUID of the event.")
    sequence: Optional[int] = Field(None, description="Sequence number of the event.")
    attendees: Optional[List[EventAttendee]] = Field(None, description="Attendees of the event.")
    reminders: Optional[EventReminders] = Field(None, description="Reminders for the event.")
    creator: Optional[EventAttendee] = Field(None, description="Creator of the event.")
    organizer: Optional[EventAttendee] = Field(None, description="Organizer of the event.")
    guestsCanInviteOthers: Optional[bool] = Field(None, description="Whether guests can invite other guests.")
    guestsCanSeeOtherGuests: Optional[bool] = Field(None, description="Whether guests can see other guests.")
    guestsCanModify: Optional[bool] = Field(None, description="Whether guests can modify the event.")
    hangoutLink: Optional[str] = Field(None, description="Hangout link of the event.")
    extendedProperties: Optional[EventExtendedProperties] = Field(None, description="Extended properties of the event.")
    privateCopy: Optional[bool] = Field(None, description="Whether this is a private copy of the event.")
    locked: Optional[bool] = Field(None, description="Whether the event is locked.")
    anyoneCanAddSelf: Optional[bool] = Field(None, description="Whether anyone can add themselves to the event.")
    source: Optional[EventSource] = Field(None, description="Source of the event.")
    gadget: Optional[EventGadget] = Field(None, description="Gadget of the event.")
    attachments: Optional[List[Dict[str, str]]] = Field(None, description="Attachments of the event.")
    eventType: Optional[str] = Field(None, description="Type of the event. Possible values are: 'default', 'outOfOffice', 'focusTime'.")
    id: Optional[str] = Field(None, description="The id of the event.")
    htmlLink: Optional[str] = Field(None, description="A link to the event's HTML representation.")
    updated: Optional[datetime] = Field(None, description="Last modification time of the event (as an RFC3339 timestamp).")
    created: Optional[datetime] = Field(None, description="Creation time of the event (as an RFC3339 timestamp).")
    status: Optional[str] = Field(None, description="Status of the event. Possible values are: 'tentative', 'confirmed', 'cancelled'.")
    kind: Optional[str] = Field(None, description="Type of the resource ('calendar#event').")
    etag: Optional[str] = Field(None, description="ETag of the resource.")