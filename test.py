dictTest = {
    "123ABC": {
        "title": "Lo Que Nunca Te Dije",
        "autor": "Antonio Ortiz", 
        "precio": 30500
        },
    
    "456DEF": {
        "titulo": "Don Quijote De La Mancha", 
        "autor": "Miguel De Cervantes Saavedra", 
        "precio": 78500
    }
}
cod = "123ABC"

print(dictTest)
del dictTest[cod]
print(dictTest)