#practica final de la parte de cadenas

nombre = "Arturo Reyes"
empresa = "Google"
dominio = ".com"

nombre_sin_espacios = nombre.strip()
print(nombre_sin_espacios)
minusculas = nombre_sin_espacios.lower()
print(minusculas)
nombre_normalizado = minusculas.replace(" ",".")
compuesto = nombre_normalizado + "@" + empresa + dominio
print(f"{nombre_normalizado}@{empresa}{dominio}")
print(f"El correo electronico es el siguiente: {compuesto}")
