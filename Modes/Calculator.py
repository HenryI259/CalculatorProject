from Util.Graphing import *
from Util.MathFunctions import *
from Util.HelperFunctions import *

functionDict = {
  "sin": sin,
  "cos": cos,
  "tan": tan,
  "csc": csc,
  "sec": sec,
  "cot": cot,
  "arcsin": arcsin,
  "arccos": arccos,
  "arctan": arctan,
  "cis": cis,
  "log": log,
  "ln": ln,
  "|": absoluteValue
}

constantDict = {
  "e": e,
  "pi": pi,
}                                                              

def solve(slist, x):
  deleteList = []
  step = 0
  while len(slist) > 1:
    for i in range(len(slist)):
      if slist[i] == '-':
        slist[i] = -1
    
    for i in range(len(slist)):
      if isinstance(slist[i], str):
        if 'i' == slist[i][-1] and slist[i] not in functionDict and slist[i] not in constantDict:
          slist[i] = slist[i][0:-1]
          slist[i] = complexNumber(0, D(slist[i]))

    for i in range(len(slist)):
      if slist[i] == 'x':
        slist[i] = x
        
    for i in range(len(slist)):
      for constant in constantDict:
        if slist[i] == constant:
          slist[i] = constantDict[constant]
              
    for i in range(len(slist)):
      if slist[i] == '!':
        slist[i-1] = factorial(D(slist[i-1]))
        deleteList.append(i)
        break
    for i in deleteList:
      slist.pop(i - step)
      step += 1
    deleteList = []
    step = 0
    
    for i in range(len(slist)):
      for func in functionDict:
        if slist[i] == func:
          slist[i] = functionDict[func](D(slist[i+1]))
          deleteList.append(i+1)
          break
    for i in deleteList:
      slist.pop(i - step)
      step += 1
    deleteList = []
    step = 0

    for i in range(len(slist)):
      if slist[i] == '^':
        slist[i-1] = exponent(D(slist[i-1]),D(slist[i+1]))
        deleteList.append(i)
        deleteList.append(i+1)
        break
    for i in deleteList:
      slist.pop(i - step)
      step += 1
    deleteList = []
    step = 0

    for i in range(len(slist)):
      if i != len(slist) - 1:
        if isNumber(slist[i]) and isNumber(slist[i+1]):
          slist[i] = D(slist[i])*D(slist[i+1])
          deleteList.append(i+1)
          break
    for i in deleteList:
      slist.pop(i - step)
      step += 1
      deleteList = []
      step = 0
    
    for i in range(len(slist)):
      if slist[i] == '*':
        slist[i-1] = D(slist[i-1])*D(slist[i+1])
        deleteList.append(i)
        deleteList.append(i+1)
        break
      if slist[i] == '/':
        slist[i-1] = D(slist[i-1])/D(slist[i+1])
        deleteList.append(i)
        deleteList.append(i+1)
        break
    for i in deleteList:
      slist.pop(i - step)
      step += 1
    deleteList = []
    step = 0

    for i in range(len(slist)):
      if slist[i] == '+':
        slist[i-1] = D(slist[i-1])+D(slist[i+1])
        deleteList.append(i)
        deleteList.append(i+1)
        break
      if slist[i] == '-':
        slist[i-1] = D(slist[i-1])-D(slist[i+1])
        deleteList.append(i)
        deleteList.append(i+1)
        break
    for i in deleteList:
      slist.pop(i - step)
      step += 1
    deleteList = []
    step = 0

  return slist[0]

def solveString(formula, x):
  formulaList = []
  solvingList = []
  replacedNumbers = []
  inPar = False
  num = ''
  func = ''
  if formula == '':
    return ''
  for char in formula:
    if char == 'i':
      if num != "":
        num += char
        continue
      elif func != "":
        func += char
        continue
        
    if char in '0123456789.':
      num += char
      continue
    else:
      if num != '':
        formulaList.append(num)
        num = ''

    if char in 'abcdefghjklmnopqrstuvwyz':
      func += char
      continue
    else:
      if func != '':
        formulaList.append(func)
        func = ''

    if char == " ":
      continue

    formulaList.append(char)

  if num != '':
    formulaList.append(num)
  elif func != '':
    formulaList.append(func)

  while '(' in formulaList and ')' in formulaList: 
    i = 0
    for item in formulaList:
      if item == '(':
        solvingList = []
        replacedNumbers = []
        inPar = True
      elif item == ')':
        formulaList[replacedNumbers[-1] + 1] = solve(solvingList, x)
        step = 0
        replacedNumbers.insert(0, replacedNumbers[0] - 1)
        for num in replacedNumbers:
          formulaList.pop(num - step)
          step += 1
        inPar = False
        break
      elif inPar:
        solvingList.append(item)
        replacedNumbers.append(i)
      i += 1
    replacedNumbers = []

  return solve(formulaList, x)

def solveFormula(string):
  print(f"The answer is {solveString(string, None)}")

def findx(x):
  pass

formulaChoices = {
  "solve" : solveFormula,
  "find x(unfinished)": findx,
}

def calculator():
  functionInput = input("Input: ")

  print("What do you want to do with this input")
  for choice in formulaChoices:
    print(f"-{choice}")
    
  formulaChoices[input()](functionInput)