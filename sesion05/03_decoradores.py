"""
Decoradores

Son funciones que se ejecutan ANTES de ejecutar
cualquier función.

Sintaxis:

@decorador
def mi_function():
  bloque de codigo
"""

# Los decoradores son funciones
# que tienen que regresar una nueva función
def decorador_hello_world(f):
  print("Ejecutando el decorador")

  def nuevo_saluda():
    print("Ejecutando la nueva implemetación de saluda")
    f()

  return nuevo_saluda


@decorador_hello_world
def saluda():
  print("Hola Como Estas?")


saluda()