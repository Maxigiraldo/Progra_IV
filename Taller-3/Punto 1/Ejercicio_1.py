# Por Maximiliano Giraldo Ocampo
class Avion:
    # Constructor de la clase, en el que incluiremos los atributos de la clase, abstrayendo los datos que se necesitan para crear un objeto de la clase en cuestión
    def __init__(self, modelo, capacidad, velocidad, peso):
        self.modelo = modelo
        self.capacidad = capacidad
        self.velocidad = velocidad
        self.peso = peso
    
    # Métodos de la clase, en este caso, incluiremso los métodos que podrían realizar los objetos de la clase, por ahora serán métodos simples para representarlo
    def volar(self):
        print("El avión está volando")
        
    def aterrizar(self):
        print("El avión está aterrizando")
    
# El resto de las clases se crean de la misma manera, con la diferencia de que se cambian los atributos y los métodos de la clase dependiendo de lo que se necesite
class Celular:
    # Constructor de la clase
    def __init__(self, marca, modelo, color, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = almacenamiento
    
    # Métodos de la clase
    def llamar(self):
        print("Llamando...")
        
    def enviar_mensaje(self):
        print("Mensaje enviado")
        
class Asignatura:
    # Constructor de la clase
    def __init__(self, nombre, creditos, docente, horario):
        self.nombre = nombre
        self.creditos = creditos
        self.docente = docente
        self.horario = horario
        
    # Métodos de la clase
    def empezar_clase(self):
        print("La clase ha comenzado")
        
    def terminar_clase(self):
        print("La clase ha terminado")
    
class Ejercito:
    def __init__(self, nombre, soldados, armas, vehiculos):
        self.nombre = nombre
        self.soldados = soldados
        self.armas = armas
        self.vehiculos = vehiculos
    
    def entrenar(self):
        print("Entrenando...")
    
    def atacar(self):
        print("Atacando...")

class Silla:
    def __init__(self, material, espaldar, tamanio, color):
        self.material = material
        self.espaldar = espaldar
        self.tamanio = tamanio
        self.color = color
        
    def sentarse(self):
        print("Sentado...")
    
    def recostarse(self):
        print("Recostado...")

class Audifonos:
    def __init__(self, tipo, microfono, color, calidad):
        self.tipo = tipo
        self.microfono = microfono
        self.color = color
        self.calidad = calidad
        
    def escuchar(self):
        print("Escuchando...")
    
    def hablar(self):
        print("Hablando...")
