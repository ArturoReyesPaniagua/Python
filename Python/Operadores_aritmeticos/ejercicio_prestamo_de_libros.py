print("*** Prestamo de libros***")

KM_PERMITIDOS = 10

tiene_crendicales = input("tienes credencial de estudiante (Si/No) ")
distancia_KM = int(input("A cuantos km vives de la bibleoteca"))

es_elegible_prestamo = (tiene_crendicales.strip().lower() == "si" or distancia_KM <= KM_PERMITIDOS )

print(f"Eres elegible para el prestamo: {es_elegible_prestamo}")
