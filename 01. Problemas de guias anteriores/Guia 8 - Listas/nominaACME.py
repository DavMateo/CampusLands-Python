# Este programa está destinado para ACME, (empresa mencionado en el ejercicio) donde se podrá
# realizar multiples acciones, como agregar, modificar o eliminar usuarios del sistema. Todo 
# esto lleva al enfoque principal, que es el de gestionar la nómina de sus empleados.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
listaEmpleados = []


# DECLARANDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(text, min):
    while True:
        try:
            pass
            
        except Exception as e:
            print("Ha ocurrido un error al ingresar el nombre. Inténtelo de nuevo.")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


# DECLARANDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcion = int(input(msj))
            
            if opcion < int(min) or opcion > int(max):
                print(f"Error: Ingresa un valor numérico válido ({min}-{max}).\n")
                continue
            return opcion
        
        except ValueError:
            print("Ha ocurrio un error al ingresar su opción. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarId(idEmpl, min):
    while True:
        try:
            id = int(input(idEmpl))
            
            if id < min:
                print(f"Error: Debes ingresar un número igual o superior a {min}\n")
                continue
            return id
        
        except ValueError:
            print("Ha ocurrido un error al registrar el ID. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")
    
    # QUEDÉ AQUÍ


def validarNombre(msj):
    while True:
        try:
            nombre = input(msj).strip()
            nombreArray = nombre.split(" ")
            nombreArrayFiltrado = []
            
            for n in nombreArray:
                if n != "":
                    nombreArrayFiltrado.append(n)
            
            nombreFiltradoValidar = "".join(nombreArrayFiltrado).lower()
            nombreFinal = " ".join(nombreArrayFiltrado).title()
            
            if len(nombreArray) < 2:
                print(f"Error: Debes ingresar al menos 1 nombre y 1 apellido.\n")
                continue

            elif len(nombreFiltradoValidar) == 0:
                print("Error: Has ingresado un nombre vacío.")
                continue
                
            elif not nombreFiltradoValidar.isalnum():
                print("Error: El nombre no puede tener caracteres especiales.\n")
                continue
            
            elif nombreFiltradoValidar.isdigit():
                print("Error: El nombre no puede contener solo números.\n")
                continue
            return nombreFinal
        
        except Exception as e:
            print("Ha ocurrido un error al ingresar el nombre. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarHorasTrabajadas(hrs, min, max):
    while True:
        try:
            horas = int(input(hrs))
            
            if horas < min or horas > max:
                print(f"Error: Ingrese un valor numérico positivo dentro del rango permitido ({min}-{max})\n")
                continue
            return horas
        
        except ValueError:
            print("Ha ocurrido un error al ingresar las horas laboradas. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarValorHora(valHr, min, max):
    while True:
        try:
            valorHora = float(input(valHr))
            
            if valorHora < min or valorHora > max:
                print(f"Error: Ingrese un valor válido dentro del rango permitido (${min} - ${max}).\n")
                continue
            return valorHora
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el valor de la hora laboral. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


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
    print("\n", "*** AGREGAR EMPLEADO ***")
    
    id = validarId(idEmpl, 1)
    nombre = validarNombre(nombreEmpl)
    horasTrabajadas = validarHorasTrabajadas(hrsTrabajoEmpl, 1, 160)
    valorHora = validarValorHora(valorHoraEmpl, 8000, 150000)
    
    listaEmpleados.append([id, nombre, horasTrabajadas, valorHora])
    print("\n", id, nombre, horasTrabajadas, valorHora)
    print(listaEmpleados)


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
        print("¡Gracias por usar nuestro software! Saliendo...")
        isVerdadero = False