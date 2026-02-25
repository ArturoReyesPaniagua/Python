numeros = range (1, 30+1)
pares = []
impares = []
sum_pares = 0
sum_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

for par in pares:
    sum_pares = sum_pares + par

for impar in impares:
    sum_impares = sum_impares + impar

print(f"los numeros pares son: {pares}")
print(f"Los numeros impares son: {impares}")
print(f"la cantidad de pares es {len(pares)}")
print(f"La cantidad de impares es{len(impares)}")
print(f"La suma de los impares es: {sum_impares}")
print(f"la suma de los pares: {sum_pares}")