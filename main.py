from Modes.Calculator import calculator
from Modes.Graph import graphing
from Modes.Triangles import solveTri
from Modes.ElectronConfig import electronConfig
from Modes.Ellipsis import ellipseCalculator
from Util.MathFunctions import *
from Util.HelperFunctions import *
from decimal import Decimal
#from tkinter import *
#from tkinter import ttk
#from tkinter import font as tkfont

allModes = {
  "Calculator": calculator,
  "Graph": graphing,
  "Solve Triangle": solveTri,
  "Electron Config" : electronConfig,
  "Solve Ellipse": ellipseCalculator
}

running = True
while running:
  for choice in allModes:
    print(f"-{choice}")
  
  Input = input()
  if Input == 'exit':
    running = False
    continue

  calculating = True
  #try:
  while calculating:
    allModes[Input]()
    if input() == 'exit':
      calculating = False
  #except:
      print("Error")
