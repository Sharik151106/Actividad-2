class CuentaBancaria:

    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta, porcentaje_interes):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0
        self.porcentaje_interes = porcentaje_interes

    def imprimir_datos(self):
        print("Nombres del titular =", self.nombres)
        print("Apellidos del titular =", self.apellidos)
        print("Número de cuenta =", self.numero_cuenta)
        print("Tipo de cuenta =", self.tipo_cuenta)
        print("Saldo =", self.saldo)

    def consignar(self, valor):
        self.saldo = self.saldo + valor
        print("Se ha consignado", valor, "en la cuenta. El nuevo saldo es", self.saldo)

    def retirar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print("Se ha retirado", valor, "de la cuenta. El nuevo saldo es", self.saldo)
        else:
            print("No se puede realizar el retiro. Saldo insuficiente.")

    def aplicar_interes(self):
        interes = self.saldo * self.porcentaje_interes / 100
        self.saldo = self.saldo + interes
        print("Se ha aplicado un interés de", self.porcentaje_interes, "%.")
        print("El nuevo saldo es", self.saldo)


cuenta = CuentaBancaria(
    "Pedro",
    "Pérez",
    "123456789",
    "AHORROS",
    2
)

cuenta.imprimir_datos()

cuenta.consignar(200000)

cuenta.consignar(300000)

cuenta.retirar(400000)

cuenta.aplicar_interes()