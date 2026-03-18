frase = "python es divertido y python es poderoso"
palabras = frase.split()
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)
