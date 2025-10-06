from random import randint

numero_aleatorio = randint(0,100)
print (f"el numero aleatorio generado es: {numero_aleatorio}")

print("inserte el rango menor")
num_menor = int(input())

print("inserte el rango mayor")
num_mayor = int(input())

numero_random = randint(num_menor, num_mayor)
if (num_menor <= num_mayor):
    print(f"el numero aleatorio entre {num_menor} y el numero mayor {num_mayor} es: {numero_random}")
else:
    print("Error el numero menor es mayor al menor")