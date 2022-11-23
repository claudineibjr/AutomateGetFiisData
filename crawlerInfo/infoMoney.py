from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from util.parseTextToFloat import parseTextToFloat

def open(driver: WebDriver, ticker: str):
  driver.get('https://www.infomoney.com.br/' + ticker)

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

def getRisk(driver: WebDriver) -> int:
  # Segment
  try:
    riskParentElement = driver.find_element(By.CLASS_NAME, "cotacoes__yield").find_element(By.TAG_NAME, "a").find_elements(By.TAG_NAME, 'span')
    risk = riskParentElement[len(riskParentElement) - 1]
    return int(parseTextToFloat(risk.text))
  except:
    return