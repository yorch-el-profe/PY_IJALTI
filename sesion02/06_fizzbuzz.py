"""
  Problema:

  Dados los números del 1 al 100, se tiene los siguientes casos:

  1. Si el número es divisible entre 3, imprimir en pantalla "fizz"

  2. Si el número es divisible entre 5, imprimir en pantalla "buzz"

  3. Si el número es divisible entre 3 y 5, imprimir en pantalla "fizzbuzz"

  1
  2
  Fizz (3)
  4
  Buzz (5)
  Fizz (6)
  7
  8
  Fizz (9)
  Buzz (10)
  11
  Fizz (12)
  13
  14
  FizzBuzz (15)
"""

for numero in range(1, 101):

  if numero % 3 == 0 and numero % 5 == 0 :
    print("FizzBuzz")
    
  elif numero % 3 == 0 :
    print("Fizz")

  elif numero % 5 == 0 :
    print("Buzz")

  else :
    print(numero)