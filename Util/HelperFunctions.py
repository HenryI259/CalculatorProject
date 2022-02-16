from decimal import Decimal

def D(x):
  try:
    return Decimal(str(x))
  except:
    return x

def isNumber(x):
  from Util.MathFunctions import complexNumber
  if isinstance(x, int) or isinstance(x, float) or isinstance(x, Decimal) or isinstance(x, complexNumber):
    return True
  else:
    for char in x:
      if char not in '-.123456789':
        return False
    return True

def keepBetween(x, min, max):
  if x > max:
    return max
  elif x < min:
    return min

def maxInList(givenList):
  max = 0
  for i in givenList:
    if i > max:
      max = i
  return max

def maxIndexInList(givenList):
  max = 0
  maxIndex = 0
  for i, item in givenList:
    if i > max:
      max = item
      maxIndex = i
  return maxIndex

def minInList(givenList):
  min = 0
  for i in givenList:
    if i < min:
      min = i
  return min

def minIndexInList(givenList):
  min = 0
  minIndex = 0
  for i, item in givenList:
    if i < min:
      min = item
      minIndex = i
  return minIndex

def orderList(givenList):
  newList = []
  for number in givenList:
    index = 0
    for newNumber in newList:
      if number > newNumber:
        index += 1
    newList.insert(index, number)
  return newList