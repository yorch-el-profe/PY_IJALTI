"""
Herencia

Es "heredar" atributos y métodos de una clase padre.

Perro -> Can -> Animal

Animal:
  * Alimentan
  * Morir

Can:
  * Colmillos
  * 4 patas
  * Pelaje
  - Alimentan
  - Morir

Perros:
  * Ladran
  * Se hacen el muertito
  - Colmillos
  - 4 patas
  - Pelaje
  - Alimentan
  - Morir
"""

class Producto:

  def __init__(self, nombre, precio, sellos):
    self.nombre = nombre
    self.sellos = sellos

    if precio < 0:
      self.precio = 0
    else:
      self.precio = precio

# Papitas hereda de Producto
# Python: ClaseHijo(ClasePadre)
# ClaseHijo hereda de ClasePadre
class Papitas(Producto):

  def __init__(self, nombre, precio, sellos, sabor, tamaño):
    # super() es la referencia a la clase padre
    super().__init__(nombre, precio, sellos)
    self.sabor = sabor
    self.tamaño = tamaño

class Refresco(Producto):

  def __init__(self, nombre, precio, sellos, sabor, presentacion):
      super().__init__(nombre, precio, sellos)
      self.sabor = sabor
      self.presentacion = presentacion

class BebidaAlcoholica(Producto):

  def __init__(self, nombre, precio, sellos, gradosAlcohol):
      super().__init__(nombre, precio, sellos)
      self.gradosAlcohol = gradosAlcohol

class Cerveza(BebidaAlcoholica):

  def __init__(self, nombre, precio, sellos, gradosAlcohol, esClara):
      super().__init__(nombre, precio, sellos, gradosAlcohol)
      self.esClara = esClara

sabritas = Papitas("Sabritas", 15, 2, "Naturales", "Bolzaza")

coca = Refresco("Coca Cola", 15, 3, "Cola", "600ml")

indio = Cerveza("Indio", 13, 0, 4, False)