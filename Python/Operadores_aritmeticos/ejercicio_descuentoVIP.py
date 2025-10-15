print("***Sistema de descuentos VIP")

No_Productos = 10
cantidad_producto = int(input("Cuantos articulos compraste "))
tiene_mebresia = input("Tienes la membresia de la tienda (si o no)")

es_elegible_descuento = (cantidad_producto >= No_Productos and tiene_mebresia.strip().lower() == "si")
print (f"Tienes acesso al descuento: {es_elegible_descuento}")