import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from crewai_tools import BaseTool

class GmailFetchTool(BaseTool):
    name: str = "Gmail Fetch Tool"
    description: str = "Fetches emails from a Gmail account."

    def _run(self, argument: str) -> str:
        try:
            creds = None
            credentials_path = r'Your Credentials path here (FULL PATH NEEDED)'
            token_path = 'token.json'
            
            # Load existing credentials if available
            if os.path.exists(token_path):
                creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/gmail.readonly'])
            
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentials_path, ['https://www.googleapis.com/auth/gmail.readonly'])
                    creds = flow.run_local_server(port=0)
                
                # Save the credentials for the next run
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())

            # Build the service and fetch emails
            service = build('gmail', 'v1', credentials=creds)
            results = service.users().messages().list(userId='me', q=argument).execute()
            messages = results.get('messages', [])

            emails = []
            for message in messages[:10]:  # Fetch the top 10 emails for simplicity
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                payload = msg.get('payload', {})
                headers = payload.get('headers', [])
                parts = payload.get('parts', [])
                email_data = {}
                for header in headers:
                    if header['name'] == 'Subject':
                        email_data['subject'] = header['value']
                    elif header['name'] == 'From':
                        email_data['from'] = header['value']
                if parts:
                    body = base64.urlsafe_b64decode(parts[0]['body'].get('data', '').encode('ASCII')).decode('utf-8')
                    email_data['body'] = body
                emails.append(email_data)

            return str(emails)
        except Exception as e:
            return str(e)
