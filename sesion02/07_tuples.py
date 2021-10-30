"""
  1. Tupla

  Permite almacenar valores CONSTANTES (textos, booleanos, numéros, etc) y TIENE UN TAMAÑO FIJOOOOOOOOOOOOOOOO!!!!!!

  Sintaxis:

  variable = (elem1, elem2, elem3, elem4, elem5, ..., elemN)

  Nota: Para tener una tupla de 1 elemento, hay que agregar al final una ,

  Ejemplo:

  tupla = (1,)

  Sin la coma (,) Python lo reconoce como un número
"""

mi_primer_tupla = (1,2,3)

tupla_un_elemento = (4,)

# print(mi_primer_tupla)

#print(tupla_un_elemento)
#print(type(tupla_un_elemento))


tupla_diferentes_elementos = (1, True, "Hola mundo", 0, -1, 4 + 3j)
#                             0    1         2       3   4     5

print(tupla_diferentes_elementos)

"""
  Para acceder a un valor dentro de una tupla se utiliza la "posición" donde se encuentra.

  Las posiciones o índices comienzan desde el 0

  Con [n] accedemos a la posición n

  tupla[3] -> Accediendo a la posición 3 o el 4to elemento
"""

print("El elemento en la posición 1 es: " + str(tupla_diferentes_elementos[1]))
print("El 5to elemento de la tupla es: " + str(tupla_diferentes_elementos[4]))

print("El tamaño de la tupla es: " + str(len(tupla_diferentes_elementos)))


tuplaA = (1,2)
tuplaB = (3,4,5)

tuplaC = tuplaA + tuplaB # (1, 2, 3, 4, 5)

print(tuplaC)