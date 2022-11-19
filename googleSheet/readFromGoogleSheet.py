from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd

from env import SPREADSHEET_ID, SPREADSHEET_RANGE

def readFromGoogleSheet(creds: Credentials):
  try:
    # Call the Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE).execute()
    values = result.get('values', [])

    # Create a data frame
    data = pd.DataFrame(values)
    data.columns = data.iloc[0]
    data = data[1:]

    print(data)

    if pd.DataFrame(data['Papel'] == 'KNRI11').bool():
      print('Exist')
  except HttpError as err:
    print(err)