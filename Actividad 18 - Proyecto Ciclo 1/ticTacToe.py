# Este programa es un videojuego del reconocido Tic Tac Toe, ejecutado 100% en consola. 
# Juego diseñado para dos jugadores, que mediante entrada de texto en consola, se elegirá
# donde colocar la ficha en el tablero de 3x3.


# IMPORTAR BIBLIOTECAS NECESARIAS
import time
import json


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
rutaFile = "Actividad 18 - Proyecto Ciclo 1/datos.json"
dictJugadores = {}


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAMENTE NECESARIAS
def filtrarTexto(texto):
    textoArray = texto.split(" ")
    textoFiltradoArray = []
    
    for i in range(len(textoArray)):
        if textoArray[i] != "":
            textoFiltradoArray.append(textoArray[i])
    
    return textoFiltradoArray


def mostrarTablero():
    pass


def crearMatrices(escala):
    matrizJuego = []
    
    for i in range(escala):
        fila = [0] * escala
        matrizJuego.append(fila)
    
    return matrizJuego


def mostrarMatriz(matrizJuego):
    for f in range(len(matrizJuego)):
        for c in range(len(matrizJuego[f])):
            print(matrizJuego[f][c], end="")
        print("")


def actualizarTableroMatriz(matrizJuego):
    pass


def cargarInformacion(rutaFile):
    try:
        fd = open(rutaFile, "r")
    except Exception as e:
        try:
            fd = open(rutaFile, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        return None
    
    print(lstPersonal)
    fd.close()
    return lstPersonal


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes elegir una opción dentro del rango válido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción elegida. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNombre(msj, min):
    while True:
        try:
            nombre = input(msj).strip()
            nombreFiltradoArray = filtrarTexto(nombre)
            
            nombreValidar = "".join(nombreFiltradoArray).lower()
            nombreFinal = " ".join(nombreFiltradoArray).title()
            
            if len(nombreFiltradoArray) < min:
                print(f"Error: Tu apodo debe tener al menos {min} palabras.\n")
                continue
            
            elif nombreValidar.isdigit() or not nombreValidar.isalnum() or len(nombreValidar) == 0:
                print("Error: El apodo no debe tener números ni caracteres especiales, solo letras.\n")
                continue
            
            return nombreFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el apodo, inténtelo de nuevo.\n")
            print(f"Error: {e}\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNumero(msj, min, max):
    while True:
        try:
            numero = int(input(msj))
            
            if numero < min or numero > max:
                print(f"Error: Debes ingresar un valor numérico entre el rango válido ({min}-{max}).\n")
                continue
            return numero
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el número. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarArchivoAperturaEscritura():
    pass


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n", "*** TIC TAC TOE ***".center(27))
    print("MENU".center(30))
    
    print("1. ¡Jugar!")
    print("2. Tabla de Clasificación")
    print("3. Salir")
    return validarOpcionUsuario(msj, 1, 3)


# Esta función contendrá múltiples llamados a otras funciones que inicializarán todos los aspectos
# necesarios para que el juego inicie correctamente.
def inicializarJuego():
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción: ")
    
    if opcionUsuario == 1:
        pass
    
    elif opcionUsuario == 2:
        pass
    
    elif opcionUsuario == 3:
        isVerdadero = False
        print("Saliendo...")