from Util.Math_Functions import *
from Other.Helper_Functions import *

def encrypt(char, key1, key2):
    num = ord(char) / 3
    num = D(complexNumber(0,-1) * ln(root(1-exponent(num, 2),2)+ complexNumber(0, num)))
    if isinstance(num, complexNumber):
      r = num.real+ D(key1)
      i = num.imaginary + D(key2)
    else:
      r = num + key1
      i = key2
    return (r, i)

def decrypt(nums, key1, key2):
  num = complexNumber(nums[0] - key1, nums[1] - key2)
  finalNum = 0 
  for i in range(50):
    n = (i*2) + 1
    finalNum += exponent(num, n) / factorial(n) * exponent(-1, i)
  char = chr(round(finalNum * 3))
  return char

def encrypter(message, key1, key2):
    newMessage = []
    for char in message:
      newNums = encrypt(char, D(key1), D(key2))
      newMessage.append(str(newNums[0]))
      newMessage.append(str(newNums[1]))
    return ' '.join(newMessage)

def decrypter(numList, key1, key2):
    newNums = []
    tuple = []
    for num in numList:
      tuple.append(D(num))
      if len(tuple) > 1:
        newNums.append(tuple)
        tuple = []
    return ''.join((map(lambda x: decrypt(x, D(key1), D(key2)), newNums)))

def encryption():
  whatDo = input('Do you want to encrypt or decrypt a message')
  
  if whatDo == 'encrypt':
    message = input("What is the message")
  elif whatDo == 'decrypt':
    nums = input("What are the numbers").split()
  else:
    print("Error")
  
  key1 = input('What is key 1')
  key2 = input('What is key 2')
  
  if whatDo == 'encrypt':
      print(encrypter(message, key1, key2))
  if whatDo == 'decrypt':
      print(decrypter(nums, key1, key2))

