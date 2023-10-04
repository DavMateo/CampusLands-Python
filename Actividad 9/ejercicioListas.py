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
            

def agregarEmpleado(id, nombre, horasTrabajadas, valorHora):
    empleados.append([id, nombre, horasTrabajadas, valorHora])
    return True


def modificarEmpleado():
    pass


def eliminarEmpleado():
    pass



# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("    >> Escoja una opción (1-8)?: ")
    
    if opcionUsuario == 1:
        isContinuar = True
        
        while isContinuar:
            # Validación ID del empleado
            while True:
                try:
                    id = int(input("\nIngrese el id: "))
                    
                    if id < 0:
                        print("Error: introduzca un valor de ID válido (No negativos, sólo números positivos enteros).")
                        continue
                    break
                
                except ValueError:
                    print("Ha ocurrido un error al ingresar el ID. Inténtelo de nuevo.")
                except:
                    print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
            
            
            # Validación Nombre del empleado
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
                    break
                
                except Exception as e:
                    print(f"Ha ocurrido un problema al ingresar el nombre. Error: {e}")
                except:
                    print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
            
            
            # Validación horas trabajadas
            while True:
                try:
                    horasTrabajadas = int(input("\nIngrese las horas trabajadas: "))
                    
                    if horasTrabajadas < 1 or horasTrabajadas > 160:
                        print("Error: Debes ingresar un valor entero numérico entre 1 y 160.")
                        continue
                    break
                
                except ValueError:
                    print("Ha ocurrido un error al ingresar las horas trabajadas. Inténtelo de nuevo.")
                except:
                    print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
            
            
            # Validación valor de la hora
            while True:
                try:
                    valorHora = int(input("\nIngrese el valor de la hora: "))
                    
                    if valorHora < 8000:
                        print("Error: El valor de la hora no puede ser menor a $8.000 COP.")
                        continue
                    
                    elif valorHora > 150000:
                        print("Error: El valor de la hora no puede ser superior a $150.000 COP.")
                        continue
                    break
                
                except ValueError:
                    print("Ha ocurrido un error al ingresar el valor de la hora. Inténtelo de nuevo.")
                except:
                    print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")

            # Invocando y almacenando el valor de retorno de la función "agregarEmpleado()"
            resultado = agregarEmpleado(id, nombreFinal, horasTrabajadas, valorHora)
            
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
                    break
                
                except Exception as e:
                    print("Ha ocurrido un error al ingresar su opción. Inténte de nuevo.")
                except:
                    print("Ha ocurrido un error desconocido. Inténtelo de nuevo o comuníquese con un administrador.")

    
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
        while True:
            try:
                confirmacion = input("¿Desea salir de la aplicación? (S/N): ").lower()
                
                if confirmacion != "s" and confirmacion != "n":
                    print("Error: Introduce una opción válida (S para Si o N para No).")
                    continue
        
                if confirmacion == "s":
                    print("\n\n¡Gracias por usar nuestra aplicación!")
                    isVerdadero = False
                    
                elif confirmacion == "n":
                    print("Regresando al menú principal...")
                    isVerdadero = True
                break
            
            except Exception as e:
                print(f"Ha ocurrido un problema al ingresar la opción. Error {e}")
            except:
                print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")