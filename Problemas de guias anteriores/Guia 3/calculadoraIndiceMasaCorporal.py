# Este programa calculará el índice de masa corporal
# mostrándola en pantalla junto a la interpretación 
# de la misma.


# IMPORTAR LAS LIBRERÍAS PERTINENTES
import math as Math

# DEFINIENDO LAS VARIABLES PRINCIPALES
pesoLibras = float(input("Ingrese su peso en libras: "))
alturaPulgadas = float(input("Ingrese su altura en pulgadas: "))

# CONVIRTIENDO LOS VALORES DE LIBRAS Y PULGADAS A KG Y MTS
pesoKilogramos = pesoLibras * 0.45359237
alturaMetros = alturaPulgadas * 0.0254

