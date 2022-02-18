from decimal import Decimal
import os

def D(x):
  try:
    return Decimal(str(x))
  except:
    if isinstance(x, str):
      try:
        return stringToComplex(x)
      except:
        return x
    else:
      return x

def stringToComplex(z):
  from Util.MathFunctions import complexNumber
  if '+' in z:
    zsplit = z.split('+')
    return complexNumber(Decimal(zsplit[0]), Decimal(zsplit[1][0:-1]))
  elif '-' in z and '-' != z[0]:
    zsplit = z.split('-')
    return complexNumber(Decimal(zsplit[0]), -Decimal(zsplit[1][0:-1]))
  elif 'i' in z:
    return complexNumber(0, Decimal(z[0:-1]))
  else:
    return Decimal(z)

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

def readCache(func, args):
    try:
      f = open(f'Cache/{func.__name__}', 'r')
    except:
      return None
    text = f.readlines()
    for line in text:
      splitLine = line.split('|')
      answer = splitLine.pop(-1)
      #print(splitLine)
      #print(map(str,args))
      if splitLine == list(map(str, args)):
          f.close()
          return D(answer)
    f.close()

def writeCache(func, args, answer):
    if readCache(func, args) == None:
        f = open(f'Cache/{func.__name__}', 'a')
        arguments = '|'.join(map(str, args))
        f.write(f'{arguments}|{answer}\n')
        f.close()

def cacheHandling(func):
    def handle(*args, **kwargs):
      if len(kwargs) == 0:
        cacheAnswer = readCache(func, args)
        if cacheAnswer == None:
          answer = func(*args)
          writeCache(func, args, answer)
          return D(answer)
        else:
          return D(cacheAnswer)
      else:
        return func(*args, **kwargs)
    return handle

def clearCache(func=None):
  if func == None:
    for file in os.listdir('Cache'):
      os.remove(os.path.join('Cache', file))
  try:
    os.remove(f'Cache/{func}')
  except:
    pass