class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    ## Sobre escribir metodo

    def __str__(self):
        return f'''
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. memoria = {super.__str__(self)}
        '''

##codigo principal

persona1 = Persona("Ana", "Martinez")

print(persona1) ## llama automaticamente al metodos __str__ desde el print()