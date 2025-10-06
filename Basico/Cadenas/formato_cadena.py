#Formato de cadenas
nombre = "Roberto"
edad = 30

#f-string

mensaje = f"Hola, me llamo {nombre} y tengo { edad } años"
print(mensaje)
#metodo format 


mensaje = " Hola, me llamo {} y tengo {} años " .format (nombre, edad)
print(mensaje)


#Metodos en python 

cadena = "    hola mundo     "

# Utilizamos upper para convertir todo en minusculas
print(f"cadena original: {cadena}")

mayusculas = cadena.upper()

print (f"Cadena en mayusculas: {mayusculas} ")

# Utilizamos el metodo lower para convertir todo en minusculas 

minusculas = cadena.lower()

print (f"Cadena en minusculas: { minusculas }")

# utilizamos el metodo strip para quitar los espacios 

sin_espacios = cadena.strip()

print (f"Cadena sin espacios: {sin_espacios}")


# Metodo para saber la longitud de una cadena 
longitud = len(cadena)

print (f"La longitud de la cadenas es: {longitud}")

hola = "hola"
longitud_hola = len(hola)
print (f"La longitud de la cadena hola es: {longitud_hola}")