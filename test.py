empleados = [["David Mateo", 51155, 43, 100000], ["Juan Gabriel", 5285024, 85, 135500]]
otrosEmpleados = [["David Mateo", 5525259, 59, 100000], ["Ian Alejandro", 482526515, 78, 89511]]


def test():
    for i in range(len(empleados)):
        for j in range(0, len(empleados[i])):
            empleados[i][j] = otrosEmpleados[i][j]
    return empleados
            
print(empleados)
print(test())