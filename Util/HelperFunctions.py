from decimal import Decimal

def D(x):
  try:
    return Decimal(str(x))
  except:
    try:
      return stringToComplex(x)
    except:
      return x

def stringToComplex(z):
  from Util.MathFunctions import complexNumber
  zsplit = z.split()
  r = D(zsplit[0])
  i = D(zsplit[2][0:-1])
  if zsplit[1] == '-':
    i *= -1
  return complexNumber(r,i)

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

def readCache(func, x):
    f = open('cache.txt', 'r')
    text = f.readlines()
    for line in text:
        splitLine = line.split('|')
        if splitLine[0] == func.__name__ and D(splitLine[1]) == D(x):
            f.close()
            return D(splitLine[2])
    f.close()

def writeCache(func, x, answer):
    if readCache(func, x) == None:
        f = open('cache.txt', 'a')
        f.write(f'{func.__name__}|{x}|{answer}\n')
        f.close()

def cacheHandling(func):
    def handle(x, *args, **kwargs):
        if len(args) + len(kwargs) == 0:
          cacheAnswer = readCache(func, x)
          if cacheAnswer == None:
              answer = func(x, *args, **kwargs)
              writeCache(func, x, answer)
              return D(answer)
          else:
              return D(cacheAnswer)
        else:
          return func(x, *args, *kwargs)
    return handle