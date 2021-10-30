print("El precio del helado es de $40")

print("Selecciona el topping de tu preferencia")

print("1. Fresas (+ $10)")
print("2. Cobertura de chocolate + ($20)")
print("3. Polvito de oreo (+ $8)")
print("4. Nada")

entrada = input()
opcion = int(entrada)

precio = 40

if opcion == 1 :
  precio = precio + 10 # precio += 10
  
elif opcion == 2 :
  precio += 20

elif opcion == 3 :
  precio += 8

elif opcion == 4 :
  precio += 0

else :
  print("Topping inválido")

print("El precio de tu helado es $" + str(precio))