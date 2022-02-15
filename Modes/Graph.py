from Util.MathFunctions import *
from Util.Graphing import *
from Modes.Calculator import *

graphChoices = {
  "Graph Function": graphFunction,
  "Graph Derivative": graphDerivative,
  "Graph Integral": graphIntegral
}

def graphing():
  function = input("f(x)=")
  for choice in graphChoices:
    print(f"-{choice}")
  choice = input()
  boundx = input("What are the side bounds").split(',')
  if boundx == ['']:
    boundx = (-10, 10)
      
  boundy = input("What are the top and bottem bounds").split(',')
  if boundy == ['']:
    boundy = (-10, 10)
    
  func = lambda x: solveString(function, x)
  graphInput = graphChoices[choice](lambda x: solveString(function, x), boundx, boundy, graphPrecision)
  drawGraph(graphInput)