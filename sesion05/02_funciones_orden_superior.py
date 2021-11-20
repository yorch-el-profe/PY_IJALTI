"""
Funciones de Orden Superior (High Order Functions)

En Python las funciones regresan funciones
y reciben funciones como parámetro
"""

def funcion_a():
  print("Ejecutando la función a")

def funcion_b(f):
  print("Ejecutando la funcion b")
  f()

# funcion_b(funcion_a)

numeritos = [-1, 19, 0, 2, -56, 29, 30, 10, 5, 3, 5, 6, 18, 11, -20, 3]

# Solución Chafa

"""
def quitar_negativos(lista):
  aux = []

  for elemento in lista:
    if elemento >= 0:
      aux.append(elemento)

  return aux

def quitar_impares(lista):
  aux = []

  for elemento in lista:
    if elemento % 2 == 0:
      aux.append(elemento)

  return aux

def quitar_positivos(lista):
  aux = []

  for elemento in lista:
    if elemento < 0:
      aux.append(elemento)

  return aux
"""

# Versión buena ✔

def filtrar(lista, condicion):
  aux = []

  for elemento in lista:
    if condicion(elemento):
      aux.append(elemento)

  return aux

def quitar_negativos(elemento):
  return elemento >= 0

def quitar_impares(elemento):
  return elemento % 2 == 0

def quitar_positivos(elemento):
  return elemento < 0

print( filtrar(numeritos, quitar_negativos) )

print( filtrar(numeritos, quitar_impares) )

print( filtrar(numeritos, quitar_positivos) )