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

def getTickerInfo(driver: WebDriver, ticker: str) -> FIIData:
  try:
    printTickerTitle(ticker)

    # --------------------
    # Funds explorer -----
    fundsExplorer.open(driver, ticker)

    # Preço / Cota
    stockPrice = fundsExplorer.getStockPrice(driver) or "---"

    # Preço patrimonial
    assetValue = fundsExplorer.getAssetValue(driver) or "---"
    
    # Dividendo
    incomeValue = fundsExplorer.getIncomeValue(driver) or "---"

    # Liquidez
    liquidity = fundsExplorer.getLiquidity(driver) or "---"

    # ----------
    # FIIs -----
    fiis.open(driver, ticker)

    # Nome
    name = fiis.getTickerName(driver) or "---"

    # Tabela de últimos rendimentos
    historicalDataList = fiis.getHistoricalData(driver) or []

    # ----------------
    # Info Money -----
    infoMoney.open(driver, ticker)

    # Setor
    sector = infoMoney.getSector(driver) or '---'

    # Segmento
    segment = infoMoney.getSegment(driver) or '---'

    # ---------------
    # Clube FII -----
    clubeFII.open(driver, ticker)

    # Vacância
    vacancy = clubeFII.getVacancy(driver) or "---"

    # Área bruta locável
    grossLeasableArea = clubeFII.getGrossLeasableArea(driver) or '---'

    # -------------------
    # Status Invest -----
    statusInvest.open(driver, ticker)

    # Patrimônio
    patrimony = statusInvest.getPatrimony(driver) or '---'

    data = FIIData(ticker, name, sector, segment, stockPrice, assetValue, incomeValue, liquidity, vacancy, grossLeasableArea, patrimony, historicalDataList)
    
    return data

  except Exception as error:
    print ('Error to get ' + ticker + ' information')
    print (error)


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