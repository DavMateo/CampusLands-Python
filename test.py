matriz = []

for i in range(3):
    fila = [0] * 3
    matriz.append(fila)

print(matriz)


for row in matriz:
    print(" | ".join(row))
    print("---" * len(row))