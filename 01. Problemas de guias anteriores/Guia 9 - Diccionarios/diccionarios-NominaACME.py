# Este programa está destinado para ACME, (empresa mencionado en el ejercicio) donde se podrá
# realizar multiples acciones, como agregar, modificar o eliminar usuarios del sistema. Todo 
# esto lleva al enfoque principal, que es el de gestionar la nómina de sus empleados.


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
dictEmpleados = {}
smmlv = 1160000
subsidioTransporte = 140606


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoArray = texto.split(" ")
    textoFiltradoArray = []
    
    for i in range(len(textoArray)):
        if textoArray[i] != "":
            textoFiltradoArray.append(textoArray[i])
    
    return textoFiltradoArray


def existeId(id):
    validarExisteId = dictEmpleados.get(id)
    
    if validarExisteId == None:
        return False
    else:
        return True


#

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


def validarId(msj, min):
    while True:
        try:
            id = int(input(msj))
            existeIdEmpleado = existeId(id)
            
            if existeIdEmpleado:
                print(f"Error: El id '{id}' ya existe.\n")
                continue
            
            else:
                if id < min:
                    print(f"Error: El ID no puede ser menor que {min}.\n")
                    continue
            return id
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el ID del empleado. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNombre(msj, min):
    while True:
        try:
            nombre = input(msj).strip()
            nombreFiltradoArray = filtrarTexto(nombre)
            
            nombreValidar = "".join(nombreFiltradoArray)
            nombreFinal = " ".join(nombreFiltradoArray)
            
            if len(nombreFiltradoArray) < min:
                print("Error: Debes ingresar al menos un nombre y un apellido.\n")
                continue
            
            elif nombreValidar.isdigit() or not nombreValidar.isalnum() or len(nombreValidar) == 0:
                print("Error: El nombre no debe tener números ni caracteres especiales, solo letras.\n")
                continue
            
            return nombreFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el nombre del empleado.\n")
            print(f"Error: {e}\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarHorasTrabajadas(msj, min, max):
    while True:
        try:
            horasTrabajadas = int(input(msj))
            
            if horasTrabajadas < min or horasTrabajadas > max:
                print(f"Error: Debes ingresar un valor numérico entre el rango válido ({min}-{max}).\n")
                continue
            return horasTrabajadas
        
        except ValueError:
            print("Ha ocurrido un error al ingresar las horas laboradas. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarValorHora(msj, min, max):
    while True:
        try:
            valorHora = int(input(msj))
            
            if valorHora < min or valorHora > max:
                print(f"Error: Debes ingresar un valor dentro del rango permitido (${min} COP - ${max} COP).\n")
                continue
            return valorHora
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el valor de la hora laboral. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n", "*** NOMINA ACME ***".center(27))
    print("MENU".center(30))
    
    print("\n1. Agregar empleado")
    print("2. Modificar empleado")
    print("3. Buscar empleado")
    print("4. Eliminar empleado")
    print("5. Listar empleados")
    print("6. Listar nómina de un empleado")
    print("7. Listar nómina de todos los empleados")
    print("8. Salir")
    return validarOpcionUsuario(msj, 1, 8)


def agregarEmpleado():
    print("\n\n", "=== AGREGAR EMPLEADO ===".center(10), "\n")
    print("Para crear el nuevo empleado, se necesita de la siguiente información:")
    
    id = validarId(">> ID: ", 1)
    nombre = validarNombre(">> Nombre: ", 2)
    horasTrabajadas = validarHorasTrabajadas(">> Horas trabajas: ", 1, 160)
    valorHora = validarValorHora(">> Valor de la hora: ", 8000, 150000)
    
    # Agregar la información recolectada al diccionario.
    dictEmpleados[id] = {
        "nombre": nombre, 
        "horasTrabajadas": horasTrabajadas, 
        "valorHora": valorHora
    }
    
    print(dictEmpleados) #EliminarLuego


def modificarEmpleado():
    entrarSubMenu = True
    
    # El objetivo de este while es que permita ejecutar tantas veces como quiera el usuario el submenú sin tener que salirse y volver a digitar la opción de modificar empleado.
    while entrarSubMenu:
        print("\n\n", "=== MODIFICAR EMPLEADO ===".center(10), "\n")
        print("¿Qué desea modificar?")
        print("1. Nombre del empleado")
        print("2. Horas trabajadas del empleado")
        print("3. Valor de la hora laboral del empleado")
        opcionUsuario = validarOpcionUsuario("   >> Escoja una opción (Ingrese 0 para regresar al menú): ", 0, 3)
        continuar = True
        
        
        #Iniciar el sub-programa que se encarga de editar un empleado según las opciones permitidas.
        while continuar:
            if opcionUsuario == 0:
                input("\nPresione cualquier tecla para regresar al menú principal...")
                return False
            
            else:
                keysEmpleados = list(dictEmpleados.keys())
                print(keysEmpleados) #EliminarLuego
                
                #Listar los empleados en pantalla
                print("\n")
                print("{:<7} {:<14} {:<35}".format("N°", "ID", "NOMBRE"))
                
                for i in range(len(keysEmpleados)):
                    print("{:<7} {:<14} {:<35}".format(i+1, keysEmpleados[i], dictEmpleados[keysEmpleados[i]]["nombre"]))
                
                empleadoEditar = validarOpcionUsuario(">> Ingrese el n° del empleado en la lista a modificar (Digite 0 para regresar al sub-menu): ", 0, len(keysEmpleados))
                
                
                #Validar si el usuario ya no desea editar ningún empleado
                if empleadoEditar == 0:
                    input("\nPresione cualquier tecla para regresar al sub-menú...")
                    break
                
                else:
                    if opcionUsuario == 1:
                        print(f"\nAnterior nombre: {dictEmpleados.get(keysEmpleados[empleadoEditar-1])['nombre']}")
                        nuevoNombre = validarNombre("Nuevo nombre: ", 2)
                        # Modificar el valor existente por el nuevo dato ingresado
                        dictEmpleados.get(keysEmpleados[empleadoEditar-1])["nombre"] = nuevoNombre
                        
                    elif opcionUsuario == 2:
                        print(f"\nAnterior cantidad de horas trabajadas: {dictEmpleados.get(keysEmpleados[empleadoEditar-1])['horasTrabajadas']} hrs")
                        nuevoHorasTrabajadas = validarHorasTrabajadas("Nueva cantidad de horas trabajadas: ", 1, 160)
                        # Modificar el valor existente por el nuevo dato ingresado
                        dictEmpleados.get(keysEmpleados[empleadoEditar-1])['horasTrabajadas'] = nuevoHorasTrabajadas
                    
                    elif opcionUsuario == 3:
                        print(f"\nAnterior valor de hora laboral: ${dictEmpleados.get(keysEmpleados[empleadoEditar-1])['valorHora']:,.0f} COP")
                        nuevoValorHora = validarValorHora("Nuevo valor de la hora laboral: ", 8000, 150000)
                        # Modificar el valor existente por el nuevo dato ingresado
                        dictEmpleados.get(keysEmpleados[empleadoEditar-1])['valorHora'] = nuevoValorHora
            
            # Verificar si el usuario desea seguir modificando información en el sistema, validando si antes el usuario  ha decidido regresar al submenú.
            continuarModificar = validarOpcionUsuario("¿Desea seguir modificando información? (1 SI / 0 NO): ", 0, 1)

            if continuarModificar == 1:
                continuar = False
                entrarSubMenu = True
            elif continuarModificar == 0:
                entrarSubMenu = False
                input("\nRegresando al menú principal...")
                break

def buscarEmpleado():
    pass


def eliminarEmpleado():
    pass


def listarEmpleados():
    pass


def listarNominaEmpleado():
    pass


def listarNominasTotalEmpleados():
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción (1-8)?: ")
    
    if opcionUsuario == 1:
        agregarEmpleado()
    
    elif opcionUsuario == 2:
        modificarEmpleado()
    
    elif opcionUsuario == 3:
        pass
    
    elif opcionUsuario == 4:
        pass
    
    elif opcionUsuario == 5:
        pass
    
    elif opcionUsuario == 6:
        pass
    
    elif opcionUsuario == 7:
        pass
    
    elif opcionUsuario == 8:
        isVerdadero = False
        print("Saliendo...")