# Python permite leer archivos mediante el uso de una librería, no solo para leerlo, 
# también para editar o recuperar información para usarse posteriormente en el ñrograma.


archivo = open("Persistencia/de/Datos/nombres.txt", "r")

texto = archivo.read()

print(texto)

archivo.close()