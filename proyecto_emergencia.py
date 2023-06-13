opcion=0
import random
listaGlobal={
        "CodigoCliente": '',
        "NombreCliente": '',
        "saldoCliente": '',
        "numCuenta":'',
    }

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
            def __init__(self, codigo, nombre, saldo, cuenta):
                self.codigo = codigo
                self.nombre = nombre
                self.saldo = saldo
                self.cuenta= cuenta

            def __str__(self):
                return f"Código: {self.codigo}\nNombre: {self.nombre}\nSaldo: {self.saldo}\nNumero de Cuenta:{self.cuenta}\n-------------------"

        clientes = []

        def agregar_cliente():
            codigo = str(random.randint(1000, 9999))
            nombre = input("Ingrese el nombre del cliente: ")
            saldo = float(input("Ingrese el saldo del cliente: "))
            cuenta = int(input("Ingrese su número de cuenta: "))
            cliente = Cliente(codigo, nombre, saldo, cuenta)
            clientes.append(cliente)
            print("Cliente agregado exitosamente.")
        def modificar_cliente():
            num_cuenta = input("Ingrese el número de cuenta del cliente a modificar: ")
            encontrado = False
            for cliente in clientes:
                if cliente.cuenta == int(num_cuenta):
                    nuevo_name= input("Ingrese el nuevo nombre: ")
                    nuevo_cuenta=int(input("Ingrese el nuevo numero de cuenta: "))
                    cliente.nombre=nuevo_name
                    cliente.cuenta=nuevo_cuenta
                    encontrado = True
                    print("Cliente modificado exitosamente.")
                    break
            if not encontrado:
                print("Cliente no encontrado.")
        def eliminar_cliente():
            num_cuenta = input("Ingrese el código del cliente a eliminar: ")
            encontrado = False
            for cliente in clientes:
                if cliente.cuenta == int(num_cuenta):
                    clientes.remove(cliente)
                    encontrado = True
                    print("Cliente eliminado exitosamente.")
                    break
            if not encontrado:
                print("Cliente no encontrado.")

        while True:
            print("\n")
            print("1. Agregar cliente")
            print("2. Modificar cliente")
            print("3. Eliminar cliente")
            print("4. Salir")
            opcionInter = input("Ingrese el número de la opción que desea realizar: ")
            if opcionInter == "1":
                agregar_cliente()
            elif opcionInter == "2":
                modificar_cliente()
            elif opcionInter == "3":
                eliminar_cliente()
            elif opcionInter == "4":
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
        def mostrar_clientes():
            if clientes:
                print("Lista de clientes:")
                for cliente in clientes:
                    print(cliente)
            else:
                print("No hay clientes registrados.")
        mostrar_clientes()
    elif opcion==5:
        print("5")
    else:
        print("Opcion no valida")
