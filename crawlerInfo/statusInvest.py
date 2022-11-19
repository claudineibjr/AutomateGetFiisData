from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from util.parseTextToFloat import parseTextToFloat

def open(driver: WebDriver, ticker: str):
  driver.get('https://statusinvest.com.br/fundos-imobiliarios/' + ticker)

def getPatrimony(driver: WebDriver) -> float:
  # Patrimônio
  try:
    patrimonyElement = driver.find_element(By.XPATH, "//*[text()='Val. patrim. p/cota']").find_element(By.XPATH, "//*[text()='Patrimônio']")
    patrimonyParentElement = patrimonyElement.find_element(By.XPATH, "..")
    patrimony = patrimonyParentElement.find_element(By.CLASS_NAME, "sub-value")
    return parseTextToFloat(patrimony.text)
  except:
    return