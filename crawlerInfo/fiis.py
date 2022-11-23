from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from model.HistoryData import HistoryData

from util.parseTextToFloat import parseTextToFloat

def open(driver: WebDriver, ticker: str):
  driver.get('https://fiis.com.br/' + ticker)

def getTickerName(driver: WebDriver) -> str:
  # Nome
  try:
    stockName = driver.find_element(By.ID, "fund-name")
    return stockName.text
  except:
    return

def getHistoricalData(driver: WebDriver) -> list[HistoryData]:
  # Dados histórico
  data:list[HistoryData] = list()
  
  try:
    lastRevenuesTable = driver.find_element(By.ID, 'last-revenues--table').find_element(By.TAG_NAME, 'tbody')
    lastRevenuesRows = lastRevenuesTable.find_elements(By.TAG_NAME, 'tr')
    
    rowCount = 0

    for row in lastRevenuesRows:
      if (rowCount <= 5):
        price = parseTextToFloat(row.find_elements(By.TAG_NAME, 'td')[2].text)
        income = parseTextToFloat(row.find_elements(By.TAG_NAME, 'td')[4].text)
        data.append(HistoryData(price, income))

        rowCount = rowCount + 1

    return data
  except:
    return []

def getNumberOfShareHolders(driver: WebDriver) -> int:
  # Número de cotistas
  try:
    numberOfShareHoldersParentElement = driver.find_element(By.XPATH, "//*[text()='Número de Cotistas']").find_element(By.XPATH, "..")
    numberOfShareHolders = numberOfShareHoldersParentElement.find_element(By.CLASS_NAME, "value")
    return int(parseTextToFloat(numberOfShareHolders.text))
  except:
    return

def getCreationDateAtCVM(driver: WebDriver) -> str:
  # Data de registro na CVM
  try:
    creationDateAtCVMParentElement = driver.find_element(By.XPATH, "//*[text()='Registro CVM']").find_element(By.XPATH, "..")
    creationDateAtCVM = creationDateAtCVMParentElement.find_element(By.CLASS_NAME, "value")
    return creationDateAtCVM.text
  except:
    return