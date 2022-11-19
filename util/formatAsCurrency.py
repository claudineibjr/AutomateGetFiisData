from util.formatAsNumber import formatNumber
from util.getTickerInfo import notApplicableText

def formatAsCurrency(value: float) -> str:
  try:
    return "R$ " + formatNumber(value)
  except:
    return notApplicableText