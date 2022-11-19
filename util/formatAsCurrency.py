import locale

def formatAsCurrency(value: float) -> str:
  locale.setlocale(locale.LC_ALL, "pt_BR")
  return "R$ " + locale.currency(value, grouping=True, symbol=False)