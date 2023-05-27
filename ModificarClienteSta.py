clientes = []

def agregar_cliente(nombre, saldo):
    cliente = {"nombre": nombre, "saldo": saldo}
    clientes.append(cliente)
    print("Cliente agregado exitosamente.")

def modificar_cliente(nombre, nuevo_saldo):
    for cliente in clientes:
        if cliente["nombre"] == nombre:
            cliente["saldo"] = nuevo_saldo
            print("Cliente modificado exitosamente.")
            return
    print("Cliente no encontrado.")

def eliminar_cliente(nombre):
    for cliente in clientes:
        if cliente["nombre"] == nombre:
            clientes.remove(cliente)
            print("Cliente eliminado exitosamente.")
            return
    print("Cliente no encontrado.")

def mostrar_clientes():
    if clientes:
        print("Lista de clientes:")
        for cliente in clientes:
            print("Nombre:", cliente["nombre"])
            print("Saldo:", cliente["saldo"])
            print("-------------------")
    else:
        print("No hay clientes registrados.")

# Ejemplo de uso
agregar_cliente("Juan Perez", 1000)
agregar_cliente("Maria Lopez", 500)
modificar_cliente("Juan Perez", 1500)
eliminar_cliente("Maria Lopez")
mostrar_clientes()

