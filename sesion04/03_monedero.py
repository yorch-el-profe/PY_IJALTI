"""
  Funciona pero no es lo ideal ❌

class MonedaUnPeso:
  valor = 1 # Atributo de la clase MonedaUnPeso

class MonedaDosPesos:
  valor = 2

class MonedaCincoPesos:
  valor = 5

class MonedaDiezPesos:
  valor = 10

class MonedaVeintePesos:
  valor = 20

class BilleteVientePesos:
  valor = 20

class BilleteCincuentaPesos:
  valor = 50

class BilleteCienPesos:
  valor = 100

class BilleteDosCientosPesos:
  valor = 200

class BilleteQuinientosPesos:
  valor = 500

class BilleteMilPesos:
  valor = 1000

class BilleteDosMilPesos:
  valor = 2000
"""

class Moneda:
  
  """
    Constructor (__init__) es una función especial
    que se ejecuta al crear una instancia de la clase.

    Sirve para dar valores iniciales a los atributos
    de una clase.
  """
  def __init__(self, denominacion):
    # Creando un atributo al objeto llamado "valor"
    self.valor = denominacion 

  def __str__(self):
    return "Moneda de ${}".format(self.valor)

class Billete:
  def __init__(self, denominacion):
    self.valor = denominacion

  # Modificar (sobrecargar) el método __str__ del objeto
  def __str__(self):
    return "Billete de ${}".format(self.valor)

class Monedero:
  def __init__(self):
    self.morralla = []

  def agregar_dinero(self, *dineros):
    for dinero in dineros:
      self.morralla.append(dinero)

  def total_dinero(self):
    total = 0
    
    for dinero in self.morralla:
      total += dinero.valor

    return total

monedero = Monedero()

monedero.agregar_dinero(Moneda(5), Moneda(10), Billete(50))
monedero.agregar_dinero(Moneda(10))
monedero.agregar_dinero(Billete(200))
monedero.agregar_dinero(Billete(20))
monedero.agregar_dinero(Moneda(1))

print(monedero.total_dinero())