class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        return (f"Cliente: {self.nombre}\n Apellido {self.apellido}\nCuenta: {self.cuenta}\nBalance: {self.balance}")

    def depositar(self, monto_depositado ):
        self.balance += monto_depositado
        print("Deposito realizado")

    def retirar(self, monto_retirada):
        if self.balance >= monto_retirada:
            self.balance -= monto_retirada
            print("Retiro realizado")
        else:
            print("No disponible")

def crear_cliente():
    nombre_cl = input("Ingrese Nombre: ")
    apellido_cl = input("Ingrese Apellido: ")
    cuenta = input("Ingrese Cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, cuenta,9000)# Creacion del objeto o instancia
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = ''
    while opcion != 'S':
        print("Elige: Depositar(D), Retirar(R),o Salir(S) ")
        opcion = input().upper()
        if opcion == 'D':
            monto_depositado = int(input("Ingrese monto de depositar: "))
            mi_cliente.depositar(monto_depositado)
        elif opcion == 'R':
            monto_retirada = int(input("Ingrese monto de retirada: "))
            mi_cliente.retirar(monto_retirada)

        print(mi_cliente)

    print("Gracias por usar el banco Python")

inicio()



