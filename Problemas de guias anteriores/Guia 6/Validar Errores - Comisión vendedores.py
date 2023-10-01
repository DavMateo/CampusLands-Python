# Programa para determinar la comisión de un vendedor de acuerdo a 
# parámetros establecidos por la compañía misma. Se validarán 
# los datos ingresados por el usuario y personalizará los posibles errores.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
nombreFiltradoFinal = ""


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
            nombreFiltradoArray = []
            
            #Algoritmo para evitar que "split()" cuente un espacio como parte del Array
            for i in range(len(nombreArray)):
                if nombreArray[i] != "":
                    nombreFiltradoArray.append(nombreArray[i])
            
            nombreFiltradoFinal += " ".join(nombreFiltradoArray)
            
            #Validación del nombre ingresado
            if len(nombreFiltradoArray) < 2 or nombreFiltradoFinal.isalnum() == False:
                print("Error: Ingresa al menos un nombre y un apellido. Solo letras.")
                continue
            break
            
        except:
            print("Algo ha ido mal, inténtalo de nuevo.")