# Este programa contendrá una serie de pequeños programas donde el usuario
# pueda elegir alguno de los problemas solucionados mediante un menú y que se 
# ejecute ese ejercicio en específico.


# DEFINICIÓN DE FUNCIONES
def menu(msj):
    while True:
        try:
            print("\n", "===== MENU =====")
            print("1- Cálculo de la combinatoria")
            print("2- Convertir texto a número")
            print("3- Calcular el IVA de una factura")
            print("4- Salir")
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < 1 or opcionUsuario > 4:
                print("Error: Debes ingresar una opción válida (1-4).")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error en la digitación del número.")
        except:
            print("Ha ocurrido un problema inesperado. Inténtelo de nuevo o pongase en contacto con el administrador.")


def calculoCombinatoria(n, k):
    while True:
        try:
            valorN = int(input(n))
            valorK = int(input(k))
            
            if valorN < 0 or valorK < 0:
                print("Error: No puedes ingresar números negativos. Ingresa números positivos.\n")
                continue
            elif valorN < valorK:
                print("Error: El total de elementos debe ser mayor a los elementos por grupo.\n")
                continue
            
            combinacionResultado = factorial(valorN) / (factorial(valorN-valorK) * factorial(valorK))
            return combinacionResultado
        
        except ValueError:
            print("Ha ocurrido un problema al ingresar los números. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Es probable que la salida contenga un número muy elevado.")
            print("Inténtelo de nuevo o póngase en contacto con el administrador.\n")
            

def factorial(num):
    resultadoFactorial = 1
    
    for i in range(1, num + 1):
        resultadoFactorial *=  i
    
    return resultadoFactorial


def textoNumero(msj):
    while True:
        try:
            pass
        except:
            pass


def ivaFactura(msj):
    while True:
        try:
            pass
        except:
            pass



# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True


# ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción (1-4): ")

    if opcionUsuario == 1:
        print("\n", "==== Indicaciones ====")
        print("En la fórmula de combinaciones el valor N indica el total de elementos y el valor K los elementos por grupos.\n")    
        resultadoCombinatoria = calculoCombinatoria("Valor n: ", "Valor k: ")

        print("\n", "**** RESULTADO ****")
        print(f"Puedes realizar: C(n,k) = {resultadoCombinatoria:.0f} combinaciones distintas.")
        input("Presione \"enter\" para continuar: ")

    elif opcionUsuario == 2:
        pass

    elif opcionUsuario == 3:
        pass

    elif opcionUsuario == 4:
        isVerdadero = False