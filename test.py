import json

testFile = open("archivo.json", "w")
json.dump({"25": "Hola", "34D": ["Mundo"]}, testFile, indent=4, sort_keys=True)
testFile.close()


abrirArchivo = open("archivo.json", "r")
recibiendoInformacion = json.load(abrirArchivo)
abrirArchivo.close()

print(recibiendoInformacion)


recibiendoInformacion["nuevaLlave"] = ["Titulo", "Autor", "Precio"]
print(recibiendoInformacion)

escribirArchivo = open("archivo.json", "w")
json.dump(recibiendoInformacion, escribirArchivo, indent=4)
escribirArchivo.close()

del recibiendoInformacion["25"]
print(recibiendoInformacion)

escribirArchivo = open("archivo.json", "w")
json.dump(recibiendoInformacion, escribirArchivo)
escribirArchivo.close()