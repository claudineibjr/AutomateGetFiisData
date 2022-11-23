import sys
from selenium.webdriver.chrome.webdriver import WebDriver

from model.FIIData import FIIData

from util.getDriver import getDriver
from util.printTickerInfo import printTickerInfo
from util.getTickerInfo import getTickerInfo

from googleSheet.authorize import authorize
from googleSheet.writeOnGoogleSheet import writeOnGoogleSheet
from googleSheet.readFromGoogleSheet import readFromGoogleSheet

from util.formatAsPercentage import formatAsPercentage

import pandas as pd
from typing import NamedTuple
import numpy as np

def main():
  driver = getDriver()

  credentials = authorize()

  data:list[FIIData] = list()

  if (len(sys.argv) > 1):
    for ticker in sys.argv[1:]:
      tickerInfo = getTickerInfo(driver, ticker)
      data.append(tickerInfo)
      printTickerInfo(tickerInfo)
  else:
    fiisToQuery = ['']
    for ticker in fiisToQuery:
      tickerInfo = getTickerInfo(driver, ticker)
      data.append(tickerInfo)
      printTickerInfo(tickerInfo)

  oldData = readFromGoogleSheet(credentials)

  writeOnGoogleSheet(credentials, oldData, data)

  print("Done")

  driver.quit()

if __name__ == "__main__":
  main()
