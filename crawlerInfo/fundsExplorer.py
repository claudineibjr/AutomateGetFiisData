from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

def open(driver: WebDriver, ticker: str):
  driver.get('https://www.fundsexplorer.com.br/funds/' + ticker)

def getStockPrice(driver: WebDriver) -> str:
  # Preço
  try:
    stockPrice = driver.find_element(By.CLASS_NAME, "price")
    return stockPrice.text
  except:
    return

def getAssetValue(driver: WebDriver) -> str:
  # Valor patrimonial
  try:
    assetValueElement = driver.find_element(By.XPATH, "//*[text()='Valor Patrimonial']")
    assetValueParentElement = assetValueElement.find_element(By.XPATH, "..")
    assetValue = assetValueParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return assetValue.text
  except:
    return

def getIncomeValue(driver: WebDriver) -> str:
  # Dividendo
  try:
    lastIncomeElement = driver.find_element(By.XPATH, "//*[text()='Último Rendimento']")
    lastIncomeParentElement = lastIncomeElement.find_element(By.XPATH, "..")
    lastIncome = lastIncomeParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return lastIncome.text
  except:
    return

def getLiquidity(driver: WebDriver) -> str:
  # Liquidez
  try:
    dailyLiquidityElement = driver.find_element(By.XPATH, "//*[text()='Liquidez Diária']")
    dailyLiquidityParentElement = dailyLiquidityElement.find_element(By.XPATH, "..")
    dailyLiquidity = dailyLiquidityParentElement.find_element(By.CLASS_NAME, "indicator-value")
    return dailyLiquidity.text
  except:
    return