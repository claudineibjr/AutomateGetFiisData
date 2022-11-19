import os.path

from typing import NamedTuple

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd

from model.FIIData import FIIData
from env import SPREADSHEET_ID, SPREADSHEET_RANGE

# Papel
# Descrição
# Setor
# Segmento
# Valor Cota
# Dividendo
# Valor Patrimonial
# Vacância
# Patrimônio
# Nº Ativos
# Nº Contratos
# Liquidez
# Outras Informações
# Score FE
# Risco
# Área bruta locável (m²)

class SpreadsheetInterface(NamedTuple):
  papel: str
  descrição: str
  setor: str
  segmento: str
  valorCota: str
  dividendo: str
  valorPatrimonial: str
  vacância: str
  patrimônio: str
  nAtivos: str
  nContratos: str
  liquidez: str
  outrasInformacoes: str
  scoreFE: str
  risco: str
  areaBrutaLocavel: str

def writeOnGoogleSheet(creds: Credentials, data: list[FIIData]):
  # Call the Sheets API
  service = build('sheets', 'v4', credentials=creds)
  sheet = service.spreadsheets()

  spreadsheetData:list[SpreadsheetInterface] = list()
  
  for fiiData in data:
    fiiDataOnSpreadsheet = SpreadsheetInterface(
      papel=fiiData.ticker, descrição=fiiData.name, setor=fiiData.sector, segmento=fiiData.segment,
      valorCota=fiiData.price, dividendo=fiiData.incomeValue, valorPatrimonial=fiiData.assetValue, vacância=fiiData.vacancy,
      patrimônio=fiiData.patrimony, nAtivos=fiiData.numberOfAssets, nContratos="TO DO", liquidez=fiiData.liquidity, outrasInformacoes="TO DO",
      scoreFE=" TO DO", risco="TO DO", areaBrutaLocavel=fiiData.grossLeasableArea
    )
    spreadsheetData.append(fiiDataOnSpreadsheet)


  dataFrame = pd.DataFrame(spreadsheetData)
  print(dataFrame)

  result = sheet.values().update( spreadsheetId=SPREADSHEET_ID,
                                  range=SPREADSHEET_RANGE,
                                  valueInputOption='RAW',
                                  body={'values': dataFrame.values.tolist()}).execute()