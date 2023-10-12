# Programa que permite leer y mostrar en pantalla los datos del personal 
# de una empresa que están almacenados en el disco del equipo de cómputo.


# DECLARANDO LAS VARIABLES PRINCIPALES
count = 0
encabezado = []
listaInfoEmpleados = []
personal = {}


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def crearMatrices(fil, col):
    matrizDatos = []
    
    for i in range(fil):
        fila = [""] * col
        matrizDatos.append(fila)
    
    return matrizDatos


def llenarMatriz(matriz):
    for f in range(len(matriz)):
        print(f"\nFila n°{f+1}")
        
        for c in range(len(matriz[f])):
            matriz[f][c] = encabezado[f], listaInfoEmpleados[f][c]
    
    return matriz
    

# CREANDO LA ESTRUCTURA DEL PROGRAMA
infoEmpleados = open("Persistencia de Datos\Ejercicios\datos-de-empleados-programa\datos-empleados.dat", "r")
encabezado.append(infoEmpleados.readline())
convertirToLista = list(infoEmpleados)


for i in range(len(convertirToLista)):
    listaInfoEmpleados.append(convertirToLista[i].split(","))
infoEmpleados.close()




for i in range(len(listaInfoEmpleados)):
    for j in range(count, count+1):
        matriz = crearMatrices(len(listaInfoEmpleados), 2)
        llenarMatriz(matriz)
        

print(encabezado)
print(matriz)