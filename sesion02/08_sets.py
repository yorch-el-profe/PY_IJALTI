"""
Conjuntos son una colección de elementos que no se repiten y no tienen un orden en específico.

Sintaxis:

variable = {1, 2, 3}
conjunto_vacio = set()
"""

mi_primer_conjunto = {1,1,1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6}

# print(mi_primer_conjunto)

"""
  En Python tengo acceso a las operaciones de:

  1. Union: La mezcla de todos los elementos de ambos conjuntos
  Notación: conjuntoA.union(conjuntoB)

  2. Intersección: Los elementos que tienen en común
  Notación: conjuntoA.intersection(conjuntoB)

  3. Diferencia: Los elementos que están en A, pero no en B
"""

conjuntoA = {1, 2, 3, 4, 5, 6}
conjuntoB = {2, 4, 6, 8, 10}

print(conjuntoA, conjuntoB)

# Union {1, 2, 3, 4, 5, 6, 8, 10}
print("Union:",conjuntoA.union(conjuntoB))

# Intersección {2, 4, 6}
print("Intersección:", conjuntoA.intersection(conjuntoB))

# Diferencia A - B {1, 3, 5}
print("Diferencia A - B:", conjuntoA.difference(conjuntoB))

# Diferencia B - A {8, 10}
print("Diferencia B - A:", conjuntoB.difference(conjuntoA))

# Agregar un nuevo elemento al conjunto
conjuntoC = set() # Conjunto vacío

print(conjuntoC)

conjuntoC.add(1)
conjuntoC.add(2)
conjuntoC.add(3)
conjuntoC.add(1)

print(conjuntoC)