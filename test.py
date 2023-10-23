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


dictTest = {"123ABC": {"Titulo", "Autor", "Precio"}}
print(list(dictTest.keys()), list(dictTest.values()))