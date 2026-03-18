def crear_diccionario(claves, valores):
    pares = []

    for i in range(len(claves)):
        tupla = (claves[i], valores[i])   # creamos la tupla (clave, valor)
        pares.append(tupla)

    diccionario = dict(pares)
    return diccionario


claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 20, "Buenos Aires"]

resultado = crear_diccionario(claves, valores)

print(resultado)