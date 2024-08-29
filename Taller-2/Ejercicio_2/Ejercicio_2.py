# Ejericio 2 Maximiliano Giraldo Ocampo
from io import *

# Creamos una clase para usuarios
class Usuarios:
    nombre = ""
    def ingresar_profesion(self):
        self.nombre = input("Ingrese su profesion: ")
# Creamos una lista para los usuarios
usuarios = []

# Creamos una funcion para ingresar usuarios
def ingresar_usuario():
    # Creamos un estado para el ciclo
    estado = True
    while estado:
        # Creamos un objeto de la clase Usuarios
        usuario = Usuarios()
        usuario.ingresar_profesion()
        usuarios.append(usuario)
        print("Desea ingresar otro usuario? (si/no)")
        respuesta = input()
        if respuesta == "no":
            estado = False

# Creamos una funcion para buscar una cantidad de veces que se encuentra un usuario en la lista
def buscar_usuario():
    usuario_ingresado = input("Ingrese el nombre del usuario: ")
    print(f"Elemento buscado: {usuario_ingresado}")
    coincidencias = sum(1 for usuario in usuarios if usuario.nombre == usuario_ingresado)
    if coincidencias > 0:
        if coincidencias % 2 == 0:
            print(f"El usuario {usuario_ingresado} se encuentra una cantidad de {coincidencias} veces en la lista")
            print("Se encuentra un numero par de veces")
        else:
            print(f"El usuario {usuario_ingresado} se encuentra una cantidad de {coincidencias} veces en la lista")
            print("Se encuentra un numero impar de veces")
    else:
        print("El usuario no se encuentra en la lista") 

# Creamos una funcion para guardar los usuarios en un archivo
def guardar_usuarios():
    archivo = open("usuarios.txt", "a")
    for usuario in usuarios:
        archivo.write(usuario.nombre + "\n")
    archivo.close()

# Llamamos a las funciones
ingresar_usuario()
buscar_usuario()
guardar_usuarios()

