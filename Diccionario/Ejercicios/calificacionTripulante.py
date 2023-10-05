# Este programa permitirá calcular la nota definitiva de un estudiante en base a 
# otras calificaciones con un peso determinado.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True



# DEFINIENDO LAS FUNCIONES
def calculoNota(nota, peso):
    pass


def notaDefinitiva(notas):
    pass


def datosEstudiante(informacion):
    pass



# ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    if codigo == 999:
        isVerdadero = False
        
    else:
        # Verificación código
        while True:
            try:
                codigo = int(input("Ingrese el código: "))
                
                if codigo < 0:
                    print("Error: El código no puede ser menor que 0.")
                break
            
            except ValueError:
                print("Ha ocurrido un error al ingresar el código. Inténtelo de nuevo.")
        
        
        # Verificación nombre
        while True:
            try:
                nombre = input("Ingrese el nombre: ")
                
                if len(nombre) == 0 or nombre.isalnum():
                    print("Error: Introduce un nombre válido.")
                    continue
                break
            
            except Exception as e:
                print(f"Ha ocurrido un problema. Error: {e}")
        
        
        # Verificación nota
        while True:
            try:
                nota1 = float(input("Ingrese la nota 1: "))
                nota2 = float(input("Ingrese la nota 2: "))
                nota3 = float(input("Ingrese la nota 3: "))
                
                if nota1 < 0.0 or nota1 > 5.0:
                    print("Error: La nota 1 es incorrecta. Asegúrese de introducir un valor entre 0.0 a 5.0.")
                    continue
                
                elif nota2 < 0.0 or nota2 > 5.0:
                    print("Error: La nota 2 es incorrecta. Asegúrese de introducir un valor entre 0.0 a 5.0.")
                    continue
                
                elif nota3 < 0.0 or nota3 > 5.0:
                    print("Error: La nota 3 es incorrecta. Asegúrese de introducir un valor entre 0.0 a 5.0.")
                    continue
                break
            
            except ValueError:
                print("Ha ocurrido un error al ingresar la(s) nota(s). Inténtelo de nuevo.")