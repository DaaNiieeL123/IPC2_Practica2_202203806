class Cliente:
    def __init__(self, nombre, apellido, correo, nit):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.nit = nit

class GestorClientes:
    def __init__(self):
        self.clientes = []

    def registrar_cliente(self, nombre, apellido, correo, nit):
        for cliente in self.clientes:
            if cliente.nit == nit:
                print("El cliente con este NIT ya está registrado.")
                return 'existente'

        # Si el NIT no existe en la lista, agrega el cliente
        nuevo_cliente = Cliente(nombre, apellido, correo, nit)
        self.clientes.append(nuevo_cliente)
        print("Cliente registrado correctamente.")
        return 'registrado'

    def obtener_clientes(self):
        return self.clientes

    def eliminar_cliente(self, nit):
        for cliente in self.clientes:
            if cliente.nit == nit:
                self.clientes.remove(cliente)
                print(f"Cliente {cliente.nombre} eliminado correctamente.")
                return cliente
        print("Error: El cliente con este NIT no está registrado.")
        return None
    

