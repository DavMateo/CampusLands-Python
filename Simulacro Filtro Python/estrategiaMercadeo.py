# Este programa permite agregar, modificar, eliminar y listar de forma ascendente varios 
# productos usando paginación. El software está destinado a la empresa ACME.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
listaProductos = []


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarID(msj):
    while True:
        try:
            pass

        except:
            print("")


def validarNombre(msj):
    while True:
        try:
            pass

        except:
            print("")


def validarPrecio(msj):
    while True:
        try:
            pass

        except:
            print("")


def validarCantidad(msj):
    while True:
        try:
            pass

        except:
            print("")


# DEFINIENDO LAS FUNCIONES PERTINENTES
def menu(msj):
    print("\n")
    print("=" * 18)
    print("  PRODUCTOS ACME")
    print("=" * 18)
    
    print("\n1. Agregar producto")
    print("2. Modificar producto")
    print("3. Eliminar producto")
    print("4. Listar varios productos")
    print("5. Estrategia de mercadeo")
    print("6. Salir")
    
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < 1 or opcionUsuario > 6:
                print("\nError: Introduce una opción válida (1-6).")
                continue
            return opcionUsuario
        
        except ValueError:
            print("\nHa ocurrido un error al ingresar la opción. Inténtelo de nuevo.")
        except:
            print("\nHa ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def agregarProducto():
    pass


def modificarProducto():
    pass


def eliminarProducto():
    pass


def listarProductos():
    pass


def estrategiaMercadeo():
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción (1-6): ")
    
    if opcionUsuario == 1:
        pass
    
    isVerdadero = False