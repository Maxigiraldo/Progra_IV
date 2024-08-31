# Ejercicio 4 Maximiliano Giraldo Ocampo
# Importamos la libreria io
from io import *
# Creamos una clase para libros
class Libros:
    # Creamos sus atributos
    titulo = " "
    autor = " "
    editorial = " "
    numero_paginas = 0
    genero = " "
    
    # Creamos sus metodos
    def leer_libro():
        print("Leyendo libro")
    def escribir_libro():
        print("Escribiendo libro")

# Creamos una clase para casas
class Casa:
    # Creamos sus atributos
    material = " "
    color = " "
    numero_pisos = 0
    numero_habitaciones = 0
    direccion = " "
    
    # Creamos sus metodos
    def vivir_en_casa():
        print("Viviendo en casa")
    
    def construir_casa():
        print("Construyendo casa")

# Creamos una clase para peliculas
class Pelicula:
    # Creamos sus atributos
    titulo = " "
    director = " "
    genero = " "
    duracion = 0
    genero = ""
    
    # Creamos sus metodos
    def ver_pelicula():
        print("Viendo pelicula")
    
    def grabar_pelicula():
        print("Grabando pelicula")

# Creamos una clase para bodegas
class Bodega:
    # Creamos sus atributos
    nombre = " "
    direccion = " "
    numero_empleados = 0
    productos = []
    capacidad = 0
    
    # Creamos sus metodos
    def disponibilidad():
        print("Disponibilidad de productos")
    
    def retirar_productos():
        print("Retirar productos")

# Creamos una clase para lamparas
class Lampara:
    # Creamos sus atributos
    estado = " "
    color = " "
    tipo = " "
    material = 0
    potencia = 0
    
    # Creamos sus metodos
    def encender_lampara():
        print("Encendiendo lampara")
    
    def apagar_lampara():
        print("Apagando lampara")

# Creamos una clase para modems
class Modem:
    # Creamos sus atributos
    marca = " "
    velocidad = 0
    modelo = " "
    puertos = 0
    estado = " "
    
    # Creamos sus metodos
    def reiniciar():
        print("Reiniciando modem")
    
    def conectar_modem():
        print("Conectado a modem")

# Creamos una clase para routers
class Router:
    # Creamos sus atributos
    marca = " "
    velocidad = 0
    modelo = " "
    alcance = 0
    antenas = " "
    
    # Creamos sus metodos
    def conectar_router():
        print("Conectando router")
    
    def cambiar_contrasenia():
        print("Cambiando contraseña")

# Creamos una clase para maletines
class Maletin:
    # Creamos sus atributos
    marca = " "
    color = " "
    capacidad = 0
    compartimientos = 0
    material = " "
    
    # Creamos sus metodos
    def guardar_objetos():
        print("Guardando objetos")
    
    def llevar_objetos():
        print("Llevando objetos")
    
# Creamos una clase para pacientes oncológicos
class PacienteOncologico:
    # Creamos sus atributos
    nombre = " "
    eps = " "
    tipo = " "
    estado_salud = " "
    progresion = " "
    
    # Creamos sus metodos
    def recibir_tratamiento():
        print("Recibiendo tratamiento")
    
    def mejorar_salud():
        print("Mejorando salud")
    
# Creamos una clase para gatos
class Gato:
    # Creamos sus atributos
    nombre = " "
    raza = " "
    dueño = " "
    color = " "
    edad = 0
    
    # Creamos sus metodos
    def maullar():
        print("Maullando")
    
    def comer():
        print("Comiendo")