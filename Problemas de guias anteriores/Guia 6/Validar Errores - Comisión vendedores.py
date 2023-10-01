# Programa para determinar la comisión de un vendedor de acuerdo a 
# parámetros establecidos por la compañía misma. Se validarán 
# los datos ingresados por el usuario y personalizará los posibles errores.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True


# DEFINIR LA ESTRUCTURA WHILE DEL PROGRAMA
while isVerdadero:
    #Comprobación cédula de ciudadanía
    while True:
        try:
            cedula = input("\nIngrese la cédula de ciudadanía: ").strip()

            if int(cedula) == -1:
                print("\n¡Gracias por usar nuestro programa!")
                isVerdadero = False
                break
            else:
                if len(cedula) < 4 or len(cedula) > 12 or cedula.isalpha() or int(cedula) < 0:
                    print("Error: Introduce un valor numérico positivo y que contenga entre 4 a 12 números.")
                    continue
                break
        
        except ValueError:
            print("Error: Ingresa un número entero válido.")
        except Exception as e:
            print(f"\nHa ocurrido un problema al digitar su cédula de ciudadanía. \nError: {e}")
        except:
            print("Algo ha ido mal. Asegúrate de ingresar solo valores válidos.")
    
    
    
    #Validación del nombre
    while isVerdadero:
        try:
            nombre = input("Ingrese el nombre: ").strip()
            nombreArray = nombre.split(" ")
            nombreFiltradoArray = []    #Creando una lista vacía
            
            #Algoritmo para evitar que "split()" cuente un espacio como parte del Array
            for i in range(len(nombreArray)):
                if nombreArray[i] != "":
                    nombreFiltradoArray.append(nombreArray[i])
            
            #Seteo la variable en vacío antes de agregarle información para evitar 
            #sobreescrituras no deseadas
            nombreFiltradoFinal = ""
            nombreFiltradoFinal += " ".join(nombreFiltradoArray)
            
            
            #Validación del nombre ingresado
            if len(nombreFiltradoArray) < 2 or nombreFiltradoFinal.isalnum():
                print("Error: Ingresa al menos un nombre y un apellido. Solo letras.")
                continue
            break
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el nombre, inténtelo de nuevo.")
        except:
            print("Algo ha ido mal, inténtalo de nuevo.")
    
    
    
    #Verificación del tipo de vendedor
    while isVerdadero:
        try:
            tipoVendedor = int(input("Ingrese el tipo de vendedor: 1 Puerta a puerta, 2 Telemercadeo o 3 Ejecutivo de ventas: "))
            
            if tipoVendedor < 1 or tipoVendedor > 3:
                print("Error: Elije una opción válida (1, 2 o 3).")
                continue
            break
        
        except ValueError:
            print("Ha ocurrido un error en la digitación de la opción. Inténtalo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtalo de nuevo o ponte en contacto con un administrador.")
    
    
    
    #Validar el valor de las ventas en el mes
    