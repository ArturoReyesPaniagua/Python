string = " Hola Mundo "
string = string.lower()
string = string.replace(" ","")
vocales = {"a","e","i","o","u"}
numero_vocales = 0

for letra in string:
    if letra in vocales:
        numero_vocales = numero_vocales + 1

print(f"La frase es: {string}")
print (numero_vocales)

lista = [1,2,2,3,3,3,4]
