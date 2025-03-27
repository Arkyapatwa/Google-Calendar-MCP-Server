import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the required scopes
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

class GoogleCalendarService:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GoogleCalendarService, cls).__new__(cls)
            cls._instance._initialize_service()
        return cls._instance

    def _initialize_service(self):
        """
        Initializes the Google Calendar API service.
        """
        creds = None

        # Check for existing credentials
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        
        # Refresh or create new credentials if necessary
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    './secrets/credentials.json', SCOPES
                )
                creds = flow.run_local_server(port=0)
            
            # Save the new credentials
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        # Create and store the service instance
        self.service = build('calendar', 'v3', credentials=creds)

    def get_service(self):
        """
        Returns the Google Calendar API service instance.
        """
        return self.service
