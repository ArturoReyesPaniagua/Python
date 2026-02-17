class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def decir_nombre(self):
        print(f"Mi nombre es: {self.nombre}")
    
    def hacersonido(self):
        print("meeee,meeeee")


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)   # llama al constructor del padre
        self.ruido = "Guau guau"

    def ladrar(self):
        print(f"El perro hace {self.ruido}")


class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.ruido = "Miau Miau"

    def maullar(self):
        print(f"El animal hace {self.ruido  }")




animal1 = Animal("Anunaki")
animal1.decir_nombre()
animal1.hacersonido()
perro1 = Perro("Roberto")
perro1.decir_nombre()
perro1.ladrar()
gato1 = Gato("Momo")
gato1.decir_nombre()
gato1.hacersonido()
gato1.maullar()

