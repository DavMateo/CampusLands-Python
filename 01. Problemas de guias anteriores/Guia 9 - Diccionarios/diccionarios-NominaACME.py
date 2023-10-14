# Este programa está destinado para ACME, (empresa mencionado en el ejercicio) donde se podrá
# realizar multiples acciones, como agregar, modificar o eliminar usuarios del sistema. Todo 
# esto lleva al enfoque principal, que es el de gestionar la nómina de sus empleados.


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
dictEmpleados = {}
smmlv = 1160000
subsidioTransporte = 140606


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS



# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes elegir una opción dentro del rango válido ({min}-{max}).")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción elegida. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validarId(msj, min):
    pass


def validarNombre(msj, min):
    pass


def validarHorasTrabajadas(msj, min, max):
    pass


def validarValorHora(msj, min, max):
    pass


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("")
    print("*** NOMINA ACME ***".center(30))
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


def modificarEmpleado():
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
        pass
    
    elif opcionUsuario == 7:
        pass
    
    elif opcionUsuario == 8:
        isVerdadero = False
        print("Saliendo...")