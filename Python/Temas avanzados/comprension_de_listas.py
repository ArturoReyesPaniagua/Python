# Filtrar solo los numeros pares y generar una nueva lista con estos valores

numeros = range(1, 10 + 1)  # Del 1 al 10
numeros_pares = []

# Iteramos cada elemento
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(f"Numeros pares del 1 al 10: {numeros_pares}")


## Sintaxis: nueva_lista = [expresion for elemento in iterable if condition]

numeros_pares = [numero for numero in numeros if numero%2 ==0]
print(f"Numeros pares del 1 al 10: {numeros_pares}")