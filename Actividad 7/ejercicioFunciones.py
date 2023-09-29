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
                print("Error: Elije una opción válida")
                continue
            return opcionUsuario
            
        except ValueError:
            print("Has elegido una opción errónea. Ingresa un número entero dentro del rango 1-4.")
            
menu()