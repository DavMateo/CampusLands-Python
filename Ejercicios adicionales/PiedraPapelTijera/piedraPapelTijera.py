# Este programa es un videojuego del clásico Piedra, Papel o Tijera en el cuál el jugador (mediante consola) podrá
# enfrentarse contra la computadora o contra otro jugador. Contará también con tabla de clasificación local y global.


# IMPORTANDO LAS LIBRERÍAS INDISPENSABLES
import random
import json
import time
import colorama


# DECLARANDO LAS VARIABLES NECESARIAS
isVerdadero = True
iniciandoSistema = True
configMod = False


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoFinalArray = []
    
    for i in range(len(texto)):
        if texto[i] != "":
            textoFinalArray.append(texto[i])
    
    textoValidar = "".join(textoFinalArray)
    textoFinal = " ".join(textoFinalArray)
    
    return [textoValidar, textoFinal]


def accederConfig(rutaFileLocal, rutaFileGlobal, checked):
    continuarConfig = True
    dictInfoReturn = {}
    
    #Verificando que el jugador ya tenga una configuración previamente aplicada al juego
    if rutaFileLocal == "" and rutaFileGlobal == "":
        opcionUsuarioConfig = validarOpcionUsuario(">> ¿Desea configurar la app (Escribir 1) o quieres aplicar la configuración por defecto? (Escribir 0): ", 0, 1)
        
        #Si el jugador desea aplicar una configuración personalizada, entonces:
        if opcionUsuarioConfig == 1:
            #El bucle while es por si acaso el usuario desea configurar más parámetros del juego
            while continuarConfig:
                opcionElegida, configuracionAplicada = configuracion("Ejercicios adicionales/PiedraPapelTijera/data", "Ejercicios adicionales/PiedraPapelTijera/data", ">> ¿Cómo quieres que se llame la IA?: ", ">> ¿Cuántas rondas deseas que tenga una partida? (Default 3 rondas): ")
                
                if opcionElegida == 1:
                    rutaFileLocal = configuracionAplicada
                    print("\nCONFIG:", rutaFileLocal)
                    dictInfoReturn[opcionElegida] = [opcionElegida, rutaFileLocal]
                
                elif opcionElegida == 2:
                    rutaFileGlobal = configuracionAplicada
                    print("\nCONFIG:", rutaFileGlobal)
                    dictInfoReturn[opcionElegida] = [opcionElegida, rutaFileGlobal]
                
                elif opcionElegida == 3:
                    nombreIA = configuracionAplicada
                    print("\nCONFIG:", nombreIA)
                    dictInfoReturn[opcionElegida] = [opcionElegida, nombreIA]
                
                elif opcionElegida == 4:
                    numRondas = configuracionAplicada
                    print("\nCONFIG:", numRondas)
                    dictInfoReturn[opcionElegida] = [opcionElegida, numRondas]
                
                elif opcionElegida == 5:
                    continuarConfig = False
                    return False
                
                #Preguntarle al jugador si ya ha terminado de realizar las configuraciones pertinentes
                continuar = validarOpcionUsuario(">> ¿Desea configurar o modificar otro parámetro? (1 SI / 0 NO): ", 0, 1)
                
                if continuar == 1:
                    continue
                elif continuar == 0:
                    continuarConfig = False
                    return dictInfoReturn
        
        #Si el jugador desea una configuración por defecto, entonces:
        elif opcionUsuarioConfig == 0:
            rutaFileGlobal = "Ejercicios adicionales/PiedraPapelTijera/data/datosGlobal.json"
            rutaFileLocal = "Ejercicios adicionales/PiedraPapelTijera/data/datosLocal.json/"
            nombreIA = "Computadora"
            numRondas = 3
            

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
    
    print(colorama.Style.DIM + "1. Tutorial")
    print("2. Jugador vs IA")
    print("3. Jugador vs Jugador")
    print("4. Tabla de clasificación")
    print("5. Configuración")
    print("6. Salir")
    return validarOpcionUsuario(msj, 1, 6)


def inicializarPrograma(rutaFileLocal, dictJugadorIA, rutaFileGlobal, dictJugadores):
    return [0, 0]


def configuracion(rutaFileGlobal, rutaFileLocal, nameIA, rondasNum):
    print("\n==== CONFIGURACIÓN ====")
    print("1. Ruta personalizada de estadísticas Player vs IA")
    print("2. Ruta personalizada del registro de victorias Player vs Player")
    print("3. Darle un nombre a la IA")
    print("4. Cambiar el número de rondas por partida")
    print("5. Regresar al menú principal")
    opcionUsuario = validarOpcionUsuario(">> Digite una opción: ", 1, 5)
    
    # Estructura de la configuración del programa
    if opcionUsuario == 1:
        print("\n", colorama.Fore.BLUE + "*** RUTA ARCHIVO PvE ***")
        nombreArchivo = validarTexto(colorama.Fore.WHITE + "¿Cómo desea llamar al archivo?: ", 1)
        rutaFileAI = f"{rutaFileLocal}" + f"/{nombreArchivo}.json"
        
        return [opcionUsuario, rutaFileAI]
    
    elif opcionUsuario == 2:
        print("\n", colorama.Fore.BLUE + "*** RUTA ARCHIVO PvP ***")
        nombreArchivo = validarTexto(colorama.Fore.WHITE + "¿Cómo desea llamar al archivo?: ", 1)
        rutaFilePvP = f"{rutaFileGlobal}" + f"/{nombreArchivo}.json"
        
        return [opcionUsuario, rutaFilePvP]
    
    elif opcionUsuario == 3:
        print("\n", colorama.Fore.BLUE + "*** NOMBRE IA ***")
        return [opcionUsuario, validarTexto(colorama.Fore.WHITE + nameIA, 1)]
    
    elif opcionUsuario == 4:
        print("\n", colorama.Fore.BLUE + "*** RONDAS POR PARTIDA ***")
        return [opcionUsuario, validarOpcionUsuario(colorama.Fore.WHITE + rondasNum, 1, 30)]
    
    elif opcionUsuario == 5:
        input("\nRegresando al menú principal. \nPresione cualquier tecla para continuar...")
        return [opcionUsuario, False] 


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    while iniciandoSistema:
        rutaFileConfig = "Ejercicios adicionales/PiedraPapelTijera/data/config.json"
        rutaFileLocal = ''
        rutaFileGlobal = ''
        continuarConfig = True
        
        accederConfig(rutaFileLocal, rutaFileGlobal, False)
                
        #Inicializando el juego
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
        opcionUsuarioConfig = validarOpcionUsuario(">> ¿Desea configurar la app (Escribir 1) o quieres aplicar la configuración por defecto? (Escribir 0): ", 0, 1)
        
        #Si el jugador desea aplicar una configuración personalizada, entonces:
        if opcionUsuarioConfig == 1:
            #El bucle while es por si acaso el usuario desea configurar más parámetros del juego
            while continuarConfig:
                opcionElegida, configuracionAplicada = configuracion("Ejercicios adicionales/PiedraPapelTijera/data", "Ejercicios adicionales/PiedraPapelTijera/data", ">> ¿Cómo quieres que se llame la IA?: ", ">> ¿Cuántas rondas deseas que tenga una partida? (Default 3 rondas): ")
                
                if opcionElegida == 1:
                    rutaFileLocal = configuracionAplicada
                    print("\nCONFIG:", rutaFileLocal)
                
                elif opcionElegida == 2:
                    rutaFileGlobal = configuracionAplicada
                    print("\nCONFIG:", rutaFileGlobal)
                
                elif opcionElegida == 3:
                    nombreIA = configuracionAplicada
                    print("\nCONFIG:", nombreIA)
                
                elif opcionElegida == 4:
                    numRondas = configuracionAplicada
                    print("\nCONFIG:", numRondas)
                
                elif opcionElegida == 5:
                    continuarConfig = False
                    break
                
                #Preguntarle al jugador si ya ha terminado de realizar las configuraciones pertinentes
                continuar = validarOpcionUsuario(">> ¿Desea configurar o modificar otro parámetro? (1 SI / 0 NO): ", 0, 1)
                
                if continuar == 1:
                    continue
                elif continuar == 0:
                    continuarConfig = False
        
        #Si el jugador desea una configuración por defecto, entonces:
        elif opcionUsuarioConfig == 0:
            rutaFileGlobal = "Ejercicios adicionales/PiedraPapelTijera/data/datosGlobal.json"
            rutaFileLocal = "Ejercicios adicionales/PiedraPapelTijera/data/datosLocal.json/"
            nombreIA = "Computadora"
            numRondas = 3
    
    elif opcionUsuario == 6:
        isVerdadero = False
        input("\nSaliendo...")