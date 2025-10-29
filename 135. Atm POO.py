class Persona:
    def __init__(self,nombre: str,apellido: str):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre: str,apellido: str, numero_cuenta: str, balance :float = 0.0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = float(balance)

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nCuenta: {self.numero_cuenta}\nBalance: Q.{self.balance:.2f}"

    def depositar(self, monto: float):
        self.balance += monto

    def retirar(self, monto: float):
        monto = float(monto)

        if monto <= self.balance:

            self.balance -= monto
            return True

        return False

def crear_cliente ():

    print("*** Creando cliente ***")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = input("Numero cuenta: ")

    return Cliente(nombre, apellido, numero_cuenta, balance = 99999)

def inicio():
    cliente = crear_cliente()
    print("*** Cliente Creado ***")
    print(cliente)

inicio()



