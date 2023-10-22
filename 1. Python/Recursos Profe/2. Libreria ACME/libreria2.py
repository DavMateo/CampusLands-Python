# Este programa permite llevar el control de los libros presentes en una librería, con toda su
# respectiva información de manera ordenada, almacenada permanentamente en disco.


# IMPORTAR LAS LIBRERÍAS NECESARIAS
import json


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
inicializandoSistema = True
dictLibros = {}


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoFinalArray = []
    
    for i in range(len(texto)):
        if texto[i] != "":
            textoFinalArray.append(texto[i])
    
    textoValidar = "".join(textoFinalArray).lower()
    textoFinal = " ".join(textoFinalArray).upper()
    
    return [textoValidar, textoFinal]


def organizarInfoLibros():
    pass


def existeLibro(cod, dictLibros):
    codigo = validarCodigo(cod, 1, 1) 
    validarExisteLibro = dictLibros.get(codigo)
    
    if validarExisteLibro == None:
        return False
    else: 
        return codigo, validarExisteLibro


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


def validarAbrirInfoArchivo(rutaFile, dictLibros):
    #Validación n°1 - Intentar abrir el archivo en modo lectura / escritura
    try:
        intentarAbrirArchivo = open(rutaFile, "r")
    
    except Exception as e:
        try:
            intentarAbrirArchivo = open(rutaFile, "w")
        
        except Exception as d:
            print("Ha ocurrido un problema al intentar abrir el archivo necesario.")
            print(f"Error: {d}.\n")
            input("Presione cualquier tecla para salir al menú principal...")  #eliminarLuego
            return False
    intentarAbrirArchivo.close()
    
    
    #Validación n°2 - Recibir la información del archivo ".json" al ejecutarse el programa
    try:
        abrirArchivo = open(rutaFile, "r")
        
        linea = abrirArchivo.readline()
        if linea.strip() != "":
            abrirArchivo.seek(0)
            dictLibros.update(json.load(abrirArchivo))
        
        else:
            dictLibros = {}
    
    except Exception as e:
        print("Ha ocurrido un problema al intentar recuperar la información del sistema.")
        print(f"Error: {e}.\n")
        input("Presione cualquier tecla para salir al menú principal...")  #eliminarLuego
        return False
    
    return dictLibros


def validarEscribirInfoArchivo(rutaFile, dictLibros):
    #Validación n°1 - Abrir el archivo en modo escritura
    try:
        guardarInfo = open(rutaFile, "w")
    
    except Exception as e:
        print("Ha ocurrido un problema al ejecutarse la función de guardado.")
        print(f"Error: {e}.\n")
        return False

    
    #Validación n°2 - Escribir la información en el archivo correspondiente
    try:
        json.dump(dictLibros, guardarInfo)
    
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


def validarPrecio(msj, min):
    while True:
        try:
            precio = int(input(msj))
            
            if precio < min:
                print(f"Error: El precio no puede ser menor a ${min:,.0f} COP.\n")
                continue
            return precio
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el precio. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n", "LIBRERÍA ACME".center(20))
    print("MENU".center(21))
    
    print("1. Insertar Libro")
    print("2. Consultar Libro")
    print("3. Editar Libro")
    print("4. Borrar Libro")
    print("5. Listar Libro")
    print("6. Salir")
    return validarOpcionUsuario(msj, 1, 6)


def inicializarPrograma(rutaFile, dictLibros):
    return validarAbrirInfoArchivo(rutaFile, dictLibros)


def insertarLibro(cod, tit, autor, precio, dictLibros):
    print("\n*** INSERTAR LIBRO ***")
    print("Ingrese a continuación la siguiente información sobre el libro:\n")
    
    #Verificar que el código sea válido y no esté registrado
    while True:
        codigo = validarCodigo(cod, 1, 1) 
        validarExisteLibro = dictLibros.get(codigo)
        
        if validarExisteLibro == None:
            titulo = validarTexto(tit, 1)
            autorLibro = validarTexto(autor, 1)
            precioLibro = validarPrecio(precio, 1000)
            return [codigo, titulo, autorLibro, precioLibro]
        
        else:
            print("Error: El código ingresado ya pertenece a un libro registrado.")
            reintentar = validarOpcionUsuario(">> ¿Deseas volver a intentarlo? (1 SI / 0 NO): ", 0, 1)
            print("")
            
            if reintentar == 1:
                continue
            elif reintentar == 0:
                return False


def consultarLibro(cod, dictLibros):
    print("\n*** CONSULTAR LIBRO ***\n")
    
    while True:
        verificarExisteLibro = existeLibro(cod, dictLibros)
        
        if verificarExisteLibro == False:
            print("Error: El código ingresado no corresponde a ningún libro registrado. Inténtelo de nuevo.\n")
            volverIntentar = validarOpcionUsuario(">> ¿Desea volver a buscar el libro? (1 SI / 0 NO): ", 0, 1)
            
            if volverIntentar == 1:
                input("Asegúrate de que el código está escrito correctamente...")
                continue
            elif volverIntentar == 0:
                input("Regresando al menú principal. Presione cualquier tecla para continuar...")
                break
        
        else:  
            tituloTab, autorTab, precioTab = list(verificarExisteLibro[1].keys())
            tituloLibro, autorLibro, precioLibro = list(verificarExisteLibro[1].values())
            
            print(f"\n==== Código: {verificarExisteLibro[0]} ====")
            print(f"{tituloTab.upper()}: {tituloLibro.title()}")
            print(f"{autorTab.upper()}: {autorLibro.title()}")
            print(f"{precioTab}: ${precioLibro:,.0f} COP")
        
        
        seguirConsultando = validarOpcionUsuario("\n>> ¿Deseas consultar otro libro? (1 SI / 0 NO): ", 0, 1)
        
        if seguirConsultando == 1:
            continue
        elif seguirConsultando == 0:
            input("Presione cualquier tecla para regresar al menú...")
            break


def editarLibro(cod, dictLibros):
    print("\n*** EDITAR LIBRO ***\n")
    
    while True:
        codigo = validarCodigo(cod, 1, 1)


def borrarLibro():
    pass


def listarLibros():
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    while inicializandoSistema:
        rutaFile = "1. Python/Recursos Profe/2. Libreria ACME/data.json"
        dictLibros = inicializarPrograma(rutaFile, {})
        print("¡EL BUCLE DE INICIALIZANDO SISTEMA ACABA DE EJECUTARSE!")
        break
    
    inicializandoSistema = False
    opcionUsuario = menu("   >> Elije una opción: ")
    
    if opcionUsuario == 1:
        while True:
            infoLibroAgregar = insertarLibro(">> Código: ", ">> Título: ", ">> Autor: ", ">> Precio: ", dictLibros)
            
            #Verifica si el código del libro existe o no mediante la respuesta de la función "insertarLibro()" por parte de la función "existeLibro()"
            if infoLibroAgregar == False:
                break
            else:
                codigo, titulo, autor, precio = infoLibroAgregar
            
            
            #Agregar la información del libro a un diccionario vacío
            dictLibrosMemoria = {}
            dictLibrosMemoria[codigo] = {
                "titulo": titulo,
                "autor": autor,
                "precio": precio
            }
            dictLibros.update(dictLibrosMemoria)
            
            #Cargar información al archivo JSON
            if validarEscribirInfoArchivo(rutaFile, dictLibros):
                print(f"\n¡El libro '{titulo.title()}' con el código '{codigo}' ha sido guardado con éxito!")
            else:
                break
            
            
            #Verificar si el usuario desea continuar agregando libros
            continuar = validarOpcionUsuario(">> ¿Desea agregar otro libro? (1 SI / 0 NO): ", 0, 1)
            if continuar == 1:
                continue
            elif continuar == 0:
                input("Presione cualquiet tecla para regresar al menú...")
                break

    
    elif opcionUsuario == 2:
        consultarLibro(">> Ingrese el código del libro a consultar: ", dictLibros)
    
    elif opcionUsuario == 3:
        editarLibro(">> Ingrese el código del libro a editar: ", dictLibros)
    
    elif opcionUsuario == 4:
        pass
    
    elif opcionUsuario == 5:
        pass
    
    elif opcionUsuario == 6:
        isVerdadero = False
        print("Saliendo...")