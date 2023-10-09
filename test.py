miLista = [["Hola", "Mundo", 1, 2, 3, 4], ["XD", 454, "greg", "Jelou", 54.3]]
buscar = "Hola"
checked = False


for i in range(len(miLista)):
    for j in range(len(miLista[i])):
        if miLista[i][j] == buscar:
            test1 = i
            test2 = j
            checked = True

if not checked:
    print("No se encontró el elemento")

else:
    print(miLista[test1][test2])


if checked:
    elementoBorrado = miLista.pop(test1)
    print(f"El elemento borrado es: {elementoBorrado}")