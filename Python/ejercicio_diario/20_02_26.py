def limpiar_texto(cadena):
    cadena = cadena.lower()  #hace minusculas todas las palabras
    nueva = ""  #Crea 

    for caracter in cadena:
        if caracter.isalnum():  
            nueva += caracter

    return nueva


def invertir(cadena):
    inversa = ""
    longitud = len(cadena) - 1

    while longitud >= 0:
        inversa += cadena[longitud]
        longitud -= 1

    return inversa


def palindromo(cadena):
    cadena = limpiar_texto(cadena)
    inversa = invertir(cadena)

    if cadena == inversa:
        return True
    else:
        return False