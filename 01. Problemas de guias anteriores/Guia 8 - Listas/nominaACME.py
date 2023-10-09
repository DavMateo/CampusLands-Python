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


def encontrarEmpleado(msj, min):
    idBuscar = validarId(msj, min)
    
    if idBuscar == 0:
        return [idBuscar]
    
    for i in range(len(listaEmpleados)):
        for j in range(len(listaEmpleados[i])):
            if listaEmpleados[i][j] == idBuscar:
                posicion1 = i
                posicion2 = j
                checked = True
    
    print(posicion1, posicion2, checked)
    
    return [idBuscar, posicion1, posicion2, checked]


def existenEmpleados():
    cantidadEmpleados = len(listaEmpleados)
    
    if cantidadEmpleados == 0:
        return False
    elif cantidadEmpleados >= 1:
        return True


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
            
            if id < int(min):
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
            
            if horas < int(min) or horas > int(max):
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
            
            if valorHora < int(min) or valorHora > int(max):
                print(f"Error: Ingrese un valor válido dentro del rango permitido (${min} - ${max}).\n")
                continue
            return valorHora
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el valor de la hora laboral. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DECLARANDO LAS FUNCIONES NECESARIAS
def menu(msj):
    print("\n\n", "*** NOMINA ACME ***")
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
    print("Ingrese la siguiente información sobre el nuevo empleado:")
    
    id = validarId(idEmpl, 1)
    nombre = validarNombre(nombreEmpl)
    horasTrabajadas = validarHorasTrabajadas(hrsTrabajoEmpl, 1, 160)
    valorHora = validarValorHora(valorHoraEmpl, 8000, 150000)
    
    listaEmpleados.append([id, nombre, horasTrabajadas, valorHora])
    print("\n", id, nombre, horasTrabajadas, valorHora)
    print(listaEmpleados)


def modificarEmpleado(msj):
    continuar = True
    cantidadEmpleados = existenEmpleados()
    print("\n\n", "*** MODIFICAR EMPLEADO ***")
    
    # Validar si existe algún empleado añadido a la lista de empleados.
    if not cantidadEmpleados:
        print("\nError: Imposible acceder a este sub-programa.")
        print("Motivo: No hay usuarios añadidos al sistema.")
        input()
        return
        
    while continuar:
        print("\n¿Qué información del empleado desea modificar?")
        print("1. Modificar el nombre")
        print("2. Modificar las horas trabajadas")
        print("3. Modificar el valor de la hora")
        opcionUsuario = validarOpcionUsuario(msj, 0, 3)
        
        if opcionUsuario == 0:
            break
        
        # Listar los empleados a modificar
        print("\n{:<7} {:<14} {:<30}".format("N°", "ID", "Nombre"))
        
        for i in range(len(listaEmpleados)):
            print("{:<7} {:<14} {:<30}".format(f"{i+1}", listaEmpleados[i][0], listaEmpleados[i][1]))
            
        elegirEmpleado = validarOpcionUsuario("\n  >> ¿Cuál es el número (N°) del empleado a modificar? Escriba 0 para salir al submenú: ", 0, i+1)
        
        
        # Verificar que el usuario no haya desistido
        if elegirEmpleado == 0:
            continue
        
        
        # Modificar el nombre de un empleado        
        if opcionUsuario == 1:
            print(f"\nNombre anterior: {listaEmpleados[elegirEmpleado-1][1]}")
            nuevoNombre = validarNombre("Nuevo nombre: ")
            
            listaEmpleados[elegirEmpleado-1][1] = nuevoNombre
        
        # Modificar las horas trabajadas de un empleado
        elif opcionUsuario == 2:
            print(f"\nHoras trabajadas anterior: {listaEmpleados[elegirEmpleado-1][2]}")
            nuevasHorasTrabajadas = validarHorasTrabajadas("Nueva cantidad de horas trabajadas: ", 1, 160)
            
            listaEmpleados[elegirEmpleado-1][2] = nuevasHorasTrabajadas
            
        # Modificar el valor de la hora de un empleado
        elif opcionUsuario == 3:
            print(f"\nValor de la Hora anterior: {listaEmpleados[elegirEmpleado-1][3]}")
            nuevoValorHora = validarHorasTrabajadas("Nuevo valor de la hora para el empleado: ", 8000, 150000)
            
            listaEmpleados[elegirEmpleado-1][3] = nuevoValorHora
        
        # Validar si el usuario desea modificar otro usuario
        continuarModificar = validarOpcionUsuario("¿Deseas modificar algún otro usuario? (1 SI / 0 NO): ", 0, 1)
        
        if continuarModificar == 1:
            continuar = True
        elif continuarModificar == 0:
            continuar = False


def buscarEmpleado(msj, validar):
    continuar = True
    cantidadEmpleados = existenEmpleados()
    
    # Condicional if-else para que muestre o no el mensaje del sub-programa al iniciarse
    if validar:
        pass
    else:
        print("\n\n", "*** BUSCAR EMPLEADO ***")
        
    # Validar si existe algún empleado añadido a la lista de empleados.
    if not cantidadEmpleados:
        print("Error: Imposible acceder a esta parte del programa.")
        print("Motivo: No hay usuarios añadidos al sistema.")
        input()
        return
    
    while continuar:
        eliminarEmpleado = validar
        valorRetornado = encontrarEmpleado(msj, 0)
        
        if len(valorRetornado) == 1:
            idBuscar, = valorRetornado
        
        else:
            idBuscar, posicion1, posicion2, checked = valorRetornado
        
        
        # Verifica si el usuario desea salir o no del sub-programa
        if idBuscar == 0:
            continuar = False
            return None
                
        
        # Comprueba si el ID ingresado existe en el sistema      
        if not checked:
            print(f"\nEl empleado con el ID '{idBuscar}' no ha sido ingresado.")
            continue
        
        else:
            if eliminarEmpleado:
                return [idBuscar, posicion1, posicion2]
            
            # En caso de que no se quiera eliminar un usuario entonces buscará el usuario.
            else:
                idInfo, nombreInfo, horasTrabajadasInfo, valorHoraInfo = listaEmpleados[posicion1]
                
                print(f"\n=== ID {idInfo} ===")
                print("Nombre:", nombreInfo)
                print(f"Horas trabajadas: {horasTrabajadasInfo} hrs")
                print(f"Valor de la hora: ${valorHoraInfo:,.0f} COP")
                input()
        
        
        continuarBuscar = validarOpcionUsuario("¿Desea buscar otro empleado? (1 SI / 0 NO): ", 0, 1)
        
        if continuarBuscar == 1:
            continuar = True
        elif continuarBuscar == 0:
            continuar = False


def eliminarEmpleado(msj, validar):
    continuar = True
    print("\n", "*** ELIMINAR EMPLEADO ***")
    
    while continuar:
        empleadoEliminado = buscarEmpleado(msj, validar)
        
        if empleadoEliminado == None:
            return
        
        else:
            # Pequeña validación para asegurarse que no hayan errores (Poco probable, pues ya se valida
            # información antes de entrar por esta nueva validación).
            while True:
                try:
                    idBuscar, posicion1, posicion2 = empleadoEliminado
                    elementoEliminado = listaEmpleados.pop(posicion1)
                    
                    if len(elementoEliminado) == 0 or not elementoEliminado:
                        print("El usuario no se ha eliminado como debía. Inténtelo de nuevo.")
                        continue
                    break
                
                except Exception as e:
                    print("Mensaje de Error:", {e})
        
        print(f"\n¡El empleado '{elementoEliminado[1]}' con ID de '{elementoEliminado[0]}' ha sido eliminado correctamente!")
        
        
        # Determinar si el usuario desea continuar eliminando empleados del sistema.
        continuarEliminar = validarOpcionUsuario("¿Desea eliminar otro empleado? (1 SI / 0 NO): ", 0, 1)
        
        if continuarEliminar == 1:
            continuar = True
        elif continuarEliminar == 0:
            continuar = False
    
    return elementoEliminado


def listarEmpleados(msj):
    pass


def listarNominaEmpleado(msj):
    pass


def listarNominas(msj):
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Ingrese una opción (1-8): ")
    
    if opcionUsuario == 1:
        agregarEmpleado("ID: ", "Nombre: ", "Horas Trabajadas: ", "Valor de la Hora: ")
    
    elif opcionUsuario == 2:
        modificarEmpleado("  >> Elija una opción (1-3) o elija 0 para salir al menú: ")
    
    elif opcionUsuario == 3:
        buscarEmpleado("Ingrese el ID del empleado a buscar (Escriba 0 para volver al menú): ", False)
    
    elif opcionUsuario == 4:
        empleadoBorrado = eliminarEmpleado("Ingrese el ID del empleado que desea eliminar (Escriba 0 para volver al menú): ", True)
    
    elif opcionUsuario == 5:
        pass
    
    elif opcionUsuario == 6:
        pass
    
    elif opcionUsuario == 7:
        pass
    
    elif opcionUsuario == 8:
        print("\n¡Gracias por usar nuestro software! Saliendo...")
        isVerdadero = False