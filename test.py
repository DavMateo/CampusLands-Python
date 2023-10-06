nombre = "      DavID                     maTeo            ".strip()
nombreArray = nombre.split(" ")
listaNombreFiltrado = []

for i in range(len(nombreArray)):
    if nombreArray[i] != "":
        listaNombreFiltrado.append(nombreArray[i])

nombreValidarFiltrado = "".join(listaNombreFiltrado).lower()
nombreFinal = " ".join(listaNombreFiltrado).title()

print(nombreArray)
print(listaNombreFiltrado)
print(nombreValidarFiltrado)
print(nombreFinal)