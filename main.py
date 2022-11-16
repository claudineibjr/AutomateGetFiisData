from typing import NamedTuple
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from collections import namedtuple

class HistoryData(NamedTuple):
    price: str
    income: str

class FIIData(NamedTuple):
  ticket: str
  price: str
  assetValue: str
  incomeValue: str
  liquidity: str
  historicalDataList: list[HistoryData]

def getDriver() -> WebDriver:
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")

  chromeService=Service('/Users/claudineibjr/Projects/AutomateGetFIIsData/Libraries/chromedriver')
  driver = webdriver.Chrome(service=chromeService, options=options)
  return driver

def printTicketTitle(ticket: str):
  repetitionNumber = 3

  title = 'Ticket: ' + ticket
  timesToRepeatHiphenOnTitle = len(title) + repetitionNumber + 1 + repetitionNumber * repetitionNumber + 1
  print('')
  print('-' * timesToRepeatHiphenOnTitle)
  print('-' * repetitionNumber + ' ' + title + ' ' + '-' * repetitionNumber * repetitionNumber)
  print('-' * timesToRepeatHiphenOnTitle)


def getStockPrice(driver: WebDriver) -> str:
  # Preço
  try:
    stockPrice = driver.find_element(By.CLASS_NAME, "price")
    return stockPrice.text
  except:
    print ('Preço: Failure')

def getAssetValue(driver: WebDriver) -> str:
  try:
    assetValueElement = driver.find_element(By.XPATH, "//*[text()='Valor Patrimonial']")
    assetValueParentElement = assetValueElement.find_element(By.XPATH, "..")
    assetValue = assetValueParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return assetValue.text
  except:
    print ('Valor patrimonial: Failure')

def getIncomeValue(driver: WebDriver) -> str:
  try:
    lastIncomeElement = driver.find_element(By.XPATH, "//*[text()='Último Rendimento']")
    lastIncomeParentElement = lastIncomeElement.find_element(By.XPATH, "..")
    lastIncome = lastIncomeParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return lastIncome.text
  except:
    print ('Último dividendo: Failure')  

def getLiquidity(driver: WebDriver) -> str:
  try:
    dailyLiquidityElement = driver.find_element(By.XPATH, "//*[text()='Liquidez Diária']")
    dailyLiquidityParentElement = dailyLiquidityElement.find_element(By.XPATH, "..")
    dailyLiquidity = dailyLiquidityParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return dailyLiquidity.text
  except:
    print ('Liquidez diária: Failure')  

def getHistoricalData(driver: WebDriver) -> list[HistoryData]:
  data:list[HistoryData] = list()
  
  try:
    lastRevenuesTable = driver.find_element(By.ID, 'last-revenues--table').find_element(By.TAG_NAME, 'tbody')
    lastRevenuesRows = lastRevenuesTable.find_elements(By.TAG_NAME, 'tr')
    
    rowCount = 0

    for row in lastRevenuesRows:
      if (rowCount <= 5):
        price = row.find_elements(By.TAG_NAME, 'td')[2].text
        income = row.find_elements(By.TAG_NAME, 'td')[4].text
        data.append(HistoryData(price, income))

        rowCount = rowCount + 1

    return data
  except:
    print ('Últimos valores/rendimentos: Failure')

def getTicketInfo(driver: WebDriver, ticket: str) -> FIIData:
  printTicketTitle(ticket)
  
  # Funds explorer
  driver.get('https://www.fundsexplorer.com.br/funds/' + ticket)

  # Preço / Cota
  stockPrice = getStockPrice(driver)

  # Preço patrimonial
  assetValue = getAssetValue(driver)
  
  # Dividendo
  incomeValue = getIncomeValue(driver)

  # Liquidez
  liquidity = getLiquidity(driver)

  # FIIs
  driver.get('https://fiis.com.br/' + ticket)

  # Tabela de últimos rendimentos
  historicalDataList = getHistoricalData(driver)

  data = FIIData(ticket, stockPrice, assetValue, incomeValue, liquidity, historicalDataList)

  return data

def printTicketInfo(data: FIIData):
  print ('Preço: ' + data.price)
  print ('Valor patrimonial: ' + data.assetValue)
  print ('Dividendo: ' + data.incomeValue)
  print ('Liquidez diária: ' + data.liquidity)
  print ('Histórico: ')
  for historicalData in data.historicalDataList:
    print ('   ' + historicalData.price + ' / ' + historicalData.income)

driver = getDriver()

printTicketInfo(getTicketInfo(driver, 'BTRA11'))

driver.quit()
