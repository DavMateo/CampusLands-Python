test = open("Persistencia de Datos\Ejercicios\datos-de-empleados-programa\datos-empleados.dat", "r")

datos = test.read()
print("\n", datos)

test.close()