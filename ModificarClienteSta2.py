class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def __str__(self):
        return f"Nombre: {self.nombre}\nSaldo: {self.saldo}\n-------------------"

clientes = []

def agregar_cliente(nombre, saldo):
    cliente = Cliente(nombre, saldo)
    clientes.append(cliente)
    print("Cliente agregado exitosamente.")

def modificar_cliente(nombre, nuevo_saldo):
    cliente_encontrado = False
    for cliente in clientes:
        if cliente.nombre == nombre:
            cliente.saldo = nuevo_saldo
            cliente_encontrado = True
            print("Cliente modificado exitosamente.")
    if not cliente_encontrado:
        print("Cliente no encontrado.")

def eliminar_cliente(nombre):
    clientes_aux = []
    cliente_encontrado = False
    for cliente in clientes:
        if cliente.nombre == nombre:
            cliente_encontrado = True
            print("Cliente eliminado exitosamente.")
        else:
            clientes_aux.append(cliente)
    if not cliente_encontrado:
        print("Cliente no encontrado.")
    clientes.clear()
    clientes.extend(clientes_aux)

def mostrar_clientes():
    if clientes:
        print("Lista de clientes:")
        for cliente in clientes:
            print(cliente)
    else:
        print("No hay clientes registrados.")

# Ejecución del programa
while True:
    print("1. Agregar cliente")
    print("2. Modificar cliente")
    print("3. Eliminar cliente")
    print("4. Mostrar clientes")
    print("5. Salir")
    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        saldo = float(input("Ingrese el saldo del cliente: "))
        agregar_cliente(nombre, saldo)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del cliente a modificar: ")
        nuevo_saldo = float(input("Ingrese el nuevo saldo: "))
        modificar_cliente(nombre, nuevo_saldo)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del cliente a eliminar: ")
        eliminar_cliente(nombre)
    elif opcion == "4":
        mostrar_clientes()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

