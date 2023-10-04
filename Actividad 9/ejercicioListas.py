# Este programa tiene como objetivo la gestión de la nómina de empleados para la empresa
# ACME mediante una serie de requerimientos que la misma empresa proporcionó.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
empleados = list()


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN DE DATOS
def validacionID(id):
    while True:
        try:
            id = int(input("\nIngrese el id: "))
            
            if id < 0:
                print("Error: introduzca un valor de ID válido (No negativos, sólo números positivos enteros).")
                continue
            return id
                
        except ValueError:
            print("Ha ocurrido un error al ingresar el ID. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validacionNombre(nombre):
    while True:
        try:
            nombre = input("\nIngrese el nombre: ").strip()
            nombreArray = nombre.split(" ")
            nombreArrayFiltrado = []
            
            # Algoritmo para filtrar la entrada del nombre para su posterior validación.
            for i in range(len(nombreArray)):
                if nombreArray[i] != "":
                    nombreArrayFiltrado.append(nombreArray[i])
            nombreValidar = "".join(nombreArrayFiltrado)
            
            if len(nombreArrayFiltrado) < 2 or len(nombreValidar) == 0 or nombreValidar.isalnum() == False:
                print("Error: Debes ingresar un nombre válido.")
                continue

            nombreFinal = " ".join(nombreArrayFiltrado).title()
            return nombreFinal
        
        except Exception as e:
            print(f"Ha ocurrido un problema al ingresar el nombre. Error: {e}")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validacionHorasTrabajadas(horasTrabajadas):
    while True:
        try:
            horasTrabajadas = int(input("\nIngrese las horas trabajadas: "))
            
            if horasTrabajadas < 1 or horasTrabajadas > 160:
                print("Error: Debes ingresar un valor entero numérico entre 1 y 160.")
                continue
            return horasTrabajadas
        
        except ValueError:
            print("Ha ocurrido un error al ingresar las horas trabajadas. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validacionValorHora(valorHora):
    while True:
        try:
            valorHora = int(input("\nIngrese el valor de la hora: "))
            
            if valorHora < 8000:
                print("Error: El valor de la hora no puede ser menor a $8.000 COP.")
                continue
            
            elif valorHora > 150000:
                print("Error: El valor de la hora no puede ser superior a $150.000 COP.")
                continue
            return valorHora
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el valor de la hora. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validacionContinuar(msj):
    while True:
        try:
            confirmacion = input(msj).lower()

            if confirmacion != "s" and confirmacion != "n":
                print("Error: Introduce una opción válida (S para Si o N para No).")
                continue

            if confirmacion == "s":
                return True

            elif confirmacion == "n":
                print("Regresando al menú principal...")
                return False
            break
        
        except Exception as e:
            print(f"Ha ocurrido un problema al ingresar la opción. Error {e}")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS A LAS FUNCIONES DE LOS ENUNCIADOS
def buscarEmpleado(empleado):
    respuesta = []
    
    for i in range(len(empleados)):
        sublista = empleados[i][0]
        print("XD")
        print(sublista) 
        respuesta.append(sublista)
    
    respuesta.insert(0, True)
    return respuesta


def listarEmpleadosModificar():
    informacionEmpleadosModificar = list()
    
    for i in range(len(empleados)):
        idEmpleado = empleados[i][0]
        nombreEmpleado = empleados[i][1]

        informacionEmpleadosModificar.append([idEmpleado, nombreEmpleado])
    
    return informacionEmpleadosModificar


def desempaquetarInfoEmpleados(lista):
    print("\n", "ID\t\t\t", "NOMBRE")
    
    for i in range(len(lista)):
        print("\n", lista[i][0], "\t", lista[i][1])


# DEFINIENDO LAS FUNCIONES DE LOS ENUNCIADOS
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
            

def agregarEmpleado(id, nombre, horasTrabajadas, valorHora):
    empleados.append([id, nombre, horasTrabajadas, valorHora])
    return True


def modificarEmpleado(opcionModificar):  
    modificar = True
    
    while modificar:
        if opcionModificar == 1:
            informacionEmpleadoModificar = listarEmpleadosModificar()
            desempaquetarInfoEmpleados(informacionEmpleadoModificar)
            
            modificar = validacionContinuar("\n¿Desea realizar otra modificación? (S/N): ")
            
        elif opcionModificar == 2:
            informacionEmpleadoModificar = listarEmpleadosModificar()
            desempaquetarInfoEmpleados(informacionEmpleadoModificar)

            modificar = validacionContinuar("\n¿Desea realizar otra modificación? (S/N): ")
        
        elif opcionModificar == 3:
            informacionEmpleadoModificar = listarEmpleadosModificar()
            desempaquetarInfoEmpleados(informacionEmpleadoModificar)

            modificar = validacionContinuar("\n¿Desea realizar otra modificación? (S/N): ")
        
        elif opcionModificar == 4:
            modificar = False
            input("\nRegresando al menú. Presione cualquier tecla para continuar...")


def eliminarEmpleado():
    pass


def listarEmpleados():
    pass



# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("    >> Escoja una opción (1-8)?: ")
    
    if opcionUsuario == 1:
        isContinuar = True
        print("\n", "*** AGREGAR EMPLEADO ***")
        
        while isContinuar:
            # Validación ID del empleado
            id = validacionID("\nIngrese el id: ")
            
            
            # Validación Nombre del empleado
            nombre = validacionNombre("\nIngrese el nombre: ")
            
            
            # Validación horas trabajadas
            horasTrabajadas = validacionHorasTrabajadas("\nIngrese las horas trabajadas: ")
            
            
            # Validación valor de la hora
            valorHora = validacionValorHora("\nIngrese el valor de la hora: ")

            # Invocando y almacenando el valor de retorno de la función "agregarEmpleado()"
            resultado = agregarEmpleado(id, nombre, horasTrabajadas, valorHora)
            
            if resultado:
                print("\n¡Se ha agregado el nuevo usuario con éxito!")
            
            
            while True:
                try:
                    continuar = input("¿Desea agregar otro usuario? (S/N): ").lower()

                    if continuar != "s" and continuar != "n":
                        print("Error: Introduce una opción válida (S para Sí o N para No).")
                        continue
                
                    if continuar == "s":
                        isContinuar = True
                        
                    elif continuar == "n":
                        isContinuar = False
                        input("Presione cualquier tecla para regresar al menú...")
                    break
                
                except Exception as e:
                    print("Ha ocurrido un error al ingresar su opción. Inténte de nuevo.")
                except:
                    print("Ha ocurrido un error desconocido. Inténtelo de nuevo o comuníquese con un administrador.")
    
    elif opcionUsuario == 2:
        print("\n", "*** MODIFICAR EMPLEADO ***")
        
        while True:
            try:
                print("\n", "==== OPCIONES MODIFICAR ====")
                print("1. Modificar el nombre de un empleado")
                print("2. Modificar la cantidad de horas de un empleado")
                print("3. Modificar el valor de la hora de un empleado")
                print("4. Regresar al menú")
                opcionModificar = int(input("    >>> "))
                
                if opcionModificar < 1 or opcionModificar > 4:
                    print("Error: Debes ingresar una opción válida (1-4).")
                    continue
                break
            
            except ValueError:
                print("Ha ocurrido un error al ingresar la opción. Inténtelo de nuevo.")
            except:
                print("Ha ocurrido un error inesperado al ingresar la opción. Inténtelo de nuevo o comuníquese con un administrador.")
        
        modificarEmpleado(opcionModificar)
    
    elif opcionUsuario == 3:
        print("\n", "*** BUSCAR EMPLEADO ***")
    
    
    elif opcionUsuario == 4:
        print("\n", "*** ELIMINAR EMPLEADO ***")
    
    
    elif opcionUsuario == 5:
        print("\n", "*** LISTAS EMPLEADO ***")
    
    
    elif opcionUsuario == 6:
        print("\n", "*** LISTAR LA NÓMINA DE UN EMPLEADO ***")
    
    
    elif opcionUsuario == 7:
        print("\n", "*** LISTAR NÓMINA DE TODOS LOS EMPLEADOS ***")
    
    
    elif opcionUsuario == 8:
        print("\n", "*** SALIR ***")
        isVerdadero = not validacionContinuar("¿Desea salir de la aplicación? (S/N): ")
        

print("\n\n¡Gracias por usar nuestra aplicación!")