# Por Maximiliano Giraldo Ocampo
from io import *
# Creacin de la lista inicial
lista = [1, 1991, "taller", 200, 3, "programación", 700, "utp", "POO"]

# Creación de la clase AdministradorArchivos
class AdministradorArchivos:
    # Constructor de la clase
    def __init__(self, lista):
        self.lista = lista
    
    # Método para guardar la lista inicial
    def guardar_lista_inicial(self):
        archivo = open("lista_inicial.txt", "a")
        for elemento in self.lista:
            archivo.write(str(elemento) + "\n")
        archivo.close()
    
    # Método para guardar los números de la lista
    def guardar_numeros(self):
        archivo = open("numeros.txt", "a")
        for elemento in self.lista:
            if type(elemento) == int:
                archivo.write(str(elemento) + "\n")
        archivo.close()
    
    # Método para guardar la lista pero cuando encuentre un número lo reemplaza por la palabra "remplazo"
    def remplazo(self):
        archivo = open("remplazo.txt", "a")
        for elemento in self.lista:
            if type(elemento) == int:
                archivo.write("remplazo" + "\n")
            else:
                archivo.write(elemento + "\n")
        archivo.close()
    
    # Método para imprimir la mitad de la lista
    def imprimir(self):
        mitad_lista = len(self.lista) // 2
        for i in range(mitad_lista):
            print(self.lista[i])
            
# Creación del objeto de la clase AdministradorArchivos
admin = AdministradorArchivos(lista)
# Llamado de los métodos de la clase
admin.guardar_lista_inicial()
admin.guardar_numeros()
admin.remplazo()
admin.imprimir()
