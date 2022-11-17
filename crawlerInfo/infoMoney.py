from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

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