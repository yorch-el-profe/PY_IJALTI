# Operadores numéricos

# Suma (+)
print(1 + 2)

# Resta (-)
print(5 - 6)

# Multiplicación (*)
print(8 * 8)

# División (/)
print(6 / 8)

# Potencia x^n
print(2 ** 4)

# Módulo (Residuo)
print(20 % 8) # 4
print(20 / 8) # 2.5

# Concatenación (Suma de cadenas de texto)
# Pegar cadenas de texto (2 o más)

print("El modulo que estoy tomando es: " + "Python")

operacion = 1 + 3

# Solo se pueden concatenar cadenas de texto
# print("La suma de 1 + 3 es: " + operacion) ❌

# Alternativa para concatenar cosas 
# que no son texto

# 1. Usar str() para convertir un valor a cadena de texto
print("[usando str()] La suma de 1 + 3 es: " + str(operacion))

# 2. Usar format (formatear un texto)
print("[usando format] La suma de 1 + 3 es: {}".format(operacion))

nombre = "Paquito"
apellido = "Sanchez"
edad = 29

print("[str] Hola, mi nombre es " + nombre + " " + apellido + " y tengo " + str(edad) + " años")

print("[format] Hola, mi nombre es {} {} y tengo {} años".format(nombre, apellido, edad))


# Operadores Lógicos

operacion_and = True and True # True
operacion_and2 = False and True # False

operacion_or = True or True # True
operacion_or2 = False or False # False
operacion_or3 = True or False # True

operacion_neg = not True # False

# Otros operadores (Comparación >, <, >=, <=, ==, !=)

num1 = 10
num2 = 20

print(num1 > num2) # False
print(num1 <= num2) # True
print(num1 == num2) # False
print(num1 != num2) # True