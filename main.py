from typing import NamedTuple
# from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

class HistoryData(NamedTuple):
    price: str
    income: str

class FIIData(NamedTuple):
  ticker: str
  name: str
  sector: str
  segment: str
  price: str
  assetValue: str
  incomeValue: str
  liquidity: str
  vacancy: str
  grossLeasableArea: str
  patrimony: str
  historicalDataList: list[HistoryData]

def getDriver() -> WebDriver:
  options = Options()
  options.add_argument("--headless")
  
  # chromeService=Service('/Users/claudineibjr/Projects/AutomateGetFIIsData/Libraries/chromedriver')
  # driver = webdriver.Chrome(service=chromeService, options=options)
  driver = uc.Chrome(options=options)

  return driver

def printTickerTitle(ticker: str):
  repetitionNumber = 3

  title = 'Ticker: ' + ticker
  timesToRepeatHiphenOnTitle = len(title) + repetitionNumber + 1 + repetitionNumber * repetitionNumber + 1
  print('-' * timesToRepeatHiphenOnTitle)
  print('-' * repetitionNumber + ' ' + title + ' ' + '-' * repetitionNumber * repetitionNumber)
  print('-' * timesToRepeatHiphenOnTitle)


def getStockPrice(driver: WebDriver) -> str:
  # Preço
  try:
    stockPrice = driver.find_element(By.CLASS_NAME, "price")
    return stockPrice.text
  except:
    return

def getTickerName(driver: WebDriver) -> str:
  # Nome
  try:
    stockName = driver.find_element(By.ID, "fund-name")
    return stockName.text
  except:
    return

def getSector(driver: WebDriver) -> str:
  # Setor
  try:
    sectorElement = driver.find_element(By.XPATH, "//*[text()='Setor']")
    sectorParentElement = sectorElement.find_element(By.XPATH, "..")
    sector = sectorParentElement.find_element(By.TAG_NAME, "p")
    return sector.text
  except:
    return

def getSegment(driver: WebDriver) -> str:
  # Segment
  try:
    segmentElement = driver.find_element(By.XPATH, "//*[text()='Segmento']")
    segmentParentElement = segmentElement.find_element(By.XPATH, "..")
    segment = segmentParentElement.find_element(By.TAG_NAME, "p")
    return segment.text
  except:
    return

def getAssetValue(driver: WebDriver) -> str:
  try:
    assetValueElement = driver.find_element(By.XPATH, "//*[text()='Valor Patrimonial']")
    assetValueParentElement = assetValueElement.find_element(By.XPATH, "..")
    assetValue = assetValueParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return assetValue.text
  except:
    return

def getIncomeValue(driver: WebDriver) -> str:
  try:
    lastIncomeElement = driver.find_element(By.XPATH, "//*[text()='Último Rendimento']")
    lastIncomeParentElement = lastIncomeElement.find_element(By.XPATH, "..")
    lastIncome = lastIncomeParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return lastIncome.text
  except:
    return

def getLiquidity(driver: WebDriver) -> str:
  try:
    dailyLiquidityElement = driver.find_element(By.XPATH, "//*[text()='Liquidez Diária']")
    dailyLiquidityParentElement = dailyLiquidityElement.find_element(By.XPATH, "..")
    dailyLiquidity = dailyLiquidityParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return dailyLiquidity.text
  except:
    return

def getVacancy(driver: WebDriver) -> str:
  try:
    vacancyElement = driver.find_element(By.ID, "vacancia").find_element(By.CLASS_NAME, "info").find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "strong")
    vacancy = vacancyElement[len(vacancyElement) - 1]
    return vacancy.text
  except:
    return

def getGrossLeasableArea(driver: WebDriver) -> str:
  try:
    grossLeasableAreaElement = driver.find_element(By.XPATH, "//*[text()='ABL (M²)']")
    grossLeasableAreaParentElement = grossLeasableAreaElement.find_element(By.XPATH, "../..")
    grossLeasableArea = grossLeasableAreaParentElement.find_element(By.TAG_NAME, "td")
    return grossLeasableArea.text
  except:
    return

def getPatrimony(driver: WebDriver) -> str:
  try:
    patrimonyElement = driver.find_element(By.XPATH, "//*[text()='Val. patrim. p/cota']").find_element(By.XPATH, "//*[text()='Patrimônio']")
    patrimonyParentElement = patrimonyElement.find_element(By.XPATH, "..")
    patrimony = patrimonyParentElement.find_element(By.CLASS_NAME, "sub-value")
    return patrimony.text
  except:
    return

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
    return []

def getTickerInfo(driver: WebDriver, ticker: str) -> FIIData:
  try:
    printTickerTitle(ticker)

    # Funds explorer
    driver.get('https://www.fundsexplorer.com.br/funds/' + ticker)

    # Preço / Cota
    stockPrice = getStockPrice(driver) or "---"

    # Preço patrimonial
    assetValue = getAssetValue(driver) or "---"
    
    # Dividendo
    incomeValue = getIncomeValue(driver) or "---"

    # Liquidez
    liquidity = getLiquidity(driver) or "---"

    # FIIs
    driver.get('https://fiis.com.br/' + ticker)

    # Nome
    name = getTickerName(driver) or "---"

    # Tabela de últimos rendimentos
    historicalDataList = getHistoricalData(driver) or []

    # Info Money
    driver.get('https://www.infomoney.com.br/' + ticker)

    # Setor
    sector = getSector(driver) or '---'

    # Segmento
    segment = getSegment(driver) or '---'

    # Clube FII
    driver.get('https://www.clubefii.com.br/fiis/' + ticker)

    # Wait the call be loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lbl_cod_neg")))

    # Vacância
    vacancy = getVacancy(driver) or "---"

    # Área bruta locável
    grossLeasableArea = getGrossLeasableArea(driver) or '---'

    # Status Invest
    driver.get('https://statusinvest.com.br/fundos-imobiliarios/' + ticker)

    # Patrimônio
    patrimony = getPatrimony(driver) or '---'

    data = FIIData(ticker, name, sector, segment, stockPrice, assetValue, incomeValue, liquidity, vacancy, grossLeasableArea, patrimony, historicalDataList)
    
    return data

  except Exception as error:
    print ('Error to get ' + ticker + ' information')
    print (error)


def printTickerInfo(data: FIIData):
  print ('Nome: ' + data.name)
  print ('Setor: ' + data.sector)
  print ('Segmento: ' + data.segment)
  print ('Preço: ' + data.price)
  print ('Valor patrimonial: ' + data.assetValue)
  print ('Dividendo: ' + data.incomeValue)
  print ('Liquidez diária: ' + data.liquidity)
  print ("Vacância: " + data.vacancy)
  print ("Área bruta locável (m²): " + data.grossLeasableArea)
  print ("Patrimônio:  " + data.patrimony)
  print ('Histórico: ')
  for historicalData in data.historicalDataList:
    print ('   ' + historicalData.price + ' / ' + historicalData.income)

def main():
  try:
    driver = getDriver()
  except Exception as error:
    print ('Error to get driver')
    print (error)
    return

  printTickerInfo(getTickerInfo(driver, 'XPLG11'))
  # getTickerInfo(driver, 'XPLG11')

  driver.quit()

if __name__ == "__main__":
    main()