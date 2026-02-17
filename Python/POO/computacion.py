class DispositivoEntrada:
    id_dispositivo_entrada = 0

    def __init__(self, marca, tipo_entrada):
        DispositivoEntrada.id_dispositivo_entrada += 1
        self.id_dispositivo_entrada = DispositivoEntrada.id_dispositivo_entrada
        self.marca = marca
        self.tipo_entrada = tipo_entrada


class Raton(DispositivoEntrada):
    id_raton = 0

    def __init__(self, marca, tipo_entrada):
        Raton.id_raton += 1
        self.id_raton = Raton.id_raton
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f""" 
        La marca es: {self.marca}
        El tipo de entrada es {self.tipo_entrada}
        El numero de raton es: {self.id_raton}
        
        """


class Teclado(DispositivoEntrada):
    id_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.id_teclado += 1
        self.id_teclado = Teclado.id_teclado
        super().__init__(marca, tipo_entrada)
   
    def __str__(self):
        return f""" 
        La marca es: {self.marca}
        El tipo de entrada es {self.tipo_entrada}
        El numero de raton es: {self.id_raton}
        """

# Prueba
raton1 = Raton("Logitech", "USB")
raton2 = Raton("HP", "Bluetooth")

print(raton1)
print(raton2)
