class TarjetaDebito:

  def __init__(self, titular, saldoInicial):
    self.titular = titular
    self.saldo = saldoInicial

  def depositar(self, cantidad):
    self.saldo += cantidad

  def retirar(self, cantidad):
    if self.saldo >= cantidad:
      self.saldo -= cantidad

class TarjetaJoven(TarjetaDebito):

  def __init__(self, titular, saldoInicial, edad):
      super().__init__(titular, saldoInicial)
      self.edad = edad

class TarjetaPremium(TarjetaDebito):

  def __init__(self, titular):
      super().__init__(titular, 10000)

class TarjetaCredito(TarjetaDebito):

  def __init__(self, titular, limiteCredito):
      super().__init__(titular, 0)
      self.limiteCredito = limiteCredito

debito = TarjetaDebito("Paquito Perez", 100)
credito = TarjetaCredito("Juan Espinoza", 40000)