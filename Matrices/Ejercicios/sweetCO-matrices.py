# Programa para la empresa SweetCO para responder sus dudas sobre las ventas semanales.


# VARIABLES PRINCIPALES
matrizPrecios = [1500, 5000, 6500, 2500, 22500]
matrizVentas = [
    [100, 88, 92, 94, 85, 110, 118],
    [30, 42, 31, 32, 38, 40, 37],
    [23, 35, 39, 45, 55, 60, 61],
    [45, 50, 56, 65, 47, 57, 68],
    [18, 25, 33, 21, 22, 28, 32]
]


# FUNCIONES COMPLEMENTARIAS


# FUNCIONES DE VALIDACIÓN



# FUNCIONES PRINCIPALES
def calcularProductoMaxIngresoSemana(matrizVentas, matrizPrecios):
    filas = len(matrizVentas)
    listaTotalVentas = [0] * filas

    for f in range(filas):
        listaTotalVentas[f] = sum(matrizVentas[f]) * matrizPrecios[f]
    
    print(listaTotalVentas)
    maxVentas = max(listaTotalVentas)
    productoMaxVentas = listaTotalVentas.index(maxVentas) + 1
    
    return productoMaxVentas


def calcularDiaSemanaMaxIngresos(matrizVentas, matrizPrecios):
    columnas = len(matrizVentas[0])
    listaTotalIngresos = [0] * columnas
    countRow = 0
    countCol = 0
    
    for f in range(len(matrizVentas)):
        for c in range(countCol, countCol+1):
            listaTotalIngresos[c] = [matrizVentas[f][c]]
            countCol += 1
        
        # countRow += 1
    # Terminar el algoritmo


# ESTRUCTURA DEL PROGRAMA
productoMaxIngresoSemana = calcularProductoMaxIngresoSemana(matrizVentas, matrizPrecios)
print(f"El producto que más genera ingresos en la semana es: {productoMaxIngresoSemana}")

print("\n\n")
diaMaxIngresoSemana = calcularDiaSemanaMaxIngresos(matrizVentas, matrizPrecios)
print(f"El día que más se genera ingresos es el: {diaMaxIngresoSemana}")