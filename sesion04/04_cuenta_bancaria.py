class CuentaBancaria:
  monto = 0

  def __init__(self, titular):
    self.titular = titular

  def abonar(self, montoAbono):
    self.monto += montoAbono

  def retirar(self, montoRetiro):
    if self.monto >= montoRetiro:
      self.monto -= montoRetiro

  def __str__(self):
    return "{} tiene ${}".format(self.titular, self.monto)


mi_cuenta = CuentaBancaria("Paquito Perez")

mi_cuenta.abonar(3000)

#print(mi_cuenta)

mi_cuenta.retirar(500)
mi_cuenta.abonar(300)
mi_cuenta.retirar(1000)

#print(mi_cuenta)

# ---------------------------------


cuenta_juan = CuentaBancaria("Juan Solis")

cuenta_juan.abonar(5000)
cuenta_juan.abonar(100)

# Se sobreescribe el monto previamente abonado
cuenta_juan.monto = 300000

print(cuenta_juan)