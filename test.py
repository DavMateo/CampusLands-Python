stringUsuario = "  re324d @gsd3  434  234a sfsdf3   ".strip()
filtrarString = []
count = 0
stringFiltrada = ""

for i in range(len(stringUsuario)):
    if stringUsuario[i].isdigit():
        # filtrarString.append(stringUsuario[i])
        stringFiltrada += stringUsuario[i]

# stringFiltrada += "".join(filtrarString)        
print(stringFiltrada)