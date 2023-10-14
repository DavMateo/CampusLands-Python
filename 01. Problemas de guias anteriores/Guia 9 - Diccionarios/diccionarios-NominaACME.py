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
    print("\n\n", "=== MODIFICAR EMPLEADO ===".center(10), "\n")
    
    print("¿Qué desea modificar?")
    print("1. Nombre del empleado")
    print("2. Horas trabajadas del empleado")
    print("3. Valor de la hora laboral del empleado")
    opcionUsuario = validarOpcionUsuario("   >> Escoja una opción (Ingrese 0 para regresar al menú): ", 0, 3)
    
    
    if opcionUsuario == 0:
        input("Presione cualquier tecla para regresar al menú principal...")
        return
    
    else:
        keysEmpleados = list(dictEmpleados.keys())
        print(keysEmpleados) #EliminarLuego
        
        #Listar los empleados en pantalla
        print("\n")
        print("{:<7} {:<14} {:<35}".format("N°", "ID", "NOMBRE"))
        
        for i in range(len(keysEmpleados)):
            print("{:<7} {:<14} {:<35}".format(i+1, keysEmpleados[i], dictEmpleados[keysEmpleados[i]]["nombre"]))
        
        
        if opcionUsuario == 1:
            pass
        
        elif opcionUsuario == 2:
            pass
        
        elif opcionUsuario == 3:
            pass
    

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