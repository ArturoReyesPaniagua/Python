class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona
        nombre: {self.nombre}
        apellido: {self.apellido}''')


if __name__ == "__main__":
    persona1 = Persona("Arturo", "Reyes")
    persona1.mostrar_persona()
