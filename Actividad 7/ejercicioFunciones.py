# Este programa almacenará la solución de tres ejercicios distintos
# donde el usuario es quien decida elegir cuál solución probar.


# DEFINIENDO LAS FUNCIONES
def menu():
    while True:
        try:
            print("\n=== MENÚ PROGRAMA ===")
            print("1. Factorial de un número.")
            print("2. Calculadora salario de un empleado.")
            print("3. Calculadora de palabras en un párrafo.")
            print("4. Salir.")
            opcionUsuario = int(input("Escoja una opción (1-4): "))
            
            if opcionUsuario < 1 or opcionUsuario > 4:
                print("\nError: Elije una opción válida")
                continue
            return opcionUsuario
            
        except ValueError:
            print("Has elegido una opción errónea. Ingresa un número entero dentro del rango 1-4.")


# Ejercicio n°1: Factorial de un número.
def factorialNumero(num):    
    while True:        
        try:
            # DEFINICIÓN DE LAS VARIABLES NECESARIAS
            resultadoFactorial = 1
            numero = int(input(num))
            
            if num < 0:
                print("Error: Debes ingresar un número entero positivo.")
                continue
            
            for i in range(1, num + 1):
                resultadoFactorial *= i
            return resultadoFactorial
            
        except ValueError:
            print("Error al momento de digital el número. Inténtelo de nuevo.")
            

test = int(input("Número factorial: "))
msj = factorialNumero(test)
print(f"El resultado del factorial del número {test:,.0f} es: {msj:,.0f}")