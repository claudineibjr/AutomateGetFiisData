import locale

from util.getTickerInfo import notApplicableText

def formatAsNumber(value: float) -> str:
  locale.setlocale(locale.LC_ALL, "pt_BR")
  return locale.currency(value, grouping=True, symbol=False)