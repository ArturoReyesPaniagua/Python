print("*** Operadores de asignacion***")
numero = 5
print(f"El valor del numero es: {numero}")
numero = 10
print(f"El valor del numero es: {numero}")
cadena = "Saludos desde python"
print(f"Valor de la cadena: {cadena}")

print("***Operadores Multiples***")

#Sintaxis de Asignacion Multiple
Variable1, Variable2 = 12, 12
a,b,c = 10, "Saludos" , 14.5
print(f" el valor de la variable 1 es: {Variable1} y el de la variable 2 {Variable2}")
print(f"imprimir a : {a} imprimir b:{b} y el valor de c: {c}")


#Asiganacion Encadenada
##permite asignar el mismo valor a multiples variables

#Sintaxis de asignacion encadenada 
variable1 = variable2 = "valor"

#Ejemplo
a=b=c=10
print(f"El valor de a:{a}")
print(f"El valor de b:{b}")
print(f"El valor de c:{c}")

#Intercambio de valores, sin utilizar variables temporales
x,y = 5 , 10
print(f" Valores iniciales x = {x}, y = {y}")
y, x = x, y
print(f"Invertir los valores x={x}, y={y}")

#recibir multiples valores de la entrada del usuario

nombre, apellido = input (" ingresa tu nombre y apellido separados por una coma: \n").split(",")
print(f"El nombre es: {nombre}\n El apellido es: {apellido}")

#Operadodes de asignacion compuestos

#Los operadores de asignacion compuestos combinan una operacion arimetica con una asignacion
print("*** Operadores de asignacion compuestos***")
a,b = 10,15
print(f"Valor incial compuesto a: {a}, b: {b}")
#Operador compuesto de suma +=
a += b 
print(f"Opeador a += b es: {a}")

#Operador de resta
a = 10 
a -= b 
print (f"Operador a -= b es : {a}")

#Operador compuesto de multiplicacion 
a = 10
a*=b 
print (f"Operador a *= b es : {a}")
#Operador compuesto de division
a = 10
a/= b 
print (f"Operador a /= b es : {a}")