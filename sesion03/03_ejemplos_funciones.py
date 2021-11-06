"""
1. Crear una función que reciba como parámetro el nombre de una persona y lo salude de la siguiente forma:

"Hola, [nombre de la persona]"
"""

"""
Los parámetros de una función son como variables que se pueden acceder únicamente dentro de la función.
"""
def saluda(nombre):
  print("Hola, " + nombre)

#saluda("Enrique")
#saluda("Maria")
#saluda("Gabriel")

"""
2. Crear una función que regrese la suma de dos números. 
Suposición: los dos números son números enteros.
"""

"""
"return" va a regresar un valor fuera de la función y finaliza la ejecución de la misma.

Las funciones sólo pueden regresar 1 valor a la vez.
"""
def suma(numero1, numero2):
  return numero1 + numero2

#print(suma(1, 2))
#print(suma(-1, 0))
#print(suma(3.1416, 5))

"""
3. Crear una función que convierta los minutos en segundos

3 -> 3 * 60 = 180
"""
def minutos_a_segundos(minutos):
  return minutos * 60

#print(minutos_a_segundos(3))
#print(minutos_a_segundos(60))

"""
4. Crear una función que reciba una cantidad INDETERMINADA DE NÚMEROS
y regrese la suma de todos
"""

# Versión chafa
# Aceptar como parámetro una lista
def sumaInfinitaLista(lista):
  total = 0

  for numero in lista:
    total += numero

  return total


# print(sumaInfinitaLista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 30, 40, 50]))

# Versión buena
# * marca una cantidad indeterminada de parámetros
def sumaInfinita(*numeros):
  total = 0

  for numero in numeros:
    total += numero

  return total

#print(sumaInfinita(100, 40, 10, 22, 2, 3, 2, 12, 3, 5, 5, 6, 3, 2, 234))

"""
5. Crear una función que reciba una cantidad indeterminada de parámetros
y una operacion matemática a ejecutar.
"""
# keyword param  ->  param = valor
def math(*numeros, op):
  if op == "+":
    return sumaInfinita(*numeros)
  else:
    return 0

def mathv2(op, *numeros):
  if op == "+":
    return sumaInfinita(*numeros)
  else:
    return 0

# Usando keyword params
print(math(1, 2, 3, 4, 5, 4, 5, 6, 67, 78, 8, 8, 9, 9, op="+"))

# Sin usar keyword params
#print(mathv2('+', 1,2,3,4,5,4,5,6,67,78,8,8,9,9))
