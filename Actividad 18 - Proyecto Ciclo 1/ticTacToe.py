# Este programa es un videojuego del reconocido Tic Tac Toe, ejecutado 100% en consola. 
# Juego diseñado para dos jugadores, que mediante entrada de texto en consola, se elegirá
# donde colocar la ficha en el tablero de 3x3.


# IMPORTAR BIBLIOTECAS NECESARIAS
import time
import json
import os


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
rutaFile = "Actividad 18 - Proyecto Ciclo 1/datos.json"
lstJugadores = []
dictJugadores = {}
count = 0


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAMENTE NECESARIAS
def filtrarTexto(texto):
    textoArray = texto.split(" ")
    textoFiltradoArray = []
    
    for i in range(len(textoArray)):
        if textoArray[i] != "":
            textoFiltradoArray.append(textoArray[i])
    
    return textoFiltradoArray


def crearMatrices(escala):
    matrizJuego = []
    
    for i in range(escala):
        fila = [''] * escala
        matrizJuego.append(fila)
    
    return matrizJuego


def llenarTableroInicial(matrizJuego):
    for f in range(len(matrizJuego)):
        for c in range(len(matrizJuego[f])):
            matrizJuego[f][c] 


def mostrarTablero(matrizJuego):
    for f in range(len(matrizJuego)):
        for c in range(len(matrizJuego[f])):
            print(matrizJuego[f][c], end=" ")
        print("")



def actualizarTableroMatriz(matrizJuego, indice):
    fila, columna = obtenerMovimientoJugador(lstJugadores[indice][1], matrizJuego)
    
    matrizJuego[fila - 1][columna - 1] = lstJugadores[indice][2]
    mostrarTablero(matrizJuego)
    
    return matrizJuego


def cargarInformacion(rutaFile):
    try:
        fd = open(rutaFile, "r")
    except Exception as e:
        try:
            fd = open(rutaFile, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            return False
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        return False
    
    # print(lstPersonal)  #eliminarLuego
    fd.close()
    return lstPersonal


def jugadoresNombre(msj1, msj2, lstJugadores):
    #Validación n°1 - Verificar si el jugador 1 ya existe
    while True:
        try:
            jugador1 = validarNombre(msj1, 1)
            existeJugador1 = validarExisteJugador(jugador1, lstJugadores)
            
            if existeJugador1:
                print("Error: El jugador ya existe. Ingrese otro apodo.\n")
                continue
            lstJugadores.append([1, jugador1])
            break
        
        except Exception as e:
            pass
    
    
    #Validación n°2 - Verificar si el jugador 2 ya existe
    while True:
        try:
            jugador2 = validarNombre(msj2, 1)
            existeJugador2 =validarExisteJugador(jugador2, lstJugadores)
            
            if existeJugador2:
                print("Error: El jugador ya existe. Ingrese otro apodo.\n")
                continue
            lstJugadores.append([2, jugador2])
            break
        
        except Exception as e:
            pass
    
    return lstJugadores


def eleccionFicha(lstJugadores, count):
    print(f"\n{lstJugadores[count][1]}, elige tu ficha: ")  #Pasar el nombre de jugador 1 y 2
    opcionUsuario = validarOpcionUsuario(">> Escribe 1 para X o 2 para O: ", 1, 2)
    
    if opcionUsuario == 1:
        jugador1Ficha = "X"
        jugador2Ficha = "O"
    
    elif opcionUsuario == 2:
        jugador1Ficha = "O"
        jugador2Ficha = "X"

    
    lstJugadores[count].append(jugador1Ficha)
    lstJugadores[count+1].append(jugador2Ficha)
    
    iniciaJugador = inicioJugador(jugador1Ficha, jugador2Ficha, count, "X")
    print(iniciaJugador)
    return [jugador1Ficha, jugador2Ficha, iniciaJugador]


def cambiarTurno(turnoActual):
    if turnoActual == 0:
        return 1
    else:
        return 0


def reiniciarTablero():
    pass


def jugarOtraPartida():
    pass


def mensajeVictoria(jugador):
    print(f"¡Felicidades {jugador}! Has ganado.")


def mensajeEmpate():
    print("¡Nadie ganó esta vez! Mejor suerte para la próxima.")


#Define cuál es el jugador que inicia (Por default será X)
def inicioJugador(jugador1Ficha, jugador2Ficha, count, inicioFicha="X"):
    if inicioFicha == jugador1Ficha:
        return lstJugadores[count][0]
    
    elif inicioFicha == jugador2Ficha:
        return lstJugadores[count+1][0]


#Manda a los jugadores a una descripción del juego mientras deciden si jugar o no
def lobbyEspera():
    print("En construcción 🚧")
    return input("¿Estas listo? (1 SI / 0 NO): ")


def obtenerMovimientoJugador(jugador, matrizJuego):
    isValido = True
    
    #Validar si alguna posición en la fila está ocupada.
    while isValido:
        fila = validarOpcionUsuario(f"{jugador}, ingresa el número de fila (1, 2, o 3): ", 1, 3)
        columna = validarOpcionUsuario(f"{jugador}, ingresa el número de columna (1, 2, o 3): ", 1, 3)
        print(fila)
        print(columna)
        print("")
        checked = validarMovimiento(matrizJuego, fila, columna)
        
        if checked:
            isValido = False
        else:
            print("Error: La posición elegida ya está ocupada. Inténtelo de nuevo.")
            isValido = True

    
    return [fila, columna]


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


def validarArchivoApertura(lstJugadores, rutaFile):
    #Validación n°1 - Abrir archivo .json
    try:
        abrirArchivo = open(rutaFile, "r")
    
    except Exception as e:
        try:
            abrirArchivo = open(rutaFile, "w")
            
        except Exception as d:
            print("Error: El archivo no se abrió correctamente. Inténtelo de nuevo.")
            print(f"Error: {d}.\n")
            return False
    
    
    #Validación n°2 - Cargar archivo en el programa
    try:
        linea = abrirArchivo.readline()
        if linea.strip() != "":
            abrirArchivo.seek(0)
            lstJugadores = json.load(abrirArchivo)
        
        else:
            lstJugadores = []
    
    except Exception as e:
        print("Error: El programa no ha podido cargar correctamente la información. Inténtelo de nuevo.")
        print(f"Error: {e}.\n")
        return False
    
    # print(lstJugadores)  #eliminarLuego
    abrirArchivo.close()
    return lstJugadores


def validarExisteJugador(jugador, lstJugadores):
    print(lstJugadores)
    for i in range(len(lstJugadores)):
        if jugador in lstJugadores[i][1]:
            print(lstJugadores[i][1])
            return True
    return False


def validarMovimiento(matrizJugador, fila, columna):
    if matrizJugador[fila - 1][columna - 1] == "":
        return True
    else:
        return False


def validarVictoria(matrizJuego, ficha):
    contador = 0
    
    #Verificando una posible victoria en las filas del tablero
    for f in range(len(matrizJuego)):
        if ficha in matrizJuego[f]:
            contador += 1
        
        if contador == 3:
            print("Ganó por tres en línea en una fila")
            return True
    
    
    #Verificando una posible victoria en las columnas del tablero
    for f in range(len(matrizJuego)):
        contador = 0
        for c in range(len(matrizJuego[f])):
            if ficha in matrizJuego[f][c]:
                contador += 1

            if contador == 3:
                print("Ganó por tres en línea en una columna")
                return True
    
    
    contador = 0
    #Verificando una posible victoria en diagonal de esquina 
    #superior izquierda a esquina inferior derecha
    for i in range(3):
        if ficha in matrizJuego[i][i]:
            contador += 1
        
        if contador == 3:
            print("Ganó por una diagonal principal")
            return True
    
    
    contador = 0
    #Lo mismo que arriba pero al revés
    for i in range(3):
        if ficha in matrizJuego[i][2 - i]:
            contador += 1
        
        if contador == 3:
            print("Ganó por una diagonal secundaria.")
            return True


#Si esta función se ejecuta, significa que la validación de ganador fue falsa
def validarEmpate(matrizJuego):
    posicionesOcupadas = 0
    posicionesTotales = len(matrizJuego) * len(matrizJuego[0])
    
    #Verificar cuantas casillas han sido ocupadas
    for f in range(len(matrizJuego)):
        for c in range(len(matrizJuego[f])):
            if matrizJuego[f][c] != "":
                posicionesOcupadas += 1
                
    #Verificar si las casillas ocupadas son iguales a las casillas totales
    if posicionesOcupadas == posicionesTotales:
        print("¡La ronda ha quedado en un empate!")
        return True
    
    return False


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n", "*** TIC TAC TOE ***".center(27))
    print("MENU".center(30))
    
    print("1. ¡Jugar!")
    print("2. Tabla de Clasificación")
    print("3. Salir")
    return validarOpcionUsuario(msj, 1, 3)


#Una vez iniciado todo lo necesario para el juego, se entra a la lógica de este, iniciando otras funciones más
def jugar(lstJugadores, indiceJugador):
    jugando = True
    turnoActual = indiceJugador
    
    #Creando el tablero del juego y mostrándolo en pantalla
    matrizJuego = crearMatrices(3)
    llenarTableroInicial(matrizJuego)
    mostrarTablero(matrizJuego)
    
    
    while jugando:
        # print(turnoActual)  #eliminarLuego
        # print(len(lstJugadores))  #eliminarLuego
        
        print(f"¡Turno de {lstJugadores[turnoActual][1]} ! Elije el movimiento de tu ficha a continuación:")
        matrizJuego = actualizarTableroMatriz(matrizJuego, turnoActual)
        
        
        #Validar si ha ocurrido una victoria
        if validarVictoria(matrizJuego, lstJugadores[turnoActual][2]):
            mensajeVictoria(lstJugadores[turnoActual][1])
            jugando = False
        
        #Validar si ha ocurrido un empate
        if validarEmpate(matrizJuego):
            mensajeEmpate()
            jugando = False
        
        turnoActual = cambiarTurno(turnoActual)


# Esta función contendrá múltiples llamados a otras funciones que inicializarán todos los aspectos
# necesarios para que el juego inicie correctamente.
def inicializarJuego(lstJugadores, count):
    ejecutar = True
    
    validarArchivoApertura(lstJugadores, rutaFile)
    test = jugadoresNombre("\n>> Nombre del jugador n°1: ", ">> Nombre del jugador n°2: ", lstJugadores)
    jugadorFicha1, jugadorFicha2, iniciaJuego = eleccionFicha(lstJugadores, count)
    
    
    #Iniciar juego solo si el usuario lo permite
    while ejecutar:
        iniciarJuego = validarOpcionUsuario(">> ¿Desean iniciar el juego? (1 SI / 0 NO): ", 0, 1)
        
        
        for i in range(len(lstJugadores)):
            if iniciaJuego in lstJugadores[i]:
                # jugadorInicial = lstJugadores[i][1]
                indiceJugador = i
        
        
        #Si los jugadores están listos para jugar, se ejecuta el siguiente código:
        if iniciarJuego == 1:
            jugar(lstJugadores, indiceJugador)
            input("Testeando...")
            ejecutar = False
        
        #Si los jugadores aún no están listos, se ejecuta lo siguiente:
        elif iniciarJuego == 0:
            opcionUsuarioLobby = lobbyEspera()
            
            if opcionUsuarioLobby == 1:
                ejecutar = False
            elif opcionUsuarioLobby == 0:
                ejecutar = True
    
    
    # print(test)  #eliminarLuego
    # print(jugadorFicha1, jugadorFicha2)  #eliminarLuego
    # print(f"Inicia juego: {iniciaJuego}")  #eliminarLuego


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción: ")
    
    if opcionUsuario == 1:
        inicializarJuego(lstJugadores, count)
        #Esta variable contador permite que el primer usuario sea el que ingrese siempre la opción, 
        #a pesar de existir más de dos jugadores registrados. Se suma de dos en dos.
        count += 2
    
    elif opcionUsuario == 2:
        pass
    
    elif opcionUsuario == 3:
        isVerdadero = False
        print("Saliendo...")