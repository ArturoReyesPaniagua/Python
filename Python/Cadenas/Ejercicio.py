print("### Promedio de calificaciones ###")

calificaciones = [] ##Creamos lista
##Solicitamos cuantas calificaciones vamos a querer y lo convertimos a entero
numero_calificaciones = int(input("¿Cuántas calificaciones deseas promediar? "))
##iteramos el numero_calificaciones
for indice in range(numero_calificaciones):
    ##pedimos las calificaciones
    calificacion = float(input(f"¿Cuál es el valor de la calificación {indice + 1}? "))
    ##la calificacion se almacena
    calificaciones.append(calificacion)

suma = 0
for calificacion in calificaciones:
    suma += calificacion

promedio = suma / numero_calificaciones

print(f"El promedio es: {promedio}")
