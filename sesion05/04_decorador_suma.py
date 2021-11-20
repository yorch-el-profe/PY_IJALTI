from filtrado import filtrar

numeritos = [1, 53, 298, -2, 293, 9, 0, 13, 4, 3, 12, -12, -40, 50, -10]


def quitar_negativos(elemento):
  return elemento >= 0

def quitar_doscientos(elemento):
  return elemento < 200

def quitar_impares(elemento):
  return elemento % 2 == 0

"""
numeritos_filtrado = filtrar(numeritos, quitar_negativos)
numeritos_filtrado2 = filtrar(numeritos_filtrado, quitar_doscientos)
numeritos_filtrado3 = filtrar(numeritos_filtrado2, quitar_impares)

print(numeritos_filtrado3)
print( suma_lista(numeritos_filtrado3) )
"""

def filtrar_negativos(suma_lista_v1):

  def suma_lista_v2(lista):
    nueva_lista = filtrar(lista, quitar_negativos)
    return suma_lista_v1(nueva_lista)

  return suma_lista_v2

def filtrar_doscientos(suma_lista_v1):

  def suma_lista_v2(lista):
    nueva_lista = filtrar(lista, quitar_doscientos)
    return suma_lista_v1(nueva_lista)

  return suma_lista_v2

def filtrar_impares(suma_lista_v1):

  def suma_lista_v2(lista):
    nueva_lista = filtrar(lista, quitar_impares)
    return suma_lista_v1(nueva_lista)

  return suma_lista_v2

@filtrar_negativos
@filtrar_doscientos
@filtrar_impares
def suma_lista(lista):
  aux = 0

  for elemento in lista:
    aux += elemento
  
  return aux

print(suma_lista(numeritos))