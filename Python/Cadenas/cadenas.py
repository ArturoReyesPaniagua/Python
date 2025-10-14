#Manejo de cadenas en python 

#Creamos cadena
cadena = "Hola mundo"
#imprimimos la cadena 
print (cadena)
#creamos una variable y le asignamos el valor de el primer digito de la cadena
primer_caracter = cadena[0]
#imprimimos el primer caracter para coroborar
print(primer_caracter)

#Caracteres especiales
print ("Hola \n Mundo") #salto de linea
print ("\"Te quiero\" ") #comillas
print ("Tabulador \t puesto \t aqui") #Tabulador

#***Concatenacion***
cadena1 = "hola"
cadena2 = "mundo"

concatenacion = cadena1 + " " + cadena2
print(concatenacion)

#con metodo joint 
concatenacion2 = "".join ([cadena1," ", cadena2," ", "Cualquier otra cadena"])
print (concatenacion2)