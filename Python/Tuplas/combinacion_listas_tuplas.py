print("Combinacion de Listas y tuplas")

productos = [
    ("P001", "Camiseta", 20.00),
    ("P002", "camisa", 30.00),
    ("P003", "Sudadera", 40.00)


]

precio_total = 0

for producto in productos:
    id, nombre, precio  = producto
    print (f" el id del producto es: {id}, el nombre del producto es: {nombre} y el precio del producto es: {precio}")
    precio_total = precio_total + precio


print(f"El precio total de los articulos que hay es: {precio}")