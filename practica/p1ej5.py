## Ejercicio 5
#Escribir un programa que pida al usuario dos números enteros (n y m) y muestre en pantalla:
#"La división entera entre **n** y **m** da un cociente **c** y un resto **r**"
#Donde **n** y **m** son los números introducidos por el usuario, y **c** y **r** son el cociente y el resto de la división entera respectivamente.

def division(n,m):
    if  m!= 0:
     c = n // m 
     r = n % m 
     print(f"El resultado de dividir a {n} por {m} es de:{c},y el resto es:{r}")

num1 = int(input("Ingrese el 1er N°:"))     
num2 = int(input("Ingrese el 2ndo N°:"))
division(num1,num2)

