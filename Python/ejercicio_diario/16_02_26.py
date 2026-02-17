class Cuenta:
    def __init__(self, dinero):
        self.dinero = dinero
    
    def depositar(self, cantidad):
        self.dinero += cantidad

    def retirar(self, cantidad):
        self.dinero -= cantidad

    def consultar(self):
        print(f"El dinero en la cuenta es: {self.dinero}")


def menu(cuenta_obj):
    while True:

        print('''
Menu, pulse la opcion que requiera 
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir
''')

        option = int(input("Seleccione opción: "))

        match option:
            case 1:
                cuenta_obj.consultar()

            case 2:
                deposito = int(input("Cuanto dinero desea depositar: "))
                cuenta_obj.depositar(deposito)
                cuenta_obj.consultar()

            case 3:
                retiro = int(input("Cuanto dinero desea retirar: "))
                dinero_en_cuenta = cuenta_obj.consulta()
                if dinero_en_cuenta > retiro:
                    cuenta_obj.retirar(retiro)
                    cuenta_obj.consultar()
                else: 
                    print("el saldo no es suficiente para el retiro")

            case 4:
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción no válida")


if __name__ == "__main__":
    mi_cuenta = Cuenta(100)
    menu(mi_cuenta)
2