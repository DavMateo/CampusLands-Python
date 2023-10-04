nombre = "     David      mateo    carreño     ".strip()
nombreArray = nombre.split(" ")
nombreArrayFiltrado = []
    
for i in range(len(nombreArray)):
    if nombreArray[i] != "":
        nombreArrayFiltrado.append(nombreArray[i])

nombreFinal = " ".join(nombreArrayFiltrado).title()
test = "".join(nombreArrayFiltrado)
print(nombreFinal, len(nombreFinal))
print(test.isalnum())