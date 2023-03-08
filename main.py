import os

class Cliente:
    def __init__(self, correo_electronico, contrasena, nombre, direccion, telefono):
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def __str__(self):
        return self.nombre
      
class PaginaCompras:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_cliente(self, correo_electronico):
        for cliente in self.clientes:
            if cliente.correo_electronico == correo_electronico:
                return cliente
        return None

    def __str__(self):
        return "Página de Compras"
  
def registro(pagina_compras):
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    correo_electronico = input("Ingrese el correo electrónico del cliente: ")
    contrasena = input("Ingrese una contraseña para el cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    
    cliente = Cliente(correo_electronico, contrasena, nombre, direccion, telefono)
    pagina_compras.agregar_cliente(cliente)
    
    print("Cliente registrado exitosamente!")

def inicio_sesion(pagina_compras):
    correo_electronico = input("Ingrese el correo electrónico del cliente: ")
    contrasena = input("Ingrese la contraseña del cliente: ")
    
    cliente = pagina_compras.buscar_cliente(correo_electronico)

    if cliente is not None and cliente.contrasena == contrasena:
        print("Inicio de sesión exitoso!")
        print("Nombre:", cliente.nombre)
        print("Dirección:", cliente.direccion)
        print("Correo electrónico:", cliente.correo_electronico)
        print("Telefono:", cliente.telefono)
    else:
        print("Correo electrónico o contraseña incorrectos.")

pagina_compras = PaginaCompras()

opcion = "1"
while opcion != "3":
    opcion = input("1. Registrar\n2. Iniciar sesión\n3. Salir\nElige una opción: ")
    if opcion == "1": registro(pagina_compras)
    elif opcion == "2": inicio_sesion(pagina_compras)
    elif opcion == "3": 
        print("Adiós!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

print(pagina_compras)