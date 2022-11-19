from typing import NamedTuple
from .HistoryData import HistoryData

class FIIData(NamedTuple):
  ticker: str # Papel
  name: str # Descrição
  sector: str # Setor
  segment: str # Segmento
  price: float # Valor Cota
  assetValue: float # Valor Patrimonial
  incomeValue: float # Dividendo
  liquidity: float # Liquidez
  vacancy: float # Vacância
  grossLeasableArea: float # Área bruta locável (m²)
  patrimony: float # Patrimônio
  numberOfAssets: int # Nº Ativos
  # historicalDataList: list[HistoryData]

 # Nº Contratos
 # Score FE
 # Risco