##Dado un texto, debes:

##Convertir todo a minúsculas.

##Eliminar signos de puntuación básicos (.,!?)

##Contar cuántas veces aparece cada palabra.

##Imprimir las 3 palabras más frecuentes junto con su cantidad.

texto = "Python es genial. Python es poderoso! Y python es divertido?"

texto = texto.lower()

resultado = texto.replace(".", "")
resultado = resultado.replace(",", "")
resultado = resultado.replace("!", "")
resultado = resultado.replace("?", "")

palabras = resultado.split()

frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

ordenado = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

for palabra, cantidad in ordenado[:3]:
    print(f"{palabra}: {cantidad}")
