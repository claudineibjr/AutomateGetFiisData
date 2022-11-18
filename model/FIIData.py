from typing import NamedTuple
from .HistoryData import HistoryData

class FIIData(NamedTuple):
  ticker: str # Papel
  name: str # Descrição
  sector: str # Setor
  segment: str # Segmento
  price: str # Valor Cota
  assetValue: str # Valor Patrimonial
  incomeValue: str # Dividendo
  liquidity: str # Liquidez
  vacancy: str # Vacância
  grossLeasableArea: str # Área bruta locável (m²)
  patrimony: str # Patrimônio
  numberOfAssets: str # Nº Ativos
  historicalDataList: list[HistoryData]

 # Nº Contratos
 # Score FE
 # Risco