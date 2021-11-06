"""
Módulo que exporta funciones relacionadas a operaciones que hace una calculadora.
"""

def suma(*numeros):
  """
  La función suma recibe como parámetro una cantidad indeterminada de números y regresa la suma de todos ellos.
  """
  total = 0
  
  for numero in numeros:
    total += numero

  return total

def resta(*numeros):
  """
  La función resta recibe como parámetro una cantidad indeterminada de números y regresa la resta de todos ellos.
  """
  total = 0
  
  for numero in numeros:
    total -= numero

  return total

def multiplicacion(*numeros):
  """
  La función multiplicacion recibe como parámetro una cantidad indeterminada de números y regresa la multiplicación de todos ellos.
  """
  total = 1

  for numero in numeros:
    total *= numero

  return total

def residuo(a, b):
  """
  La función residuo regresa el modulo de a con b
  """
  return a % b

# D R Y (Don't Repeat Yourself)