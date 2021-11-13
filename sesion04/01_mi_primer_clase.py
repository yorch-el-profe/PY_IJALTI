"""
Clase

Una clase es una plantilla que define un objeto. Las clases pueden tener propiedades (atributos) y acciones (métodos).

Sintaxis:

class NombreClase:
  bloque código

Pascal Case:
  anita lava la tina
  AnitaLavaLaTina

Camel Case:
  anita lava la tina
  anitaLavaLaTina
"""
class MiPrimerClase:
  pass

class Calculadora:

  def suma(self, a, b):
    return a + b

  def resta(self, a, b):
    return a - b

  def multiplicacion(self, a, b):
    return a * b

"""
Objeto:

Un objeto es una referencia en memoria de una clase. También se le conoce como una "instancia de la clase"

Sintaxis:

class MiClase:
  bloque de código

variable = MiClase()
"""

calcu = Calculadora()

# print(calcu) Dirección de memoria

"""
Notación punto (.)

Sirve para acceder a los atributos o métodos de un objeto.

Sintaxis:

  objeto.atributo
  objeto.metodo()
"""
resultado = calcu.suma(1,2)
print(resultado)

# Format es un método de clase String (texto)
print(    "Hola me llamo, {}".format("Jorge")       )