class Refresco:

  def __init__(self, nombre, precio, sabor, presentacion, sellos):
    self.nombre = nombre
    self.precio = precio
    self.sabor = sabor
    self.presentacion = presentacion
    self.sellos = sellos

  def __str__(self):
    return "{} de {} a solo ${}".format(self.nombre, self.sabor, self.precio)

fanta_naranja = Refresco("Fanta", 18, "Naranja", "1lt")
fanta_uva = Refresco("Fanta", 30, "Uva", "3lt")

class Papitas:

  def __init__(self, nombre, precio, sabor, tamaño, sellos):
    self.nombre = nombre
    self.precio = precio
    self.sabor = sabor
    self.tamaño = tamaño 
    self.sellos = sellos

sabritas_bolzaza = Papitas("Sabritas", 15, "Naturales", "Bolzaza")

doritos_nacho = Papitas("Doritos", 10, "Nachos", "250g")

class Cerveza:

  def __init__(self, nombre, precio, es_clara, tamaño, sellos):
    self.nombre = nombre
    self.precio = precio
    self.es_clara = es_clara
    self.tamaño = tamaño
    self.sellos = sellos

corona = Cerveza("Corona", 45, True, "Familiar")
tecate = Cerveza("Tecate Ambar", 45, False, )