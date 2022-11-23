from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd

from env import SPREADSHEET_ID, SPREADSHEET_READ_RANGE

def readFromGoogleSheet(creds: Credentials) -> pd.DataFrame:
  try:
    # Call the Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_READ_RANGE).execute()
    values = result.get('values', [])

    # Create a data frame
    data = pd.DataFrame(values)

    # Set the first row as header
    new_header = data.iloc[0]
    data = data[1:]
    data.columns = new_header

    return data
  except HttpError as err:
    print(err)