from util.formatAsNumber import formatAsNumber

def formatAsCurrency(value: float) -> str:
  return "R$ " + formatAsNumber(value)