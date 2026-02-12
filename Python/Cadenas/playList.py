print ("!!!PlayList de Canciones!!!")

#Creamos una lista vacia
lista_reproduccion = []
numero_canciones = int(input("Cuantas canciones deseas agregar "))

# Iteramos cada elemento de la lista para agregar unn nuevo elemento

for indice in range(numero_canciones):
    cancion = input(f"Proporciona la cancion {indice + 1}")
    lista_reproduccion.append(cancion)
    
#Empezamos a agregar canciones
lista_reproduccion.append("In the end")
lista_reproduccion.append("Counting stars")
lista_reproduccion.append("Debi Tirar Mas Fotos")
lista_reproduccion.append("Altanera")


for cancion in lista_reproduccion:
    print(cancion)
print("\n")
## Ordenar alfabeticamente las canciones
print("Ordenando alfabeticamnte")

lista_reproduccion.sort()

##Imprimir la lista ordenada
for cancion in lista_reproduccion:
    print(cancion)