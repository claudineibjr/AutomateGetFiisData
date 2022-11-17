from typing import NamedTuple
from HistoryData import HistoryData

class FIIData(NamedTuple):
  ticker: str
  name: str
  sector: str
  segment: str
  price: str
  assetValue: str
  incomeValue: str
  liquidity: str
  vacancy: str
  grossLeasableArea: str
  patrimony: str
  historicalDataList: list[HistoryData]