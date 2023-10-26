# Este programa es un videojuego del clásico Piedra, Papel o Tijera en el cuál el jugador (mediante consola) podrá
# enfrentarse contra la computadora o contra otro jugador. Contará también con tabla de clasificación local y global.


# IMPORTANDO LAS LIBRERÍAS INDISPENSABLES
import random
import json
import time


# DECLARANDO LAS VARIABLES NECESARIAS
numRondas = 3
isVerdadero = True
iniciandoSistema = True


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoFinalArray = []
    
    for i in range(len(texto)):
        if texto[i] != "":
            textoFinalArray.append(texto[i])
    
    textoValidar = "".join(textoFinalArray)
    textoFinal = " ".join(textoFinalArray)
    
    return [textoValidar, textoFinal]


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes elegir una opción numérica dentro del rango válido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción seleccionada. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarAbrirInfoArchivo(rutaFileJson, dictJuego):
    #Validación n°1 - Intentar abrir el archivo en modo lectura / escritura
    try:
        intentarAbrirArchivo = open(rutaFileJson, "r")
    
    except Exception as e:
        try:
            intentarAbrirArchivo = open(rutaFileJson, "w")
        
        except Exception as d:
            print("Ha ocurrido un problema al intentar abrir el archivo necesario.")
            print(f"Error: {d}.\n")
            return False
    intentarAbrirArchivo.close()
    
    
    #Validación n°2 - Recibir la información del archivo ".json" al ejecutarse el programa
    try:
        abrirArchivo = open(rutaFileJson, "r")
        
        linea = abrirArchivo.readline()
        if linea.strip() != "":
            abrirArchivo.seek(0)
            dictJuego.update(json.load(abrirArchivo))
        
        else:
            dictJuego = {}
    
    except Exception as e:
        print("Ha ocurrido un problema al intentar recuperar la información del sistema.")
        print(f"Error: {e}.\n")
        return False
    
    return dictJuego


def validarEscribirInfoArchivo(rutaFileJson, dictJuego):
    #Validación n°1 - Abrir el archivo en modo escritura
    try:
        guardarInfo = open(rutaFileJson, "w")
    
    except Exception as e:
        print("Ha ocurrido un problema al ejecutarse la función de guardado.")
        print(f"Error: {e}.\n")
        return False

    
    #Validación n°2 - Escribir la información en el archivo correspondiente
    try:
        json.dump(dictJuego, guardarInfo)
    
    except Exception as e:
        print("Ha ocurrido un problema al guardar la información del libro ingresado.")
        print(f"Error: {e}.\n")
        return False
    
    guardarInfo.close()
    return True


def validarCodigo(msj, min, max):
    while True:
        try:
            codigo = input(msj).strip()
            codigoArray = codigo.split(" ")
            
            if len(codigoArray) < min or len(codigoArray) > max:
                print(f"Error: El código introducido no puede ser menor ni mayor a {min}-{max} palabras.\n")
                continue
            codigoValidar, codigoFinal = filtrarTexto(codigoArray)
            
            if not codigoValidar.isalnum() or len(codigoValidar) == 0:
                print("Error: El código no puede estar vacío ni contener caracteres especiales.\n")
                continue
            return codigoFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el código. Inténtelo de nuevo.\n")
            print(f"Error: {e}.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarTexto(msj, min):
    while True:
        try:
            texto = input(msj).strip()
            textoArray = texto.split(" ")
            
            if len(textoArray) < min:
                print(f"Error: El texto debe contener al menos {min} palabras.\n")
                continue
            textoValidar, textoFinal = filtrarTexto(textoArray)
            
            if textoValidar.isdigit() or not textoValidar.isalnum() or len(textoValidar) == 0:
                print("Error: El texto ingresado no puede estar vacío, componerse de solo números o contener caracteres especiales.\n")
                continue
            return textoFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el texto. Inténtelo de nuevo.\n")
            print(f"Error: {e}.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n", "JUEGO PIEDRA-PAPEL-TIJERA".center(20))
    print("MENU".center(26))
    
    print("1. Tutorial")
    print("2. Jugador vs IA")
    print("3. Jugador vs Jugador")
    print("4. Tabla de clasificación")
    print("5. Configuración")
    print("6. Salir")
    return validarOpcionUsuario(msj, 1, 6)


def inicializarPrograma(rutaFileLocal, dictJugadorIA, rutaFileGlobal, dictJugadores):
    return [0, 0]


def configuracion(rutaFileGlobal, rutaFileLocal, nameIA, rondasNum):
    return [0, 0, 0, 0]


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    while iniciandoSistema:
        rutaFileGlobal, rutaFileLocal, nombreIA, numRondas = configuracion("Ejercicios adicionales/PiedraPapelTijera/data", "Ejercicios adicionales/PiedraPapelTijera/data", ">> ¿Cómo quieres que se llame la IA?: ", ">> ¿Cuántas rondas deseas que tenga una partida? (Default 3 rondas): ")
        dictJugadorIA, dictJugadores = inicializarPrograma(rutaFileLocal, {}, rutaFileGlobal, {})
        break
    
    iniciandoSistema = False
    opcionUsuario = menu("   >> Elija una opción: ")
    
    if opcionUsuario == 1:
        pass
    
    elif opcionUsuario == 2:
        pass
    
    elif opcionUsuario == 3:
        pass
    
    elif opcionUsuario == 4:
        pass
    
    elif opcionUsuario == 5:
        pass
    
    elif opcionUsuario == 6:
        isVerdadero = False
        input("\nSaliendo...")