from model.FIIData import FIIData

from util.formatAsCurrency import formatAsCurrency
from util.formatAsNumber import formatAsNumber
from util.formatAsPercentage import formatAsPercentage

def printTickerInfo(data: FIIData):
  print ('Nome: ' + data.name)
  print ('Setor: ' + data.sector)
  print ('Segmento: ' + data.segment)
  print ('Preço: ' + formatAsCurrency(data.price))
  print ('Valor patrimonial: ' + formatAsCurrency(data.assetValue))
  print ('Dividendo: ' + formatAsCurrency(data.incomeValue))
  print ('Liquidez diária: ' + formatAsNumber(data.liquidity))
  print ("Número de cotistas: " + formatAsNumber(data.numberOfShareHolders))
  print ("Vacância: " + formatAsPercentage(data.vacancy))
  print ("Área bruta locável (m²): " + formatAsNumber(data.grossLeasableArea))
  print ("Patrimônio: " + formatAsCurrency(data.patrimony))
  print ("Número de ativos: " + data.numberOfAssets)
  print ('Histórico: ')
  for count, historicalData in enumerate(data.historicalDataList):
    countValue = count + 1
    monthStr = 'mês' if countValue == 1 else 'meses'
    print ('   ' + str(countValue) + ' ' + monthStr + ': ' + formatAsCurrency(historicalData.price) + ' / ' + formatAsCurrency(historicalData.income))

  print('')