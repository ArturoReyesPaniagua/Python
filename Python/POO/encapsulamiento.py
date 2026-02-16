class Coche:
    def __init__ (self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    

    def conducir(self):
        print(f'''Conduciendo el coche:
              Marca: {self._marca}
              Modelo: {self._modelo}
              Color: {self._color}''')
    
    def set_marca(self, marca):
        self._marca = marca
    def get_marca(self):
        return self._marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_modelo(self):
        return self._modelo

    def set_color(self, color):
        self._color = color
    def get_color(self):
        return self._color
        
        ###Programa principal

if __name__ == "__main__":
    Coche1 = Coche("Honda", "Yaris", "Negro")
    Coche1.conducir()

    Coche1.set_marca("Ford")
    marca_coche = Coche1.get_marca()
    print(f"La marca actual del vehiculo es: {marca_coche}") 

    Coche1.set_color("Rosa")
    Coche1.conducir()