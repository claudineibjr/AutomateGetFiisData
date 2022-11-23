from selenium.webdriver.chrome.webdriver import WebDriver

import crawlerInfo.fundsExplorer as fundsExplorer
import crawlerInfo.fiis as fiis
import crawlerInfo.infoMoney as infoMoney
import crawlerInfo.clubeFii as clubeFII
import crawlerInfo.statusInvest as statusInvest

from model.FIIData import FIIData

from util.printTickerTitle import printTickerTitle

notApplicableText = 'N/A'

def debugGetInfo(driver: WebDriver, ticker: str):
    infoMoney.open(driver, ticker)

    # Número de cotistas
    risk = infoMoney.getRisk(driver) or "notApplicableText"

    printTickerTitle(ticker)
    print(risk)

def getTickerInfo(driver: WebDriver, ticker: str) -> FIIData:
  try:
    printTickerTitle(ticker)

    # --------------------
    # Funds explorer -----
    fundsExplorer.open(driver, ticker)

    # Preço / Cota
    stockPrice = fundsExplorer.getStockPrice(driver) or notApplicableText

    # Preço patrimonial
    assetValue = fundsExplorer.getAssetValue(driver) or notApplicableText
    
    # Dividendo
    incomeValue = fundsExplorer.getIncomeValue(driver) or notApplicableText

    # Liquidez
    liquidity = fundsExplorer.getLiquidity(driver) or notApplicableText

    # Número de ativos
    numberOfAssets = fundsExplorer.getNumberOfAssets(driver) or notApplicableText

    # ----------
    # FIIs -----
    fiis.open(driver, ticker)

    # Nome
    name = fiis.getTickerName(driver) or notApplicableText

    # Tabela de últimos rendimentos
    historicalDataList = fiis.getHistoricalData(driver) or []

    # Número de cotistas
    numberOfShareHolders = fiis.getNumberOfShareHolders(driver) or notApplicableText

    # Data de registro na CVM
    creationDateAtCVM = fiis.getCreationDateAtCVM(driver) or notApplicableText

    # ----------------
    # Info Money -----
    infoMoney.open(driver, ticker)

    # Setor
    sector = infoMoney.getSector(driver) or notApplicableText

    # Segmento
    segment = infoMoney.getSegment(driver) or notApplicableText

    # Risco
    risk = infoMoney.getRisk(driver) or notApplicableText

    # ---------------
    # Clube FII -----
    clubeFII.open(driver, ticker)

    # Vacância
    vacancy = clubeFII.getVacancy(driver) or notApplicableText

    # Área bruta locável
    grossLeasableArea = clubeFII.getGrossLeasableArea(driver) or notApplicableText

    # -------------------
    # Status Invest -----
    statusInvest.open(driver, ticker)

    # Patrimônio
    patrimony = statusInvest.getPatrimony(driver) or notApplicableText

    data = FIIData(ticker, name, sector, segment, stockPrice, assetValue, incomeValue, liquidity, vacancy, grossLeasableArea, patrimony, numberOfAssets, numberOfShareHolders, creationDateAtCVM, risk, historicalDataList)
    
    return data

  except Exception as error:
    print ('Error to get ' + ticker + ' information')
    print (error)