from constants import *
from decimal import Decimal
from Util.HelperFunctions import *

class complexNumber():
  def __init__(self, r, i):
    self.real = D(r)
    self.imaginary = D(i)
    
  # addition override
  def __add__(self, other):
    if False:
      print(f"{str(self)} + {str(other)}")
    if isinstance(other, complexNumber):
      r = self.real + other.real
      i = self.imaginary + other.imaginary
    else:
      r = self.real + D(other)
      i = self.imaginary
    return complexNumber(r, i).fixI()

  __radd__ = __add__

  # subtraction overrides
  def __sub__(self, other):
    if debug:
      print(f"{str(self)} - {str(other)}")
    if isinstance(other, complexNumber):
      r = self.real - other.real
      i = self.imaginary - other.imaginary
    else:
      r = self.real - D(other)
      i = self.imaginary
    return complexNumber(r, i).fixI()

  def __rsub__(self, other):
    if debug:
      print(f"{str(other)} - {str(self)}")
    if isinstance(other, complexNumber):
      r = other.real - self.real
      i = other.imaginary - self.real
    else:
      r = D(other) - self.real
      i = self.imaginary * D(-1)
    return complexNumber(r, i).fixI()

  # multiplication overrides
  def __mul__(self, other):
    if False:
      print(f"{str(self)} * {str(other)}")
    if isinstance(other, complexNumber):
      r = (self.real * other.real) - (self.imaginary * other.imaginary)
      i = (self.real * other.imaginary) + (self.imaginary * other.real)
    else:
      r = self.real * D(other)
      i = self.imaginary * D(other)
    return complexNumber(r, i).fixI()

  __rmul__ = __mul__

  # division overrides
  def __truediv__(self, other):
    if False:
      print(f"{str(self)} / {str(other)}")
    if isinstance(other, complexNumber):
      a = self.real
      b = self.imaginary
      c = other.real
      d = other.imaginary
      r = ((a * c) + (b * d)) / (exponent(c, 2) + exponent(d, 2))
      i = ((b * c) - (a * d)) / (exponent(c, 2) + exponent(d, 2))
    else:
      r = self.real / D(other)
      i = self.imaginary / D(other)
    return complexNumber(r, i).fixI()

  def __floordiv__(self, other):
    if debug:
      print(f"{str(self)} // {str(other)}")
    if isinstance(other, complexNumber):
      a = self.real
      b = self.imaginary
      c = other.real
      d = other.imaginary
      r = ((a * c) + (b * d)) // (exponent(c, 2) + exponent(d, 2))
      i = ((b * c) - (a * d)) // (exponent(c, 2) + exponent(d, 2))
    else:
      r = self.real // D(other)
      i = self.imaginary // D(other)
    return complexNumber(r, i).fixI()

  def __rtruediv__(self, other):
    if debug:
      print(f"{str(other)} / {str(self)}")
    c = self.real
    d = self.imaginary
    a = other
    r = (a * c) / (exponent(c, 2) + exponent(d, 2))
    i = (D(-1) * a * d) / (exponent(c, 2) + exponent(d, 2))
    return complexNumber(r, i).fixI()

  # greater than and less than overrides
  def __lt__(self, other):
    if isinstance(other, complexNumber):
      return self.radius() < other.radius()
    else:
      return self.radius() < other

  def __le__(self, other):
    if isinstance(other, complexNumber):
      return self.radius() <= other.radius()
    else:
      return self.radius() <= other

  def __gt__(self, other):
    if isinstance(other, complexNumber):
      return self.radius() > other.radius()
    else:
      return self.radius() > other

  def __ge__(self, other):
    if isinstance(other, complexNumber):
      return self.radius() >= other.radius()
    else:
      return self.radius() >= other

  # rounds complex number
  def __round__(self, number=0):
    if debug:
      print(f"Rounding {str(self)} to {str(number)} decimal places")
    r = round(self.real, number)
    i = round(self.imaginary, number)
    return complexNumber(r, i).fixI()

  # returns radius for polar form
  def radius(self):
    if debug:
      print(f"Radius of {str(self)}")
    return D(root(exponent(self.real, 2) + exponent(self.imaginary, 2), 2))

  # returns the angle for polar form
  # uses pi, arctan
  def angle(self):
    if debug:
      print(f"Angle of {str(self)}")
    if self.real == 0:
      if self.imaginary > 0:
        return D(pi / 2)
      elif self.imaginary < 0:
        return D(-pi / 2)
    elif self.real > 0:
      return D(arctan(self.imaginary/self.real))
    elif self.real < 0:
      if self.imaginary > 0:
        return D(arctan(self.imaginary/self.real) + pi)
      elif self.imaginary < 0:
        return D(arctan(self.imaginary/self.real) - pi)

  def fixI(self):
    if (self.imaginary < exponent(10, -numPrecision) and self.imaginary > -exponent(10, -numPrecision)):
      return D(self.real)
    elif (self.real < exponent(10, -numPrecision) and self.real > -exponent(10, -numPrecision)):
      return complexNumber(0, self.imaginary)
    else:
      return self
      
  # string override
  def __str__(self):
    if self.imaginary == 0 and self.real == 0:
      return "0"
    elif self.real == 0:
      if self.imaginary == 1:
        return "i"
      elif self.imaginary == -1:
        return "-i"
      else:
        return str(self.imaginary) + "i"
    elif self.imaginary == 0:
      return str(self.real)
    elif self.imaginary == 1:
      return f"{self.real} + i"
    elif self.imaginary == -1:
      return f"{self.real} - i"
    elif self.imaginary > 0:
      return f"{self.real} + {self.imaginary}i"
    elif self.imaginary < 0:
      return f"{self.real} - {self.imaginary * -1}i"
  
# returns the factorial of a number
def factorial(x):
  if False:
      print(f"Factorial({str(x)})")
  return D(piFunction(1, x, lambda x: x))

# returns the sin of a number
# uses int exponents, factorial
@cacheHandling
def sin(x, precision=trigPrecision):
  # uses a taylor series
  if debug:
      print(f"Sin({str(x)})")
  x = D(x)
  if isinstance(x, Decimal):
      if x > 10 or x < 10:
          x = x%(2*pi)
  return D(sigmaFunction(0, precision, lambda n, x: exponent(x, ((n*2)+1)) / factorial((n*2)+1) * exponent(-1, n), x))

# returns the cos of a number
# uses int exponents, factorial
@cacheHandling
def cos(x, precision=trigPrecision):
  if debug:
      print(f"Cos({str(x)})")
  x = D(x)
  if x == 0:
    return 1
  if isinstance(x, Decimal):
      if x > 10 or x < 10:
        x = x%(2*pi)
  # uses a taylor series
  return D(sigmaFunction(0, precision, lambda n, x: exponent(x, (n*2)) / factorial(n*2) * exponent(-1, n), x))

# returns tan of a number
# uses sin, cos
@cacheHandling
def tan(x):
  if debug:
      print(f"Tan({str(x)})")
  x=D(x)
  try:
    return D(sin(x) / cos(x))
  except ZeroDivisionError:
    return Decimal('Infinity')

# returns the csc of a number
# uses sin
@cacheHandling
def csc(x):
  if debug:
      print(f"Csc({str(x)})")
  x=D(x)
  try:
    return D(1/sin(x))
  except ZeroDivisionError:
    return Decimal('Infinity')

# returns the sec of a number
# uses cos
@cacheHandling
def sec(x):
  if debug:
      print(f"Sec({str(x)})")
  x=D(x)
  try:
    return D(1/cos(x))
  except ZeroDivisionError:
    return Decimal('Infinity')

# returns the cot of a number
# uses sin, cos
@cacheHandling
def cot(x):
  if debug:
      print(f"Cot({str(x)})")
  x = D(x)
  try:
    return D(cos(x) / sin(x))
  except ZeroDivisionError:
    return Decimal('Infinity')

# returns the arcsin of a number
# uses ln, root, int exponents
@cacheHandling
def arcsin(x, amount=1):
  if debug:
      print(f"Arcsin({str(x)})")
  x = D(x)

  arcsin = complexNumber(0,-1) * ln(root(1-exponent(x, 2),2) + (complexNumber(0, 1) * x))

  if amount == 1:
      return arcsin
  else:
      answerList = []
      n=0
      extraPi = 0

      for i in range(amount):
        if i%2 == 0:
          answerList.append(arcsin + (2 * pi * n) + extraPi)
          arcsin *= -1
          extraPi += pi
          extraPi = absoluteValue(extraPi) * -1
        else:
          answerList.append(arcsin - (2 * pi * n) + extraPi)
        if (i - 1) % 4 == 0:
          n += 1
      return orderList(answerList)

# returns the arccos of a number
# uses arcsin, pi
@cacheHandling
def arccos(x, amount=1):
  if debug:
      print(f"Arccos({str(x)})")
  # uses inverse of cos
  x = D(x)
  
  arccos = D((pi/2) + complexNumber(0,1) * ln(root(1-exponent(x, 2),2) + (complexNumber(0, 1) * x)))

  if amount == 1:
      return arccos
  else:
      answerList = []
      n=0
      extraPi = 0

      for i in range(amount):
        if i%2 == 0:
            answerList.append(arccos + (2 * pi * n))
            arccos *= -1
        else:
            answerList.append(arccos - (2 * pi * n))
        if (i - 1) % 4 == 0:
            n += 1
        return orderList(answerList)

# returns the arctan of a number
# uses int exponents, factorial
@cacheHandling
def arctan(x, amount=1, precision=arctanPrecision):
  if debug:
      print(f"Arctan({str(x)})")
  x=D(x)
  # uses a taylor series
  arctan = D(sigmaFunction(0, precision, lambda n, x: D(exponent(2, 2*n) * exponent(factorial(n), 2) / factorial(2*n + 1)) * D(exponent(x, 2*n + 1)/exponent(1 + exponent(x, 2), n+1)), x))

  if amount == 1:
      return arctan
  else:
      answerList = []
      n=0

      for i in range(amount):
        if i % 2 == 0:
            answerList.append(arctan - pi * n)
        else:
            n += 1
            answerList.append(arctan + pi * n)
      return orderList(answerList)

@cacheHandling
def cis(x):
  x = D(x)
  return cos(x) + complexNumber(0, 1) * sin(x)

# returns the log of a number
# uses ln
@cacheHandling
def log(x, base):
  if debug:
      print(f"Log base {str(base)} of {str(x)}")
  x = D(x)
  return D(ln(x) / ln(base))

# returns the ln of a number
# uses complex number's radius/angle, exponent, nearZero
@cacheHandling
def ln(x, precision=logPrecision):
  if debug:
      print(f"ln({str(x)})")
  x = D(x)
  if isinstance(x, complexNumber):
    # finds the ln of a complex number in polar form
    num = 0
    radius = x.radius()
    if radius == 1:
        r = 0
    else:
        while radius > e:
            radius /= e
            num += 1
        n = 1/(radius-1)
        ln = sigmaFunctionX(0, precision, lambda i, n: 1/(((i * 2) + 1) * exponent((2*n)+1, ((i * 2) + 1))), n)
        r = D((2*ln) + num)
    return complexNumber(r, x.angle())

  else:
    negative = False
    if x < 0:
        negative = True
        x *= -1
    if x == 1:
        if negative:
            return complexNumber(0, pi)
        else:
            return 0
    num = 0
    while x > e:
        x /= e
        num += 1
    n = 1/(x-1)
    ln = sigmaFunction(0, precision, lambda i, n: 1/(((i * 2) + 1) * exponent((2*n)+1, ((i * 2) + 1))), n)
    if negative:
        return complexNumber((2*ln) + num, pi)
    else:
        return D((2*ln) + num)

# returns a number raised to another number
# uses sin, cos, ln
@cacheHandling
def exponent(number, power):
  number, power = D(number), D(power)
  if debug and number != 10:
      print(f"{str(number)} to the {str(power)}")
  if power == 0 and number != 0:
    return 1

  elif number == 0:
    return 0

  elif number == 1:
    return 1

  # uses sin, cos, ln
  elif isinstance(power, complexNumber):
    if isinstance(number, complexNumber):
      # complex number to a complex number
      # uses a changed eulars equation
      c = power.real
      d = power.imaginary
      return D(exponent(number, c) * cis(d * ln(number)))
    
    else:
      # number to a complex number
      # uses a changed eulars equation
      r = exponent(number, power.real) * cos(power.imaginary * ln(number))
      i = exponent(number, power.real) * sin(power.imaginary * ln(number))
      return complexNumber(r, i)

  elif power == int(power):
    # number to an int
    # multiplies the number n times
    power = int(power)
    negative = False
    if power < 0:
      power *= -1
      negative = True
    original = number
    for i in range(power - 1):
      number *= original
    if negative:
      return D(1 / number)
    else:
      return D(number)
  
  elif isinstance(power, Decimal):
    # uses sin, cos, ln
    if isinstance(number, complexNumber):
      # complex number to a float
      # uses a changed eulars equation
      return D(cis(complexNumber(0, -1) * power * ln(number)))

    # uses python exponents
    else:
      return D(cis(complexNumber(0, -1) * power * ln(number)))

# returns a number to a root
# uses exponents
def root(number, root=2):
  if debug:
      print(f"Root {str(root)} of {str(number)}")
  number,root = D(number),D(root)
  return D(exponent(number, 1/root))

#returns the absolute value of x
def absoluteValue(x):
  x=D(x)
  if x < 0:
    return -x
  else:
    return x

def sigmaFunction(start, end, function, otherVariable=None):
  answer = 0
  if otherVariable == None:
      for n in range(int(end)-int(start)+1):
        answer = D(answer) + D(function(n+start))
  else:
      otherVariable = D(otherVariable)
      for n in range(end-start+1):
        answer = D(answer) + D(function(n+start, otherVariable))
  return answer

def piFunction(start, end, function, otherVariable=None):
  answer = 1
  if otherVariable == None:
      for n in range(end-start+1):
        answer = D(answer) * D(function(n+start))
  else:
      otherVariable = D(otherVariable)
      for n in range(end-start+1):
        answer = D(answer) * D(function(n+start, otherVariable))
  return answer

def lim(func, approachedNum=0, *args):
    try:
        return func(approachedNum, *args)
    except:
        return func(approachedNum+nearZero, *args)

def derivative(func):
    def fprime(x):
        return lim(lambda h, x: (func(x+h) - func(x))/h, 0, x)
    return fprime

def defIntegral(lower, upper, func, precision=integralPrecision):
    return sigmaFunction(0, precision, lambda n, dx: func((n * dx) + lower) * dx, (upper-lower)/precision)

# eulars number
e = D(sigmaFunction(0, ePrecision, lambda n: 1/factorial(n)))

# pi
pi = D((426880 * root(10005, 2)) / sigmaFunction(0, piPrecision, lambda i: (factorial(6*i)*(13591409 + (545140134 * i))) / (factorial(3*i)*exponent(factorial(i),3) *exponent(-262537412640768000, i))))

# a number close to zero
# uses int exponents
nearZero = D(exponent(10, zeroPrecision * -1))