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


def calculoCombinatoria(msj):
    # La combinatoria es una rama de las matemáticas que trata de contar, organizar y seleccionar
    # objetos sin considerar un orden en específico. Se ocupa con el conteo de números de tal 
    # manera para elegir u organizar elementos de un conjunto. Un concepto importante en la 
    # combinatoria es el concepto de "Combinaciones".
    # 
    # Una combinación de un conjunto de elementos es la selección de esos elementos donde su 
    # orden no importa. La fórmula para calcular el número de combinaciones (denotado como "C(n, k)")
    # desde un conjunto de "n" elementos, eligiendo "k" elementos al mismo tiempo, está dada por:
    # (Ver fórmula en la guía).
    #
    # Esta fórmula calcula el número de veces que se puede elegir "k" elemenots desde un conjunto de
    # "n" elementos sin considerar su orden. Las combinaciones son comúnmente usadas en probabilidad, 
    # estadística, y varios problemas de cálculo en las matemáticas y la ciencia.
    
    while True:
        try:
            pass
        except:
            pass


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



# ESTRUCTURA DEL PROGRAMA
opcionUsuario = menu("   >> Escoja una opción (1-4): ")

if opcionUsuario == 1:
    resultadoCombinatoria = calculoCombinatoria("Valor: ")

elif opcionUsuario == 2:
    pass

elif opcionUsuario == 3:
    pass

elif opcionUsuario == 4:
    pass