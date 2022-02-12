from Util.Graphing import *
from Util.Math_Functions import *
from Other.Helper_Functions import *
from Modes.Calculator import *

def checkTriangle(sides, angles):
  if '' not in sides:
    if float(sides[0]) > (float(sides[1]) + float(sides[2])) or float(sides[1]) > (float(sides[0]) + float(sides[2])) or float(sides[2]) > (float(sides[1]) + float(sides[0])):
      return False

  if sides == ['', '', '']:
    return False

  if '' not in angles:
    if round(angles[0] + angles[1] + angles[2], 5) != round(pi, 5):
      return False

  return True

def solveTriangle(sides, angles):
  sinOverSide = 0
  sideOverSin = 0
  while '' in sides or '' in angles:
    for i in range(3):
      if angles[i] != '':
        angles[i] = toNumber(angles[i])
      if sides[i] != '':
        sides[i] = toNumber(sides[i])

    for i in range(3):
      knownAngles = []
      knownSides = []
      totalAngles = 0
      for angle in angles:
        if angle != '':
          knownAngles.append(angle)
          totalAngles += angle
      for side in sides:
        if side != '':
          knownSides.append(side)

      if sides[i] != '' and angles[i] != '':
        sinOverSide = sin(angles[i]) / sides[i]
        sideOverSin = sides[i] / sin(angles[i])

      if angles[i] != '':
        totalAngles += angles[i]

      if len(knownSides) < 3:
        if sides[i] == '' and angles[i] != '':
          if sideOverSin != 0:
            sides[i] = sin(angles[i]) * sideOverSin
          elif len(knownSides) == 2:
            sides[i] = exponent(exponent(knownSides[0], 2) + exponent(knownSides[1], 2) - (2*knownSides[0]*knownSides[1]*cos(angles[i])), 0.5)

      if len(knownAngles) < 3 and angles[i] == '':
        if len(knownAngles) == 2:
          angles[i] = pi - totalAngles
          continue

        if sides[i] != '':
          if sinOverSide != 0:
            angles[i] = arcsin(sides[i]*sinOverSide)
            continue

        if len(knownSides) == 3:
          knownSides.remove(sides[i])
          angles[i] = arccos((exponent(knownSides[0], 2) + exponent(knownSides[1], 2) - exponent(sides[i],2))/(2 * knownSides[0] * knownSides[1]))
          continue

  area = sides[0] * sides[2] * sin(angles[1]) / 2
  return sides, angles, area

def solveTri():
  sides = []
  angles = []
  print("Input known sides, if unknown leave blank")
  sides.append(solveString(input("a="), None))
  sides.append(solveString(input("b="), None))
  sides.append(solveString(input("c="), None))
  print("Input known angles, if unknown leave blank")
  angles.append(solveString(input("A="), None))
  angles.append(solveString(input("B="), None))
  angles.append(solveString(input("C="), None))
  for i in range(3):
    if angles[i] != '':
      angles[i] = int(angles[i])*pi/180
  if checkTriangle(sides, angles):
    sides, angles, area = solveTriangle(sides, angles)
    for i in range(3):
      angles[i] = angles[i]*180/pi
    print(f"a={sides[0]}")
    print(f"b={sides[1]}")
    print(f"c={sides[2]}")
    print(f"A={angles[0]}")
    print(f"B={angles[1]}")
    print(f"C={angles[2]}")
    print(f"The Area is {area}")
  else:
    print("This triangle cannot be solved")