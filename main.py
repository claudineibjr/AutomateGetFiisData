from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--headless")

chromeService=Service('/Users/claudineibjr/Projects/AutomateGetFIIsData/Libraries/chromedriver')
driver = webdriver.Chrome(service=chromeService, options=options)

ticket = "VGHF11"

# Funds explorer
driver.get('https://www.fundsexplorer.com.br/funds/' + ticket)

# Preço
try:
  stockPrice = driver.find_element(By.CLASS_NAME, "price")
  print ('Preço: ' + stockPrice.text)
except:
  print ('Preço: Failure')

# Preço patrimonial
try:
  assetValueElement = driver.find_element(By.XPATH, "//*[text()='Valor Patrimonial']")
  assetValueParentElement = assetValueElement.find_element(By.XPATH, "..")
  assetValue = assetValueParentElement.find_element(By.CLASS_NAME, "indicator-value")
  print ('Valor patrimonial: ' + assetValue.text)
except:
  print ('Valor patrimonial: Failure')

# Dividendo
try:
  lastIncomeElement = driver.find_element(By.XPATH, "//*[text()='Último Rendimento']")
  lastIncomeParentElement = lastIncomeElement.find_element(By.XPATH, "..")
  lastIncome = lastIncomeParentElement.find_element(By.CLASS_NAME, "indicator-value")
  print ('Último dividendo: ' + lastIncome.text)
except:
  print ('Último dividendo: Failure')

# Liquidez
try:
  dailyLiquidityElement = driver.find_element(By.XPATH, "//*[text()='Liquidez Diária']")
  dailyLiquidityParentElement = dailyLiquidityElement.find_element(By.XPATH, "..")
  dailyLiquidity = dailyLiquidityParentElement.find_element(By.CLASS_NAME, "indicator-value")
  print ('Liquidez diária: ' + dailyLiquidity.text)
except:
  print ('Liquidez diária: Failure')

print ("End")

driver.quit()
