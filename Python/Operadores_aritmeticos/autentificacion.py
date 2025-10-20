#Sistema de autentificacion pirata 

cuenta = "SofiaReyes"
password = "hola123"

cuenta_proporcionada = input("Cuenta: \n")
password_proporcionada = input("Password: \n")

if (cuenta_proporcionada == cuenta):
    if (password_proporcionada == password):
        print ("Acceso concedido")
    else :
        print ("Password incorrecto")
else :
    print("No se a encontrado la cuenta")