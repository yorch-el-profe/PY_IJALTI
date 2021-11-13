"""
Encapsulación

Es ocultar el acceso a métodos y/o atributos para evitar la modificación del comportamiento de mi objeto
"""
class CuentaBancaria:
  """
    Poner al principio doble guión bajo (__) hace que el atributo no sea accesible (PRIVADO)

    Los atributos PRIVADOS sólo son accesibles/modificables dentro de la propia clase
  """
  __monto = 0

  def __init__(self, titular):
    self.__titular = titular

  def abonar(self, montoAbono):
    self.__monto += montoAbono

  def retirar(self, montoRetiro):
    if self.__monto >= montoRetiro:
      self.__monto -= montoRetiro

  def __str__(self):
    return "{} tiene ${}".format(self.__titular, self.__monto)

cuenta_juan = CuentaBancaria("Juan Solis")
cuenta_juan.abonar(5000)
cuenta_juan.abonar(100)

# cuenta_juan.__titular = "Chuchito"
# print(cuenta_juan.__monto)
# cuenta_juan.__monto = 300000

print(cuenta_juan)