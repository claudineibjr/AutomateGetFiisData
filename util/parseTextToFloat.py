import re

def parseTextToFloat(text: str) -> float:
  specialCharacters = re.sub('\d|[,]', '', text)
  for character in specialCharacters:
    text = text.replace(character, "")
  
  text = text.replace(",", ".")

  return float(text)