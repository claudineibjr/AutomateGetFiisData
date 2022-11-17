def printTickerTitle(ticker: str):
  repetitionNumber = 3

  title = 'Ticker: ' + ticker
  timesToRepeatHiphenOnTitle = len(title) + repetitionNumber + 1 + repetitionNumber * repetitionNumber + 1
  print('-' * timesToRepeatHiphenOnTitle)
  print('-' * repetitionNumber + ' ' + title + ' ' + '-' * repetitionNumber * repetitionNumber)
  print('-' * timesToRepeatHiphenOnTitle)