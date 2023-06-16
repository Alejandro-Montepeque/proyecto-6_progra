opcion=0
import random
listaGlobal={}
while opcion !=5:
    print(":::::Bienvenido al Banco del caribe::::::")
    print("\n")
    print("Seleccione Una opción a realizar:")
    print("1) Modificación de Clientes")
    print("2) Agregar Transacción")
    print("3) Lista Movimientos")
    print("4) Lista de Clientes")
    print("5) Salir")
    opcion= int(input("Opcion: "))
    if opcion == 1:
        class Cliente:
            def __init__(self, codigo, nombre, saldo, cuenta):
                self.codigo = codigo
                self.nombre = nombre
                self.saldo = saldo
                self.cuenta = cuenta
                self.retiro_count = 0
                self.deposito_count = 0

            def __str__(self):
                return f"Código: {self.codigo}\nNombre: {self.nombre}\nSaldo: {self.saldo}\nNumero de Cuenta: {self.cuenta}\n-------------------"

        def agregar_cliente():
            codigo = str(random.randint(1000, 9999))
            nombre = input("Ingrese el nombre del cliente: ")
            saldo = float(input("Ingrese el saldo del cliente: "))
            cuenta = int(input("Ingrese su número de cuenta: "))
            cliente = Cliente(codigo, nombre, saldo, cuenta)
            listaGlobal[cuenta] = cliente
            print("Cliente agregado exitosamente.")
        def modificar_cliente():
            num_cuenta = int(input("Ingrese el número de cuenta del cliente a modificar: "))
            if num_cuenta in listaGlobal:
                cliente = listaGlobal[num_cuenta]
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nuevo_cuenta = int(input("Ingrese el nuevo número de cuenta: "))
                cliente.nombre = nuevo_nombre
                cliente.cuenta = nuevo_cuenta
                print("Cliente modificado exitosamente.")
            else:
                print("Cliente no encontrado.")

        def eliminar_cliente():
            num_cuenta = int(input("Ingrese el número de cuenta del cliente a eliminar: "))
            if num_cuenta in listaGlobal:
                del listaGlobal[num_cuenta]
                print("Cliente eliminado exitosamente.")
            else:
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
            print("¿Qué tipo de transacción desea hacer?")
            print("1. Depositar dinero.")
            print("2. Retirar dinero.")
            print("3. Salir.")
            opcionExt = int(input("Ingrese la acción que desea tomar: "))
            if opcionExt == 1:
                num_cuenta = input("Ingrese su número de cuenta: ")
                if int(num_cuenta) in listaGlobal:
                    cliente = listaGlobal[int(num_cuenta)]
                    ingreso = float(input("¿Cuánto dinero deseas depositar?: "))
                    if ingreso >= 0:
                        cliente.saldo += ingreso
                        cliente.deposito_count += 1
                        print(f"Tu saldo total es de {cliente.saldo:.2f}")
                    else:
                        print("La cantidad debe ser mayor a 0")
                else:
                    print("Cliente no encontrado.")
            elif opcionExt == 2:
                num_cuenta = input("Ingrese el número de cuenta para retirar dinero: ")
                if int(num_cuenta) in listaGlobal:
                    cliente = listaGlobal[int(num_cuenta)]
                    egreso = float(input("¿Cuánto dinero deseas retirar?: "))
                    if cliente.saldo - egreso < 0:
                        cliente.retiro_count += 1
                        print(f"No tienes saldo suficiente en tu cuenta. Tu saldo total es de {cliente.saldo:.2f}")
                    else:
                        cliente.saldo -= egreso
                        cliente.saldo -= egreso
                        print(f"Tu saldo total es de {cliente.saldo:.2f}")
                else:
                    print("Cliente no encontrado.")
    elif opcion==3:
        print("Contadores de retiros y depósitos:")
        for cliente in listaGlobal.values():
            print(f"Número de cuenta: {cliente.cuenta}")
            print(f"Contador de retiros: {cliente.retiro_count}")
            print(f"Contador de depósitos: {cliente.deposito_count}")
            print("-------------------")
    elif opcion==4:
        print("Clientes registrados:")
        for cliente in listaGlobal.values():
            print(cliente)
    elif opcion==5:
        print("Gracias por utilizar EL BANCO DEL CARIBE")
        break
    else:
        print("Opcion no valida")