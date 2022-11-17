from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

def getDriver() -> WebDriver:
  try:
    options = Options()
    options.add_argument("--headless")
    
    driver = uc.Chrome(options=options)

    return driver
  except Exception as error:
    print ('Error to get driver')
    print (error)
    return    