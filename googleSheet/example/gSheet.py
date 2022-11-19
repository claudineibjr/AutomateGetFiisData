import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = 'TODO'
SAMPLE_RANGE_NAME_READ = 'TODO'
SAMPLE_RANGE_NAME_WRITE = 'TODO'


def authorize() -> Credentials:
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('.env/token.json'):
        creds = Credentials.from_authorized_user_file(
            '.env/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '.env/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('.env/token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def readFromGoogleSheet(creds: Credentials):
    try:
        # Call the Sheets API
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME_READ).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)


def writeOnGoogleSheet(creds: Credentials):
    # Call the Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    newValues = [
        ['ABC', '123'],
        ['DEF', '456'],
    ]

    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                   range=SAMPLE_RANGE_NAME_WRITE,
                                   valueInputOption='RAW',
                                   body={'values': newValues}).execute()


def main():
    creds = authorize()

    readFromGoogleSheet(creds)
    writeOnGoogleSheet(creds)


if __name__ == '__main__':
    main()
