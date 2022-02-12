from Util.Math_Functions import *

def oldRoot(number):
  num = 1
  if number < 0:
    number *= -1
    num = complexNumber(0, 1)
  upper = number
  lower = 0
  for i in range(rootPrecision):
    middle = (upper + lower) / 2
    if exponent(middle, root) > number:
      upper = middle
    elif exponent(middle, root) < number:
      lower = middle
    elif exponent(middle, root) == number:
      break
  return middle * num

def oldLn(x):
  n = 0
  while x > 1.1:
    x /= 1.1
    n += 1
  lnx = 0
  ln2 = 0
  for i in range(logPrecision):
    if i % 2 == 0:
      lnx += (exponent((x - 1), i + 1) / (i + 1))
      ln2 += (exponent((1.1 - 1), i + 1) / (i + 1))
    else:
      lnx -= (exponent((x - 1), i + 1) / (i + 1))
      ln2 -= (exponent((1.1 - 1), i + 1) / (i + 1))
  return lnx + (ln2 * n)

def hfunction1(x):
  return root(1-exponent(absoluteValue(x) - 1, 2), 2)

def hfunction2(x):
  if x < nearZero() and x > -nearZero():
    return -pi()
  else:
    return arccos(1 - absoluteValue(x)) - pi()

graph1 = graph(hfunction1, (-2, 2), (-10, 10), graphPrecision)
graph2 = graph(hfunction2, (-3.982/2, 3.982/2), (-10, 10), graphPrecision)

def drawSetGraphs():
  #graph1.plot('g')
  #graph2.plot('g')
  plt.show()