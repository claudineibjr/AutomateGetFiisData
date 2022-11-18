import sys
from selenium.webdriver.chrome.webdriver import WebDriver

import crawlerInfo.fundsExplorer as fundsExplorer
import crawlerInfo.fiis as fiis
import crawlerInfo.infoMoney as infoMoney
import crawlerInfo.clubeFii as clubeFII
import crawlerInfo.statusInvest as statusInvest

from model.FIIData import FIIData

from util.getDriver import getDriver
from util.printTickerTitle import printTickerTitle
from util.printTickerInfo import printTickerInfo
from util.getTickerInfo import getTickerInfo

def main():
  driver = getDriver()

  if (len(sys.argv) > 1):
    ticker = sys.argv[1]
    printTickerInfo(getTickerInfo(driver, ticker))
  else:
    fiisToQuery = ['CPTS11']
    for fiiToQuery in fiisToQuery:
      printTickerInfo(getTickerInfo(driver, fiiToQuery))

  driver.quit()

if __name__ == "__main__":
    main()