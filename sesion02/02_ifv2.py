print("Ingresa un número:")

entrada = input()

numero = int(entrada)

"""
  if - else 
  Ejecuta la comparación del if
  y si no se cumple, ejecuta el else

  Sintaxis:

  if condicion :
    bloque de codigo

  elif condicion2 :
    bloque de codigo

  elif condicion3 :
    bloque de codigo

  ...

  elif condicionN :
    bloque de codigo

  else :
    bloque de codigo
"""

if numero > 0 :
  print("El número es mayor a cero")

elif numero < 0 :
  print("El número es negativo")

else : # Cualquier otro caso (es 0)
  print("El número es cero")