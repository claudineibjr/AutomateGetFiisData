from model.FIIData import FIIData

def printTickerInfo(data: FIIData):
  print ('Nome: ' + data.name)
  print ('Setor: ' + data.sector)
  print ('Segmento: ' + data.segment)
  print ('Preço: ' + data.price)
  print ('Valor patrimonial: ' + data.assetValue)
  print ('Dividendo: ' + data.incomeValue)
  print ('Liquidez diária: ' + data.liquidity)
  print ("Vacância: " + data.vacancy)
  print ("Área bruta locável (m²): " + data.grossLeasableArea)
  print ("Patrimônio: " + data.patrimony)
  print ("Número de ativos " + data.numberOfAssets)
  print ('Histórico: ')
  for historicalData in data.historicalDataList:
    print ('   ' + historicalData.price + ' / ' + historicalData.income)

  print('')