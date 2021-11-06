"""
  Diccionario

  Es un par de llave valor, donde la llave es una cadena de texto y el valor puede ser lo que sea.

  Sintaxis:

  { 
    "nombre": "Jorge", 
    "edad": 30, 
    "vacunado": True 
  }
"""

persona = { 
  "nombre": "Jorge", 
  "edad": 30, 
  "vacunado": True 
}

print(persona)

# Acceder a un valor en el diccionario

print(persona["nombre"])
print(persona["edad"])

# Agregar una nueva llave

persona["fecha_nacimiento"] = "10/11/1990"

# Eliminar una llave
del persona["nombre"]

print(persona)


excel = [
  { 
    "no_cuenta": "01928930982109832",
    "nombre": "Paquito",
    "cantidad": 4000
  },
  { 
    "no_cuenta": "9123908123890213",
    "nombre": "Jesus",
    "cantidad": 5000
  },
  { 
    "no_cuenta": "1238912039821398",
    "nombre": "Juanito",
    "cantidad": 30000
  }
]

deudor = excel[1]

deudor["pagado"] = True

print(deudor)

print(excel)