class CuentaBancaria:
    def __init__(self,saldo):
        self.saldo=saldo
    def ver_saldo(self):
        return self.saldo
    def depositar(self,monto):
        self.saldo+=monto
    def retirar(self,monto):
        if monto>self.saldo:
            print('No hay suficiente saldo')
        else:
            self.saldo-=monto
    
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(cuenta.ver_saldo())