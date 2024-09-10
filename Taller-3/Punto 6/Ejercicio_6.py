# Por Maximiliano Giraldo Ocampo
from io import *
# Creamos una clase para manejar los ejemplos de los metodos de archivos
class MetodosArchivos:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
    # Ejemplo with, para abrir un archivo
    # With es un métoddo de python que se utiliza para abrir un archivo y que posee la ventaja de que
    # cierra el archivo automáticamente una vez se termina de utilizar
    def leerArchivo(self):
        # Abrimos un archivo en modo lectura
        with open(self.nombreArchivo, 'r') as archivo:
            print(archivo.read())
        # Para el resto del punto, se utilizará el método with para abrir los archivos
    
    # Ejemplo seek, para mover el cursor del archivo
    # Seek es un método que se utiliza para mover el cursor del archivo a una posición específica
    def moverCursor(self):
        # Abrimos un archivo en modo lectura
        with open(self.nombreArchivo, 'r') as archivo:
            # Movemos el cursor a la posición 20 del archivo
            archivo.seek(20)
            print(archivo.read())
        
    # Ejemplo tell, para contar caracteres
    # Tell es un método que se utiliza para contar la cantidad de caracteres que tiene un archivo, también nos sirve para saber en que posición del archivo estamos
    def contarCaracteres(self):
        # Abrimos un archivo en modo lectura
        with open(self.nombreArchivo, 'r') as archivo:
            print(archivo.read())
            # Contamos la cantidad de caracteres que tiene el archivo
            print(archivo.tell())
            
    # Ejemplo readline, para leer una línea
    # Readline es un método que se utiliza para leer una línea de un archivo
    def leerLinea(self):
        # Abrimos un archivo en modo lectura
        with open(self.nombreArchivo, 'r') as archivo:
            print(archivo.readline())
    
    # Ejemplo readlines, para leer todas las líneas
    # Readlines es un método que se utiliza para leer todas las líneas de un archivo, y nos la almacena en una lista
    def leerLineas(self):
        # Abrimos un archivo en modo lectura
        with open(self.nombreArchivo, 'r') as archivo:
            print(archivo.readlines())
    
    # Ejemplo writelines, para escribir líneas
    # Writelines es un método que se utiliza para escribir líneas en un archivo, pero nos escribe una lista de caracteres
    def escribirLineas(self):
        # Abrimos un archivo en modo escritura
        with open(self.nombreArchivo, 'w') as archivo:
            archivo.writelines(['Hola\n', 'Mundo\n', 'Desde\n', 'Python\n'])
    
# Creamos el objeto y usaremos cada uno de los métodos creados para mostrar su funcionamiento
archivo = MetodosArchivos('archivo.txt')
archivo.leerArchivo()
archivo.moverCursor()
archivo.contarCaracteres()
archivo.leerLinea()
archivo.leerLineas()
archivo.escribirLineas()
archivo.leerArchivo()