clientes = {}

def añadir_cliente():
    cuit = input("Ingrese el CUIT del cliente: ")

    if cuit in clientes:
        print("Ese cliente ya existe en la base de datos.")
    else:
        nombre = input("Ingrese el nombre: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")
        correo = input("Ingrese el correo: ")
        preferente = input("¿Es cliente preferente? (si/no): ").lower() == "si"

        clientes[cuit] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": preferente
        }

        print("Cliente agregado correctamente.")


def eliminar_cliente():
    cuit = input("Ingrese el CUIT del cliente a eliminar: ")

    if cuit in clientes:
        del clientes[cuit]
        print("Cliente eliminado correctamente.")
    else:
        print("No existe un cliente con ese CUIT.")


def mostrar_cliente():
    cuit = input("Ingrese el CUIT del cliente a consultar: ")

    if cuit in clientes:
        print("Datos del cliente:")
        print(f"CUIT: {cuit}")
        print(f"Nombre: {clientes[cuit]['nombre']}")
        print(f"Dirección: {clientes[cuit]['direccion']}")
        print(f"Teléfono: {clientes[cuit]['telefono']}")
        print(f"Correo: {clientes[cuit]['correo']}")
        print(f"Preferente: {clientes[cuit]['preferente']}")
    else:
        print("No existe un cliente con ese CUIT.")


def listar_clientes():
    if len(clientes) == 0:
        print("No hay clientes cargados.")
    else:
        print("Lista de clientes:")
        for cuit, datos in clientes.items():
            print(f"{cuit} - {datos['nombre']}")


def listar_clientes_preferentes():
    hay_preferentes = False

    for cuit, datos in clientes.items():
        if datos["preferente"]:
            print(f"{cuit} - {datos['nombre']}")
            hay_preferentes = True

    if not hay_preferentes:
        print("No hay clientes preferentes.")


while True:
    print("\n--- MENÚ DE CLIENTES ---")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        añadir_cliente()
    elif opcion == "2":
        eliminar_cliente()
    elif opcion == "3":
        mostrar_cliente()
    elif opcion == "4":
        listar_clientes()
    elif opcion == "5":
        listar_clientes_preferentes()
    elif opcion == "6":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")