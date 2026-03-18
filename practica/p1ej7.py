## Ejercicio 7
"""
Gestor de Base de Datos de Clientes de Empresa
Este módulo implementa un sistema de gestión de clientes que almacena
información en una estructura de diccionarios.
Estructura de Datos:
    - Diccionario principal: {CUIT: {datos_cliente}}
    - Datos del cliente: {
        'nombre': str,
        'direccion': str,
        'telefono': str,
        'correo': str,
        'preferente': bool
      }
Funcionalidades:
    1. Añadir cliente: Solicita datos del cliente y lo agrega a la BD
    2. Eliminar cliente: Elimina un cliente por su CUIT
    3. Mostrar cliente: Muestra los datos completos de un cliente específico
    4. Listar todos: Muestra CUIT y nombre de todos los clientes
    5. Listar preferentes: Muestra solo clientes con preferente=True
    6. Terminar: Finaliza la ejecución del programa
Flujo Principal:
    - Menú interactivo que solicita opción al usuario (1-6)
    - Validación de entrada y manejo de errores
    - Iteración continua hasta seleccionar opción 6 (Terminar)
Autor: 
Descripción: Práctica 1, Ejercicio 7
"""

clientes =  {}

def anadirCliente ():
        cuit =  input("Ingrese el numero de cuit del cliente: ")
        nombre = input("Ingrese su nombre: ")
        direccion = input("Ingrese su direccion: ")
        telefono = input("Ingrese su telefono: ")
        correo  = input("Ingrese su correo electronico: ")
        preferencia = input("Es cliente preferente ? (si/no)...").lower()
  
        if preferencia == 'si':
                preferencia = True
        elif preferencia == 'no':
                preferencia= False        
        else: 
                print("lo siento ingreso algo invalido ingrese si/no no otra cosa...")
                preferencia = False


        clientes[cuit] = {
                "nombre" : nombre, 
                "direccion" : direccion ,
                "telefono" : telefono ,
                "correo" : correo, 
                "preferente": preferencia
        }
       


def eliminarCliente():
    cuit_Buscar = input("Ingrese el cuit del cliente que quiera eliminar: ")

    for cuit in clientes:
        if cuit == cuit_Buscar:
            clientes.pop(cuit)
            print(f"El cliente {cuit} fue eliminado correctamente")
            break
    else:
        print(f"No se encontró ningún cliente con ese id: {cuit_Buscar}")

               
def mostrarDatos():
      
    cuit_Buscar = input("Ingrese el cuit del cliente que quiera mostrar sus datos: ")

    for cuit in clientes:
          if cuit == cuit_Buscar:
                cliente = clientes[cuit_Buscar]
                print(f"Su N° de cuit es: {cuit}")
                print(f"Nombre: {cliente['nombre']}")
                print(f"Direccion:{clientes[cuit]['direccion']}")
                print(f"Teléfono: {clientes[cuit]['telefono']}")
                print(f"Correo: {clientes[cuit]['correo']}")
                print(f"Preferente: {cliente['preferente']}")
          else:
                print("No existe ningun cliente con ese cuit....")      


def mostrarTodosclientes():
      if len(clientes) == 0:
            print("lo siento no hay clientes todavia registrados... ");         
      else:
            for cuit,cliente in clientes.items():
                  print(f"Cuit n°:{cuit}")
                  print(f"Nombre: {cliente['nombre']}")
                  print(f"Direccion: {cliente['direccion']}")
                  print(f"Teléfono: {cliente['telefono']}")
                  print(f"Correo: {cliente['correo']}")
                  print(f"Preferente: {cliente['preferente']}")

def mostrar_Nombre_Prefente():
             
    cuit_Buscar = input("Ingrese el cuit del cliente que quiera mostrar sus datos: ")
    for cuit,cliente in clientes.items():
          if cliente ["preferencia"]:
                print(f"Su N° es: {cuit} y su nombre es: {cliente['nombre']}")

                
while True:
    print("\n--- MENU DE CLIENTES ---")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

    opcion = input("Ingrese una opción (1-6): ")

    if opcion == "1":
        anadirCliente()
    elif opcion == "2":
        eliminarCliente()
    elif opcion == "3":
        mostrarDatos()
    elif opcion == "4":
        mostrarTodosclientes()
    elif opcion == "5":
        mostrar_Nombre_Preferente()
    elif opcion == "6":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida. Intente de nuevo.")