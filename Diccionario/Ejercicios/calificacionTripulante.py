# Este programa permitirá calcular la nota definitiva de un estudiante en base a 
# otras calificaciones con un peso determinado.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
aprobar = False
count = 0
notasEstudiante = []
infoEstudianteLista = [] # Esta lista se destructurará para convertirse en un objeto. Se apoyará con el uso de otra lista.
infoEstudianteTransitoria = []
listaNotas = []
informacionEstudiante = {}


# DEFINIENDO LAS FUNCIONES
def calculoNota(nota, peso, contador):
    while True:
        try:
            calificacion = float(input(nota))
            
            if calificacion < 0.0 or calificacion > 5.0:
                print("Error: La nota ingresada es incorrecta. Asegúrese de introducir un valor entre 0.0 a 5.0.")
                continue
            
            listaNotas.append(calificacion)
            break
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la(s) nota(s). Inténtelo de nuevo.")
        
    
    while True:
        try:
            pesoPorcentaje = int(peso)
            
            if pesoPorcentaje < 0 or pesoPorcentaje > 100:
                print("Error: El peso ingresado es incorrecto. Asegúrese de introducir un valor entre 0 a 100.")
                continue
            
            listaNotas.append(pesoPorcentaje)
            break
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el peso de la nota. Inténtelo de nuevo.")

    
    if len(listaNotas) == 6:
        notaDefinitiva(listaNotas, contador)


def notaDefinitiva(notas, contador):
    notaPromedio = ((notas[0] * notas[1]) + (notas[2] * notas[3]) + (notas[4] * notas[5])) / 100
    infoEstudianteLista.append(notaPromedio)
    
    if notaPromedio >= 3.0:
        aprobar = True
    elif notaPromedio <= 2.9:
        aprobar = False
    
    infoEstudianteLista.append(aprobar)
    datosEstudiante(infoEstudianteLista, contador)


def datosEstudiante(informacion, contador):
    for i in range(1, len(informacion)):
        infoEstudianteTransitoria.append(infoEstudianteLista[i])
    
    informacionEstudiante[contador] = infoEstudianteTransitoria



# ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    # Verificación código
    while True:
        try:
            codigo = int(input("Ingrese el código: "))
            
            if codigo < 0:
                print("Error: El código no puede ser menor que 0.")
                continue
            
            infoEstudianteLista.append(codigo)
            break
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el código. Inténtelo de nuevo.")
    
    if codigo == 999:
        isVerdadero = False
    
    
    # Verificación nombre
    while isVerdadero:
        try:
            nombre = input("Ingrese el nombre: ")
            
            if len(nombre) == 0 or nombre.isalnum():
                print("Error: Introduce un nombre válido.")
                continue
            
            infoEstudianteLista.append(nombre)
            break
        
        except Exception as e:
            print(f"Ha ocurrido un problema. Error: {e}")
    
    
    # Verificación nota
    while isVerdadero:
        for i in range(3):
            if i == 0 or i == 1:
                pesoNota = 30
            elif i == 2:
                pesoNota = 40
            
            calculoNota(f"Ingrese la nota {i+1}: ", pesoNota, count)
        break
    
    count += 1
    
    break

print("")
print(infoEstudianteLista)