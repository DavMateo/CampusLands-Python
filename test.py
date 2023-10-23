# def ordenar_palabras(lista_palabras):
#     for i in range(0, len(lista_palabras) - 1):
#         for j in range(i+1, len(lista_palabras)):
#             if lista_palabras[i] > lista_palabras[j]:
#                 t = lista_palabras[i]
#                 lista_palabras[i] = lista_palabras[j]
#                 lista_palabras[j] = t
#     return numeros

# # Ejemplo de uso
# numeros = ["Manzana", "Limón", "Pera", "Uva", "Fresa", "Banano", "Ciruela", "Sandía"]
# numerosOrdenados = ordenar_palabras(numeros)
# print(numerosOrdenados)


dictTest = {
    "123ABC": {
        "titulo": "Un título", 
        "autor": "Un autor", 
        "precio": "Un precio"
    }, 
    "456DEF": {
        "titulo": "Otro título", 
        "autor": "Otro autor", 
        "precio": "Otro precio"
    },
    "789GHI": {
        "titulo": "Otro título más",
        "autor": "Otro nuevo autor",
        "precio": "Un precio más"
    }
}

try:
    cod = "789ghi".upper()
    keysDiccionario = list(dictTest.keys())
    # print(keysDiccionario)
    valorKey = list(dictTest[cod].values())
    # print(valorKey)

    for i in range(len(keysDiccionario)):
        if valorKey == list(dictTest[keysDiccionario[i]].values()):
            # print("¡ES VERDADERO!", i)
            valorKey.insert(0, keysDiccionario[i])
    
    # print("")
    # print(valorKey)
        
except KeyError:
    print("Error: El código no corresponde a ningún libro registrado. Inténtelo de nuevo.")
    pass