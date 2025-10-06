#Sistema generador de ID
from random import randint

print("Inseta el nombre del usuario")
nombre = input()
nombre_normalizado = nombre[0:1].upper()

print("Inseta el apellido del usuario")
apellido = input()
apellido_normalizado = apellido[0:1].upper()

print("Inserta año de naciomiento")
año = input()
año_normalizado = año[-2:]  # últimos dos dígitos

valor_aleatorio = str(randint(1000,9999))
ID = nombre_normalizado + apellido_normalizado + año_normalizado + valor_aleatorio

print(f"El codigo de usuario es: {ID} ")