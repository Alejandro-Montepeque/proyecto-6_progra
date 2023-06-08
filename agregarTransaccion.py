total = 0.0
opcion = 0

while opcion != 3:
    print("¡¡Bienvenido a Banco Del Caribe!!\n"
        "¿Qué deseas hacer?\n"
        "1. Depositar dinero.\n"
        "2. Retirar dinero.\n"
        "3. Salir.\n")
    opcion = int(input())

    if opcion == 1:
        ingreso = float(input("¿Cuánto dinero deseas depositar?: "))
        if ingreso >= 0:
            total += ingreso
            print(f"Tu saldo total es de {total:.2f}")
        else:
            print("La cantidad debe ser mayor a 0")
    elif opcion == 2:
        egreso = float(input("¿Cuánto dinero deseas retirar?: "))
        if total - egreso < 0:
            print(f"No tienes saldo suficiente en tu cuenta. Tu saldo total es de {total:.2f}")
        else:
            total -= egreso
            print(f"Tu saldo total es de {total:.2f}")
    elif opcion == 3:
        print("Gracias por utilizar Banco Del Caribe")
        break
    else:
        print("Por favor, selecciona una opción válida.\n")

