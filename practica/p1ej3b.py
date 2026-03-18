## Ejercicio 3
# Contar cuántas veces aparece la letra "a" en el *string ingresado por el usuario* almacenado en la variable "letras"

letraIngresadas =input("Ingrese una oracion:")
contador = 0

for letraIngresada in letraIngresadas:
    if letraIngresada == 'a' or letraIngresada  == 'A' :
        contador = contador + 1

print(f"Su oracion ingresada es:{letraIngresadas},por lo tanto tiene:{contador},a en su oracion...")         
