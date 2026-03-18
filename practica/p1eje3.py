## Ejercicio 3
#* Contar cuántas veces aparece la letra "a" en el *string* almacenado en la variable "letras"


letras = "letras"
contador = 0 

for letra in letras:
    if letra == 'a':
        contador = contador +1 

print("La letras A: aparece", contador,"veces")   

