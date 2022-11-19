from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from util.parseTextToFloat import parseTextToFloat

def open(driver: WebDriver, ticker: str):
  driver.get('https://www.fundsexplorer.com.br/funds/' + ticker)

def getStockPrice(driver: WebDriver) -> float:
  # Preço
  try:
    stockPrice = driver.find_element(By.CLASS_NAME, "price")
    return parseTextToFloat(stockPrice.text)
  except:
    return

def getAssetValue(driver: WebDriver) -> float:
  # Valor patrimonial
  try:
    assetValueElement = driver.find_element(By.XPATH, "//*[text()='Valor Patrimonial']")
    assetValueParentElement = assetValueElement.find_element(By.XPATH, "..")
    assetValue = assetValueParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return parseTextToFloat(assetValue.text)
  except:
    return

def getIncomeValue(driver: WebDriver) -> float:
  # Dividendo
  try:
    lastIncomeElement = driver.find_element(By.XPATH, "//*[text()='Último Rendimento']")
    lastIncomeParentElement = lastIncomeElement.find_element(By.XPATH, "..")
    lastIncome = lastIncomeParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return parseTextToFloat(lastIncome.text)
  except:
    return

def getLiquidity(driver: WebDriver) -> float:
  # Liquidez
  try:
    dailyLiquidityElement = driver.find_element(By.XPATH, "//*[text()='Liquidez Diária']")
    dailyLiquidityParentElement = dailyLiquidityElement.find_element(By.XPATH, "..")
    dailyLiquidity = dailyLiquidityParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return parseTextToFloat(dailyLiquidity.text)
  except:
    return

def getNumberOfAssets(driver: WebDriver) -> float:
  # Número de ativos
  try:
    numberOfAssetsElement = driver.find_element(By.ID, "fund-actives-chart-info-wrapper").find_element(By.CLASS_NAME, "fund-actives")
    return float(numberOfAssetsElement.text)
  except:
    return