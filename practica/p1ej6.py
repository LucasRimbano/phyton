## Ejercicio 6
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
def saludar(mensaje):
    print(mensaje)

bienvenida = "Bienvenido al sistema..."
saludar(f"****{bienvenida}**** , acceso concedido")


nombre = input("Ingrese su nombre: ")

constraseniaValida = "asd1"
constraseniaEncontrada = "Contraseña valida, pudo entrar a su perfil..."
constraseniaNoEncontrada = "Su contraseña no es esta, siga intentando..."

constrasenia = input("Ingrese su contraseña: ").strip()

while constrasenia != constraseniaValida:
    saludar(constraseniaNoEncontrada)
    constrasenia = input("Ingrese su contraseña: ").strip()


saludar(f"Felicidades {nombre}, acceso encontro su constraseña")
saludar(constraseniaEncontrada)