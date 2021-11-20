def filtrar(lista, condicion):
  aux = []

  for elemento in lista:
    if condicion(elemento):
      aux.append(elemento)

  return aux