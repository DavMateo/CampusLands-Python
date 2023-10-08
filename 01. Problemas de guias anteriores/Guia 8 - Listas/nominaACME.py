# Este programa está destinado para ACME, (empresa mencionado en el ejercicio) donde se podrá
# realizar multiples acciones, como agregar, modificar o eliminar usuarios del sistema. Todo 
# esto lleva al enfoque principal, que es el de gestionar la nómina de sus empleados.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True


# DECLARANDO LAS FUNCIONES COMPLEMENTARIAS



# DECLARANDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcion = int(input(msj))
            
            if opcion < int(min) or opcion > int(max):
                print(f"Error: Ingresa un valor numérico válido ({min}-{max}).")
                continue
            return opcion
        
        except ValueError:
            print("Ha ocurrio un error al ingresar su opción. Inténtelo de nuevo.")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validarId(idEmpl, min):
    while True:
        try:
            id = int(input(idEmpl))
            
            if id < min:
                print(f"Error: Debes ingresar un número igual o superior a {min}")
                continue
            return id
        
        except ValueError:
            print("Ha ocurrio un error al registrar el ID. Inténtelo de nuevo.")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
    
    # QUEDÉ AQUÍ


def validarNombre():
    pass


def validarHorasTrabajadas():
    pass


def validarValorHora():
    pass


# DECLARANDO LAS FUNCIONES NECESARIAS
def menu(msj):
    print("\n", "*** NOMINA ACME ***")
    print(" " * 8, "MENÚ")
    
    print("\n1. Agregar empleado")
    print("2. Modificar empleado")
    print("3. Buscar empleado")
    print("4. Eliminar empleado")
    print("5. Listar empleados")
    print("6. Listar nómina de un empleado")
    print("7. Listar nómina de todos los empleados")
    print("8. Salir")
    
    return validarOpcionUsuario(msj, 1, 8)


def agregarEmpleado(idEmpl, nombreEmpl, hrsTrabajoEmpl, valorHoraEmpl):
    id = validarId(idEmpl, 1)
    nombre = validarNombre(nombreEmpl)
    horasTrabajadas = validarHorasTrabajadas(hrsTrabajoEmpl)
    valorHora = validarValorHora(valorHoraEmpl)


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


def listarNominas():
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Ingrese una opción (1-8): ")
    
    if opcionUsuario == 1:
        print("Ingrese la siguiente información sobre el nuevo empleado:")
        agregarEmpleado("ID: ", "Nombre: ", "Horas Trabajadas: ", "Valor de la Hora: ")
    
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