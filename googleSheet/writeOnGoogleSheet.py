from typing import NamedTuple

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import pandas as pd

from datetime import datetime

from util.getTickerInfo import notApplicableText

from model.FIIData import FIIData
from model.HistoryData import HistoryData

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
  nCotistas: str
  outrasInformacoes: str
  scoreFE: str
  risco: str
  areaBrutaLocavel: str
  dataRegistro: str
  valorCota_1: str
  dividendo_1: str
  valorCota_2: str
  dividendo_2: str
  valorCota_3: str
  dividendo_3: str
  valorCota_4: str
  dividendo_4: str
  valorCota_5: str
  dividendo_5: str
  valorCota_6: str
  dividendo_6: str
  atualizadoEm: str

def getHistoricalPrice(data: list[HistoryData], index: int) -> str:
  if (index < len(data)):
    return data[index].price
  else:
    return notApplicableText

def getHistoricalIncome(data: list[HistoryData], index: int) -> str:
  if (index < len(data)):
    return data[index].income
  else:
    return notApplicableText

def writeOnGoogleSheet(creds: Credentials, oldData: pd.DataFrame, data: list[FIIData]):
  # Call the Sheets API
  service = build('sheets', 'v4', credentials=creds)
  sheet = service.spreadsheets()

  spreadsheetData:list[SpreadsheetInterface] = list()
  
  for fiiData in data:
    historicalData = fiiData.historicalDataList

    fiiDataOnSpreadsheet = SpreadsheetInterface(
      papel=fiiData.ticker, descrição=fiiData.name, setor=fiiData.sector, segmento=fiiData.segment,
      valorCota=fiiData.price, dividendo=fiiData.incomeValue, valorPatrimonial=fiiData.assetValue, vacância=fiiData.vacancy,
      patrimônio=fiiData.patrimony, nAtivos=fiiData.numberOfAssets, nContratos="TO DO", liquidez=fiiData.liquidity, nCotistas=fiiData.numberOfShareHolders,
      outrasInformacoes="TO DO", scoreFE=" TO DO", risco="TO DO", areaBrutaLocavel=fiiData.grossLeasableArea, dataRegistro=fiiData.creationDateAtCVM,
      valorCota_1=getHistoricalPrice(historicalData, 0), dividendo_1=getHistoricalIncome(historicalData, 0),
      valorCota_2=getHistoricalPrice(historicalData, 1), dividendo_2=getHistoricalIncome(historicalData, 1),
      valorCota_3=getHistoricalPrice(historicalData, 2), dividendo_3=getHistoricalIncome(historicalData, 2),
      valorCota_4=getHistoricalPrice(historicalData, 3), dividendo_4=getHistoricalIncome(historicalData, 3),
      valorCota_5=getHistoricalPrice(historicalData, 4), dividendo_5=getHistoricalIncome(historicalData, 4),
      valorCota_6=getHistoricalPrice(historicalData, 5), dividendo_6=getHistoricalIncome(historicalData, 5),
      atualizadoEm=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    spreadsheetData.append(fiiDataOnSpreadsheet)


  newDataFrame = pd.DataFrame(spreadsheetData)
  dataFrame = pd.concat([newDataFrame, oldData]).drop_duplicates(subset="papel")

  sheet.values().update(  spreadsheetId=SPREADSHEET_ID,
                          range=SPREADSHEET_RANGE,
                          valueInputOption='USER_ENTERED',
                          body={'values': dataFrame.values.tolist()}).execute()
