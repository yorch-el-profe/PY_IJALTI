"""
Un módulo es una serie de funciones que pueden utilizar dentro de un archivo.

Importar un archivo
"""

# 1. Importar todas las funciones de un archivo bajo el nombre del mismo archivo

import calculadora

#print(calculadora.suma(1,2,3,4,5,6))
#print(calculadora.multiplicacion(5,4,1,2,3,4,5))

# 2. Importar únicamente lo que me interesa del archivo

from calculadora import residuo

#print(residuo(2,2))

# 3. Importar todo pero sin estar usando nombre.funcion()

#from calculadora import *

#print(suma(1,2,3,4,5))


# Usando import dentro de una funcion
def f():
  from calculadora import suma
  return suma(1,2)

print(f())