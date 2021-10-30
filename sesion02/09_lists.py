"""
  Lista permite almacenar una cantidad indeterminada de valores, pudiendo acceder a su posición e incluso modificando sus valores

  Sintaxis:
  variable = [1,2,3,4,5,5]

  lista_vacia1 = list()
  lista_vacia2 = []
"""

mi_primer_lista = [1,1,2,2,3,3,True,"Hola Mundo", (6,7)]

print(mi_primer_lista)

# Acceder a los valores de una lista es igual que en una tupla

lista_numeritos = [10, 20, 30, 40]
#                  0    1   2   3

print("El elemento en la posición 2 es: ", lista_numeritos[2])

# Modificar los valores por posición

lista_numeritos[3] = 45

# print(lista_numeritos)

"""
Al igual que los conjuntos puedo agregar nuevos elementos hasta el final de la lista
Notación: lista.append(50)

Existe otra manera utilizando la concatenación de listas

listaA = [1,2,3]
listaA = [0] + listaA -> [0, 1, 2, 3]
lista = listaA + [4]  -> [0, 1, 2, 3, 4]

La + concatena listas y regresa una nueva lista con los elementos mezclados
"""

lista_numeritos.append(50)

lista_numeritos = [100] + lista_numeritos + [1000, 2000, 3000]

# [100, 10, 20, 30, 45, 50, 1000, 2000, 3000]
#   0   1   2   3   4   5    6      7    8
print(lista_numeritos)

# Insertar un número entre el 45 y 50
# Insertando el 0 en la posición 4
lista_numeritos.insert(5, 0)

print(lista_numeritos)

# Eliminar la posición 4 (osea el 45)
del lista_numeritos[4]

print(lista_numeritos)