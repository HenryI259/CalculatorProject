from decimal import Decimal
import time

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

def readCache(func, x):
    f = open('cache.txt', 'r')
    text = f.readlines()
    for line in text:
        splitLine = line.split()
        if splitLine[0] == func.__name__ and splitLine[1] == str(x):
            f.close()
            return Decimal(splitLine[2])
    f.close()

def writeCache(func, x, answer):
    if readCache(func, x) == None:
        f = open('cache.txt', 'a')
        f.write(f'{func.__name__} {x} {answer}\n')
        f.close()

def cacheHandling(func):
    def handle(x):
        cacheAnswer = readCache(func, x)
        if cacheAnswer == None:
            answer = func(*args, **kwargs)
            writeCache(func, x, answer)
            return answer
        else:
            return cacheAnswer
    return handle

def cache(func):
    """
    A decorator to cache/memoize func's restults
    
    Parameters
    ----------
    func: callable
      The function being decorated
    
    Returns
      func: callable
        The decorated function
    """
    # Create a dictionary to store results
    cache = {}  # this will be stored in closure because it is nonlocal
    
    def wrapper(*args, **kwargs):
        # Unpack args and kwargs intp a tuple to be used as dict keys
        keys = (tuple(args) + tuple(kwargs.keys()))
        # If not seen before
        if keys not in cache:
            # Store them in cache
            cache[keys] = func(*args, **kwargs)
        # Else return the recorded result
        return cache[keys]
    
    return wrapper

def timer(func):
    """
    A decorator to calculate how long a function runs.
    
    Parameters
    ----------
    func: callable
      The function being decorated.
      
    Returns
    -------
    func: callable
      The decorated function.
    """
    def wrapper(*args, **kwargs):
        # Start the timer
        start = time.time()
        # Call the `func`
        result = func(*args, **kwargs)
        # End the timer
        end = time.time()
        
        print(f"{func.__name__} took {round(end - start, 4)} "
                "seconds to run!")
        return result
    return wrapper