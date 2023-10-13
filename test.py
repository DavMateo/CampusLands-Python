# diccionario = {
#     1099737474: {'nombre': 'David Mateo', 'edad': 17, 'sexo': 'M', 'telefono': '+57 3142170246'},
#     354545: {'nombre': 'Hbkerg Ergonerg', 'edad': 17, 'sexo': 'M', 'telefono': '+57 3155425415'}
# }

# print("\n")
# for i in range(len(diccionario)):
#     print(list(diccionario.items())[i])



test = [
    {1099737474: {'nombre': 'David Mateo', 'edad': 17, 'sexo': 'M', 'telefono': '+57 3142170246'}}, 
    {354545: {'nombre': 'Hbkerg Ergonerg', 'edad': 17, 'sexo': 'M', 'telefono': '+57 3155425415'}}
]


for i in range(len(test)):
    if test[i].get(1099737474):
        texto = test[i].get(1099737474)
    
    print("")