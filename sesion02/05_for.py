"""
  For me permite iterar sobre una estructura

  Sintaxis:

  for variable in estructura :
    bloque de codigo
"""
# Problema: Suma de los primeros 20 números

"""
contador = 1
suma = 0

while contador <= 20:
  suma += contador
  contador += 1

print("La suma de los primeros 20 números es " + str(suma))
"""
suma = 0

# range no toma en cuenta el último número
for numero in range(1, 21):
  suma += numero

print("La suma de los primeros 20 numeros es " + str(suma))

#for letra in "hola mundo":
#  print(letra)