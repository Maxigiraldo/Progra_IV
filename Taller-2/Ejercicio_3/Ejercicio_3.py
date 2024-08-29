# Ejercicio 3 Maximiliano Giraldo Ocampo
# Importamos la libreria io
from io import *
# Creamos una clase Cadenas
class Cadenas:
    # Creamos una lista vacia para almacenar las cadenas de texto ingresadas
    lista = []
    
    # Creamos un metodo para ingresar las cadenas de texto
    def ingreso(self):
        print("Ingrese una cadena de texto, para finalizar ingrese SALIR")
        estado = True
        while estado:
            cadena = input("Ingrese una cadena de texto: ")
            # Verificamos que la cadena de texto ingresada no sea SALIR
            if cadena.upper() == "SALIR" and len(self.lista) >= 15:
                estado = False
            # Verificamos que la cadena de texto ingresada no sea SALIR y que la lista tenga al menos 15 elementos
            elif cadena.upper() == "SALIR" and len(self.lista) < 15:
                print("Debe ingresar al menos 15 cadenas de caracteres")
            else:
                self.lista.append(cadena)

    # Creamos un metodo para ordenar las cadenas de texto por longitud
    def ordenar_por_longitud(self):
        for i in range(len(self.lista)):
            # Recorremos la lista
            for j in range(i + 1, len(self.lista)):
                # Verificamos si la longitud del elemento actual es mayor a la longitud del siguiente
                if len(self.lista[i]) > len(self.lista[j]):
                    # Intercambiamos las posiciones si el elemento actual es más largo que el siguiente
                    self.lista[i], self.lista[j] = self.lista[j], self.lista[i]
        print("Lista ordenada por longitud de cadenas")
        for i in self.lista:
            print(i)
            
# Creamos una instancia de la clase Cadenas
cadena = Cadenas()
cadena.ingreso()
cadena.ordenar_por_longitud()

# Creamos un archivo para almacenar las cadenas de texto
archivo = open("cadenas.txt", "a")
for i in cadena.lista:
    archivo.write(i + "\n")
    
archivo.close()

