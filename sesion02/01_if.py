print("Ingresa un número:")

# input() captura un texto del usuario
entrada = input()

# type(variable o valor) regresa el tipo
print(type(entrada))

# Casting: Convertir de un tipo A a un tipo B
# str (cadena de texto) -> int (número)
# int(variable)
numero = int(entrada)

print(type(numero))

"""
  Sintaxis:

  if condicion booleana :
    bloque de código
    linea
    linea
    linea
    linea
    linea

  linea <-- NO PERTENECE AL BLOQUE DE CODIGO

"""

if numero > 0 :
  print("El número es mayor a cero")

if numero < 0 :
  print("El número es negativo")

# = asignación
# a = 0 (a la variable "a" se le asigna el valor 0)

# == comparación
# a == 0 (¿será que a es exactamente igual a 0?)

if numero == 0 :
  print("El número es cero")