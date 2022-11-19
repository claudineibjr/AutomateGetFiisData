from util.formatAsNumber import formatNumber
from util.getTickerInfo import notApplicableText

def formatAsPercentage(value: float) -> str:
  try:
    return formatNumber(value * 100) + " %"
  except:
    return notApplicableText