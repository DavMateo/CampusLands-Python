miLista = [["Hola", "Mundo", 1, 2, 3, 4], ["XD", 454, "greg", "Jelou", 54.3]]
buscar = "Hola"
checked = False


for i in range(len(miLista)):
    *a, = miLista[i]
    checked = True

if not checked:
    print("No se encontró el elemento")

else:
    print(a)
    # print(b)
    # print(c)
    # print(d)
    # print(e)
    # print(f)