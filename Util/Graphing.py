from Util.Math_Functions import *
from Other.Helper_Functions import D
from constants import *
import os
import tempfile
os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()
import matplotlib.pyplot as plt


class graphFunction():
  def __init__(self, function, betweenX, betweenY, graphPrecision):
    self.function = function
    self.graphStart = D(betweenX[0])
    self.graphEnd = D(betweenX[1])
    self.miny = D(betweenY[0])
    self.maxy = D(betweenY[1])
    self.graphPrecision = D(graphPrecision)
    self.x = []
    self.y = []

  def findValues(self):
    graphLength = self.graphEnd - self.graphStart
    step = graphLength / self.graphPrecision
    for i in range(int(self.graphPrecision) + 1):
      x = (i * step) + self.graphStart
      try:
        y = self.function(x)
      except ZeroDivisionError:
        continue
      if not isinstance(x, complexNumber) and not isinstance(y, complexNumber) and y < self.maxy and y > self.miny:
        self.x.append(x)
        self.y.append(y)
        print(i)

  def plot(self, color='b'):
    self.findValues()
    plt.plot(self.x, self.y, color)

class graphDerivative():
  def __init__(self, function, betweenX, betweenY, graphPrecision):
    self.function = function
    self.graphStart = D(betweenX[0])
    self.graphEnd = D(betweenX[1])
    self.miny = D(betweenY[0])
    self.maxy = D(betweenY[1])
    self.graphPrecision = graphPrecision
    self.x = []
    self.y = []

  def findValues(self):
    graphLength = self.graphEnd - self.graphStart
    step = graphLength / self.graphPrecision
    for i in range(int(self.graphPrecision) + 1):
      x = (i * step) + self.graphStart
      try:
        y = (self.function(x+nearZero)-self.function(x))/nearZero
      except ZeroDivisionError:
        continue
      if not isinstance(x, complexNumber) and not isinstance(y, complexNumber) and y < self.maxy and y > self.miny:
        self.x.append(x)
        self.y.append(y)

  def plot(self, color='g'):
    self.findValues()
    plt.plot(self.x, self.y, color)

class graphIntegral():
  def __init__(self, function, betweenX, betweenY, graphPrecision):
    self.function = function
    self.graphStart = D(betweenX[0])
    self.graphEnd = D(betweenX[1])
    self.miny = D(betweenY[0])
    self.maxy = D(betweenY[1])
    self.graphPrecision = D(graphPrecision)
    self.x = []
    self.y = []
    self.C = 0

  def findValues(self):
    graphLength = self.graphEnd - self.graphStart
    step = graphLength / self.graphPrecision
    y=0
    tempX = []
    tempY = []
    for i in range(int(self.graphPrecision) + 1):
      x = (i * step) + self.graphStart
      try:
        y += self.function(x+(step/2)) * step
      except:
        continue
      if x > 0 and self.C == 0 and not isinstance(y, complexNumber):
        self.C = -y

      tempX.append(x)
      tempY.append(y)
      if isinstance(y, complexNumber):
        y = y.real

    for i in range(len(tempY)):
      tempY[i] = tempY[i] + self.C
      if not isinstance(tempX[i], complexNumber) and not isinstance(tempY[i], complexNumber) and tempY[i] < self.maxy and tempY[i] > self.miny:
        self.x.append(tempX[i])
        self.y.append(tempY[i])

  def plot(self, color='r'):
    self.findValues()
    plt.plot(self.x, self.y, color)

def drawGraph(givenGraph):
  if graphDebug:
    givenGraph.findValues()
    for i in range(len(givenGraph.y)):
      print(f"{givenGraph.x[i]}, {givenGraph.y[i]}")
    if len(givenGraph.y) == 0:
      print("empty")
  
  if isinstance(givenGraph, graphIntegral):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_visible(False)
    #ax.spines['bottom'].set_position('')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticklabels([])
  else:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
  
  givenGraph.plot()
  plt.show()