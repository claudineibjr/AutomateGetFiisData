import locale

def formatAsNumber(value: float) -> str:
  try:
    locale.setlocale(locale.LC_ALL, "pt_BR")
    return locale.currency(value, grouping=True, symbol=False)
  except:
    return "N/A"