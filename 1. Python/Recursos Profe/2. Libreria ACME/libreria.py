# Este programa permite llevar el control de los libros presentes en una librería, con toda su
# respectiva información de manera ordenada, almacenada permanentamente en disco.


# IMPORTAR LAS LIBRERÍAS NECESARIAS
import json


# DECLARANDO LAS VARIABLES PRINCIPALES
lstLibros = []
dictLibros = {}
isVerdadero = True
inicializandoSistema = True


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoFinalArray = []
    
    for i in range(len(texto)):
        if texto[i] != "":
            textoFinalArray.append(texto[i])
    
    textoValidar = "".join(textoFinalArray)
    textoFinal = " ".join(textoFinalArray)
    
    return [textoValidar, textoFinal]


def organizarInfoLibros():
    pass


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


def validarAbrirInfoArchivo(rutaFile, xd):
    #Validación n°1 - Intentar abrir el archivo en modo lectura / escritura
    try:
        abrirArchivo = open(rutaFile, "r")
        
    except Exception as e:
        try:
            abrirArchivo = open(rutaFile, "w")
            
        except Exception as d:
            print("Ha ocurrido un problema al intentar abrir el archivo necesario.")
            print(f"Error: {d}.\n")
            input("Presione cualquier tecla para salir al menú principal...")  #eliminarLuego
            return False
    
    
    #Validación n°2 - Recibir la información del archivo ".json" al ejecutarse el programa
    try:
        linea = abrirArchivo.readline()
        if linea.strip() != "":
            abrirArchivo.seek(0)
            lstLibros = json.load(abrirArchivo)
        
        else:
            lstLibros = []
    
    except Exception as e:
        print("Ha ocurrido un problema al intentar recuperar la información del sistema.")
        print(f"Error: {e}.\n")
        input("Presione cualquier tecla para salir al menú principal...")  #eliminarLuego
        return False
    
    print(lstLibros)  #eliminarLuego
    abrirArchivo.close()
    return lstLibros


def validarEscribirInfoArchivo():
    while True:
        try:
            pass

        except:
            pass


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
    

def inicializarPrograma(rutaFile, lstLibros):
    validarAbrirInfoArchivo(rutaFile, lstLibros)


def insertarLibro(cod, tit, autor, precio):
    print("\n*** INSERTAR LIBRO ***")
    print("Ingrese a continuación la siguiente información sobre el libro:\n")
    
    codigo = validarCodigo(cod, 1, 1)
    titulo = validarTexto(tit, 1)
    autorLibro = validarTexto(autor, 1)
    precioLibro = validarPrecio(precio, 1000)
    
    return [codigo, titulo, autorLibro, precioLibro]


def consultarLibro():
    pass


def editarLibro():
    pass


def borrarLibro():
    pass


def listarLibros():
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    while inicializandoSistema:
        inicializarPrograma("1. Python/Recursos Profe/2. Libreria ACME/data.json", lstLibros)
        print("¡EL BUCLE DE INICIALIZANDO SISTEMA ACABA DE EJECUTARSE!")
        break
    
    inicializandoSistema = False
    opcionUsuario = menu("   >> Elije una opción: ")
    
    if opcionUsuario == 1:
        insertarLibro(">> Código: ", ">> Título: ", ">> Autor: ", ">> Precio: ")
        input()
    
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
        print("Saliendo...")