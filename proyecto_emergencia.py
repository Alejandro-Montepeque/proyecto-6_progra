opcion=0
while opcion !=5:
    print(":::::Bienvenido al Banco del caribe::::::")
    print("\n")
    print("Seleccione Una opción a realizar:")
    print("1)Modificación de Clientes")
    print("2)Agregar Transacción")
    print("3)Lista Movimientos")
    print("4) Lista de Clientes")
    print("5) Salir")
    opcion= int(input("Opcion: "))
    if opcion == 1:
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
            print("\n")
            print("1. Agregar cliente")
            print("2. Modificar cliente")
            print("3. Eliminar cliente")
            print("4. Mostrar clientes")
            print("5. Salir")
            opcionInter = input("Ingrese el número de la opción que desea realizar: ")
            if opcionInter == "1":
                nombre = input("Ingrese el nombre del cliente: ")
                saldo = float(input("Ingrese el saldo del cliente: "))
                agregar_cliente(nombre, saldo)
            elif opcionInter == "2":
                nombre = input("Ingrese el nombre del cliente a modificar: ")
                nuevo_saldo = float(input("Ingrese el nuevo saldo: "))
                modificar_cliente(nombre, nuevo_saldo)
            elif opcionInter == "3":
                nombre = input("Ingrese el nombre del cliente a eliminar: ")
                eliminar_cliente(nombre)
            elif opcionInter == "4":
                mostrar_clientes()
            elif opcionInter == "5":
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")            
    elif opcion==2:
        total = 0.0
        opcionExt = 0
        while opcionExt != 3:
            print("¡¡Bienvenido a Banco Del Caribe!!\n")
            print("¿Qué deseas hacer?")
            print("1. Depositar dinero.")
            print("2. Retirar dinero.")
            print("3. Salir.")
            opcionExt = int(input())
            if opcionExt == 1:
                ingreso = float(input("¿Cuánto dinero deseas depositar?: "))
                if ingreso >= 0:
                    total += ingreso
                    print(f"Tu saldo total es de {total:.2f}")
                else:
                    print("La cantidad debe ser mayor a 0")
            elif opcionExt == 2:
                egreso = float(input("¿Cuánto dinero deseas retirar?: "))
                if total - egreso < 0:
                    print(f"No tienes saldo suficiente en tu cuenta. Tu saldo total es de {total:.2f}")
                else:
                    total -= egreso
                    print(f"Tu saldo total es de {total:.2f}")
            elif opcionExt == 3:
                print("Gracias por utilizar Banco Del Caribe")
                break
            else:
                print("Por favor, selecciona una opción válida.\n")
    elif opcion==3:
        print("3")
    elif opcion==4:
        print("4")
    elif opcion==5:
        print("5")
    else:
        print("Opcion no valida")
