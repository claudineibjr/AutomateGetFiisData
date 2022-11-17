from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open(driver: WebDriver, ticker: str):
  driver.get('https://www.clubefii.com.br/fiis/' + ticker)

  # Wait the call be loaded
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lbl_cod_neg")))

def getVacancy(driver: WebDriver) -> str:
  # Vacância
  try:
    vacancyElement = driver.find_element(By.ID, "vacancia").find_element(By.CLASS_NAME, "info").find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "strong")
    vacancy = vacancyElement[len(vacancyElement) - 1]
    return vacancy.text
  except:
    return

def getGrossLeasableArea(driver: WebDriver) -> str:
  # Área bruta locável
  try:
    grossLeasableAreaElement = driver.find_element(By.XPATH, "//*[text()='ABL (M²)']")
    grossLeasableAreaParentElement = grossLeasableAreaElement.find_element(By.XPATH, "../..")
    grossLeasableArea = grossLeasableAreaParentElement.find_element(By.TAG_NAME, "td")
    return grossLeasableArea.text
  except:
    return