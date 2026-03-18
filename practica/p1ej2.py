
## Ejercicio 2
#* Preguntar fecha de nacimiento y decir en qué estación nació (primavera, verano, otoño, invierno)

dia = int(input("Ingrese su fecha dia nacimiento:"))
mes = int(input("Ingrese su mes del dia de nacimiento:"))
anio = int(input("Ingrese su anio de nacimiento:"))


if (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or dia <= 20)):
     print(f"Su mes es: {mes},Su dia es {dia}...\n Por lo tanto usted nacio en verano del {anio}")
elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes < 6 or dia <= 20)):
      print(f"Su mes es:{mes},Su dia es {dia}...\n Por lo tanto usted nacio en otoño del {anio}")
elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or dia <= 20)):
    print(f"Su mes es {mes}, su día es {dia}.\n Por lo tanto usted nació en invierno del {anio}")

else:
    print(f"Su mes es {mes}, su día es {dia}.\n Por lo tanto usted nació en primavera del {anio}")