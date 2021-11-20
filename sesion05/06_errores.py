def division(a, b):
  return a / b

"""
Sintaxis:

try:
  bloque de codigo
  potencialmente con errores
except:
  bloque de codigo
  manejando el error
finally:
  bloque de codigo
  que se ejecuta SIEMPRE

Cuando el código no tiene ningún error
el bloque "except" jamás es ejecutado.
"""
"""
try:
  print("Ingresa el primer numero:")
  x = int(input())

  print("Ingresa el segundo numero:")
  y = int(input())

  resultado = division(x, y)

  print("El resultado es:", resultado)
except:
  print("Ocurrio un error, intente más tarde")
finally:
  print("Terminando programa")
"""

# TypeError: Operando con tipos equivocados
# NameError: Variables con existen
# ZeroDivisionError: Intento dividir entre 0
# ValueError: Intento convertir un cadena en numero

class CustomError(Exception):
  pass

try:
  print("Ingresa el primer numero:")
  x = int(input())

  if x > 100:
    raise CustomError()

  print("Ingresa el segundo numero:")
  y = int(input())

  if y > 100:
    raise CustomError()

  resultado = division(x, y)

  print("El resultado es:", resultado)
except ZeroDivisionError:
  print("Error, no se puede dividir entre 0")

except ValueError:
  print("El número ingresado es inválido")

except CustomError:
  print("El numero no puede ser mayor a 100")