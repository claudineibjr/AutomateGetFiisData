from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def getDriver():
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")

  chromeService=Service('/Users/claudineibjr/Projects/AutomateGetFIIsData/Libraries/chromedriver')
  driver = webdriver.Chrome(service=chromeService, options=options)
  return driver

def printTicketTitle(ticket):
  title = 'Ticket: ' + ticket
  timesToRepeatHiphenOnTitle = len(title) + 4 + 3 * 3 + 1
  print('')
  print('-' * timesToRepeatHiphenOnTitle)
  print('-' * 3 + ' ' + title + ' ' + '-' * 3*3)
  print('-' * timesToRepeatHiphenOnTitle)


def getTicketInfo(driver, ticket):
  printTicketTitle(ticket)
  
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

  # FIIs
  driver.get('https://fiis.com.br/' + ticket)

  # Tabela de últimos rendimentos
  try:
    lastRevenuesTable = driver.find_element(By.ID, 'last-revenues--table').find_element(By.TAG_NAME, 'tbody')
    lastRevenuesRows = lastRevenuesTable.find_elements(By.TAG_NAME, 'tr')
    
    rowCount = 0

    print('Histórico:')

    for row in lastRevenuesRows:
      if (rowCount <= 5):
        price = row.find_elements(By.TAG_NAME, 'td')[2].text
        income = row.find_elements(By.TAG_NAME, 'td')[4].text

        print('\t' + price + ' / ' + income)

        rowCount = rowCount + 1

    print('')
  except:
    print ('Últimos valores/rendimentos: Failure')

driver = getDriver()

driver.quit()
