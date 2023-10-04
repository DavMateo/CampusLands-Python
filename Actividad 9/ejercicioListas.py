# Este programa tiene como objetivo la gestión de la nómina de empleados para la empresa
# ACME mediante una serie de requerimientos que la misma empresa proporcionó.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
empleados = list()


# DEFINIENDO LAS FUNCIONES
def menu(msj):
    while True:
        try:
            print("\n", "*** NOMINA ACME ***", "\n", " " * 7, "MENU")
            print("\n1-  Agregar empleado")
            print("2-  Modificar empleado")
            print("3-  Buscar empleado")
            print("4-  Eliminar empleado")
            print("5-  Listar empleados")
            print("6-  Listar nómina de un empleado")
            print("7-  Listar nómina de todos los empleados")
            print("8-  Salir")
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < 1 or opcionUsuario > 8:
                print("Error: Debes elegir una opción válida (1-8).")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al digitar el número de opción. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Vuelva a intentarlo o comuníquese con un administrador.")
            

def agregarEmpleado(id, nombre, horasTrabajadas, ValorHora):
    empleados.append(id, nombre, horasTrabajadas, ValorHora)
    print(empleados, len(empleados))


def modificarEmpleado():
    pass


def eliminarEmpleado():
    pass



# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("    >> Escoja una opción (1-8)?: ")
    print(opcionUsuario)
    
    if opcionUsuario == 1:
        # Validación ID del empleado
        while True:
            try:
                id = int(input("Ingrese el id: "))
                
                if id < 0:
                    print("Error: introduzca un valor de ID válido (No negativos, sólo números positivos enteros).")
                    continue
                break
            
            except ValueError:
                print("Ha ocurrido un error al ingresar el ID. Inténtelo de nuevo.")
            except:
                print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
        
        
        while True:
            try:
                nombre = input("Ingrese el nombre: ").strip()
                nombreArray = nombre.split(" ")
                
                for i in nombreArray:
                    if i == " ":
                        nombreArray.pop(i)
                
            except Exception as e:
                print(f"Ha ocurrido un problema al ingresar el nombre. Error: {e}")
            except:
                print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
    break