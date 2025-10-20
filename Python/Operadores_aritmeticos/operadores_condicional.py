# Operadores condicionales
#el resultado sera siempre un valor binario y verificara si la condicion es verdadera o falsa

#a=b   operador de igualdad
# 
# 
#a!=b operdador diferente de 
# 
# 
# Operador menor que (<) 
#
#
#Operador menor o igual que (<=)

print ("***Operadores comparacion (relacionales)")

a,b = 3,5
print (f"El valor incial de a:{a}\n el valor de b: {b}")
resultado = ( a ==b )
print(f"Resultad de a = b :{resultado}")

#operador diferente 
resultado = (a != b)
print(f"Resultad de a != b :{resultado}")

#Operaor de mayor 
resultado = (a > b)
print(f"Resultad de a > b :{resultado}")

#Operaor de mayor o igual 
resultado = (a >= b)
print(f"Resultad de a >= b :{resultado}")

#Operaor de menor l 
resultado = (a < b)
print(f"Resultad de a < b :{resultado}")

#Operaor de menor o igual 
resultado = (a <= b)
print(f"Resultad de a <= b :{resultado}")


#Expresiones logicas
exp1 = False
exp2 = True
#Operador logico and 

resultado = exp1 and exp2 
print (f"El resultado de comparar true y false con and es: {resultado}")

resultado = exp1 or exp2 
print (f"El resultado de comparar true y false con aor es: {resultado}")

resultado = not exp1 
print (f"El resultado de aplicar not en False es: {resultado}")

