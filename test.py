nombre = input("Ingrese el nombre: ").strip()
nombreArray = nombre.split(" ")
    
for i in range(len(nombreArray)):
    print(i)
    if i == " ":
        nombreArray.pop(i, "")

print(nombreArray)