#Crea un programa para solicitar a los empleados su informacion por consola
print("Dame tu nombre")
nombre_empleado = input()
print("Dame tu edad")
edad = int(input())
print("Dame tu salario")
salario = float(input())
print(" departamento de:")
departamento = input()
print ("¿Es jefe?")
jefe = bool(input())

print(f"El nombre del empleado es: {nombre_empleado} \n es la edad del empleado es: {edad}\n el salario del empleado es: {salario} \n es jefe del departamento de: {departamento}")