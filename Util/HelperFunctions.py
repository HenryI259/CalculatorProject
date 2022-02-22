from decimal import Decimal
import os
from time import time

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
    return func
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

def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

def floor(x):
  x=D(x)
  return x - (x%1)

def ceiling(x):
  x=D(x)
  return x + (1 - (x%1))

def decimalPlaces(x):
  x=D(x)
  i = D(0)
  while x != floor(x):
    print(f"{x}, {floor(x)}")
    original = x
    for j in range(9):
      x += original
    i += 1
  return i

def toRadians(x):
  x=D(x)
  from Util.MathFunctions import pi
  return D(x * pi / 180)

def toDegrees(x):
  x=D(x)
  from Util.MathFunctions import pi
  return D(x * 180 / pi)

def toDMS(x):
  x=D(x)
  minutes = (x%1) * 60
  seconds = (minutes%1) * 60
  return f"{floor(x)} {floor(minutes)}' {seconds}''"

def toDecimalDegrees(degrees, minutes, seconds):
  degrees, minutes, seconds = D(degrees), D(minutes), D(seconds)
  return D(degrees + (minutes / 60) + (seconds / 3600))

def toPi(x, decimalPlaces):
  x=D(x)
  from Util.MathFunctions import pi
  return f"{round(x/pi, decimalPlaces)}pi"