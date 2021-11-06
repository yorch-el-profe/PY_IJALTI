from re import search

texto = "Anita lava la tina"
busqueda = "lava"

resultado = search(busqueda, texto)

print("Posición donde empieza la palabra lava:", resultado.start())
print("Posición donde termina la palabra lava:", resultado.end())