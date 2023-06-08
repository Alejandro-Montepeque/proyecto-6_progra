class Transaccion:
    def __init__(self, tipo, monto):
        self.tipo = tipo
        self.monto = monto


class Cuenta:
    def __init__(self):
        self.movimientos = []

    def agregar_transaccion(self, tipo, monto):
        transaccion = Transaccion(tipo, monto)
        self.movimientos.append(transaccion)

    def obtener_lista_retiro(self):
        lista_retiro = [transaccion for transaccion in self.movimientos if transaccion.tipo == 'retiro']
        return lista_retiro

    def obtener_lista_deposito(self):
        lista_deposito = [transaccion for transaccion in self.movimientos if transaccion.tipo == 'deposito']
        return lista_deposito


# Ejemplo de uso
cuenta = Cuenta()

# Agregar transacciones
cuenta.agregar_transaccion('retiro', 100)
cuenta.agregar_transaccion('deposito', 200)
cuenta.agregar_transaccion('retiro', 50)
cuenta.agregar_transaccion('deposito', 150)

# Obtener listas de retiros y depósitos
lista_retiro = cuenta.obtener_lista_retiro()
lista_deposito = cuenta.obtener_lista_deposito()

# Imprimir listas
print("Lista de retiros:")
for transaccion in lista_retiro:
    print(f"Tipo: {transaccion.tipo}, Monto: {transaccion.monto}")

print("\nLista de depósitos:")
for transaccion in lista_deposito:
    print(f"Tipo: {transaccion.tipo}, Monto: {transaccion.monto}")
