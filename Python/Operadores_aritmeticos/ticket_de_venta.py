print("*** Generar Ticket de Venta")

precio_leche = float(input("precio del leche"))
precio_pan = float(input("precio del pan"))
precio_lechuga = float(input("precio del lechuga"))
precio_platanos = float(input("precio del platano"))

print("Calculo del subtotal(sin impuestos)")
subtotal = precio_leche + precio_lechuga + precio_pan + precio_platanos
print(subtotal)
#Calculo de impuestos
impuestos = subtotal * .07
print(f"Los impuestos fueron {impuestos:.2f}")

#calculo con impuestos
total = impuestos + subtotal
print(f"el total de el producto es {total:.2f}")