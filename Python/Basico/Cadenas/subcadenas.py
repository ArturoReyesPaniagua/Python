#Manejo de subcadenas

cadena  = "Hola mundo"

subcadena = cadena [0:4]

print(f"Imprimimos la subcadena hola: {subcadena} ")

subcadena_mundo = cadena[5:10]
print(f"Imprimimos la subcadena de mundo: {subcadena_mundo}")

posicion = cadena.find("mundo")
print (f"imprime la posicion en la que se encuentra la cadena de mundo que es: {posicion}")

subcadena_prueba = cadena[posicion:10]

print (f"la subcadena mundo por el metodo find y subcadena es: {subcadena_prueba}")

nueva_cadena = cadena.replace("mundo", "a todos")

print(f"la nueva cadena con remplazar es: {nueva_cadena}")

nueva_cadena2 = cadena.replace("Hola", "Adios")
print (nueva_cadena2)

datos = "Rodrigo, 19, Mexico"
lista = datos.split(",")
print (lista)