def analizar(cadena):
    cadena = cadena.lower()
    
    # eliminar signos
    for signo in ".,;:!?":
        cadena = cadena.replace(signo, "")
    
    palabras = cadena.split()
    
    conteo = {}
    
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    
    # encontrar la más repetida
    max_palabra = ""
    max_numero = 0
    
    for palabra in conteo:
        if conteo[palabra] > max_numero:
            max_numero = conteo[palabra]
            max_palabra = palabra
    
    print(conteo)
    print(f"La palabra más repetida es: {max_palabra} ({max_numero} veces)")