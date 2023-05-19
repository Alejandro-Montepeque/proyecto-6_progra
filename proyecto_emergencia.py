opcion=0
opcion2=0
while opcion !=6:
    print(":::::Bienvenido al Banco del caribe::::::")
    print("\n")
    print("Seleccione Una opción:")
    print("1)Modificacion de Clientes")
    print("2)Agregar Transacción")
    print("3)Lista de Depositos")
    print("4) Lista de Retiros")
    print("5) Lista de Clientes")
    print("6) Salir")
    opcion= int(input("Opcion: "))
    if opcion ==1:
        while opcion2 !=4:
            print("Que desea hacer:\n")
            print("1)Agregar un Cliente")
            print("2)Eliminar un Cliente")
            print("3)Modificacion de Clientes")
            print("4)Atras")
            opcion2=int(input("Opcion: "))
            if opcion2==1:
                print("1)Agregar Cliente")
            elif opcion2==2:
                print("2)Eliminar un Cliente")
            elif opcion2==3:
                print("3)Modificacion de Clientes")
            elif opcion2==4:
                print("4)Atras")
            else:
                print("Opcion No valida")
    elif opcion==2:
        print("2")
    elif opcion==3:
        print("3")
    elif opcion==4:
        print("4")
    elif opcion==5:
        print("5")
    elif opcion==6:
        print("6")
    else:
        print("Opcion no valida")
