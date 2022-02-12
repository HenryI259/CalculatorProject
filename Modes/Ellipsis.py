from Util.Math_Functions import *
from Other.Helper_Functions import *

def ellipseCalculator():
  print("Give the values to this equation")
  print("ax^2 + bx + cy^2 + dy + e = 0")
  a = input('a=')
  b = input('b=')
  c = input('c=')
  d = input('d=')
  e = input('e=')
  vertical = False
  fociX1 = 0
  fociY1 = 0
  fociX2 = 0
  fociY2 = 0
  h, k, a, b, xd, yd = ellipseSolver(D(a),D(b),D(c),D(d),D(e))
    
  if xd < yd:
    vertical = True
  c = root(exponent(a, 2) - exponent(b, 2), 2)
  if vertical:
    fociX1, fociX2 = h, h
    fociY1, fociY2 = k + c, k - c
  else:
    fociX1, fociX2 = h + c, h - c
    fociY1, fociY2 = k, k

  print(f"(x - {h})^2 / {xd} + (y - {k})^2 / {yd} = 1")
  print(f"h={h}")
  print(f"k={k}")
  print(f"a={a}")
  print(f"b={b}")
  print(f"c={c}")
  print(f"Center: ({h}, {k})")
  print(f"Foci: ({fociX1}, {fociY1}), ({fociX2}, {fociY2})")
  if vertical:
    print("The major axis is vertical")
  else:
    print("The major axis is horizontal")

def ellipseSolver(a,b,c,d,e):
  h = -b/(2*a)
  k = -d/(2*c)
  den = ((exponent(b, 2) * c) + (exponent(d, 2) * a) - (4*a*c*e)) / (4*a*c)
  xd = den / a
  yd = den / c
  a = max(root(xd, 2), root(yd, 2))
  b = min(root(xd, 2), root(yd, 2))
  return h, k, a, b, xd, yd