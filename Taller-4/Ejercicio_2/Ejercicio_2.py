# Por Maximiliano Giraldo Ocampo
# Superclase
class Vehiculos:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

# Subclases
class Coche(Vehiculos):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindraje, carga):
        super().__init__(color, ruedas, velocidad, cilindraje)
        self.carga = carga

class Bicicleta(Vehiculos):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

def impresion(vehiculo):
    if type(vehiculo) is Coche:
        print(f"Coche -> Color: {vehiculo.color}, Ruedas: {vehiculo.ruedas}, Velocidad: {vehiculo.velocidad}, Cilindrada: {vehiculo.cilindrada}")
    elif type(vehiculo) is Camioneta:
        print(f"Camioneta -> Color: {vehiculo.color}, Ruedas: {vehiculo.ruedas}, Velocidad: {vehiculo.velocidad}, Cilindrada: {vehiculo.cilindrada}, Carga: {vehiculo.carga}")
    elif type(vehiculo) is Bicicleta:
        print(f"Bicicleta -> Color: {vehiculo.color}, Ruedas: {vehiculo.ruedas}, Tipo: {vehiculo.tipo}")
    else:
        print(f"Motocicleta -> Color: {vehiculo.color}, Ruedas: {vehiculo.ruedas}, Tipo: {vehiculo.tipo}, Velocidad: {vehiculo.velocidad}, Cilindrada: {vehiculo.cilindrada}")

def catalogar(ruedas, vehiculos):
    if ruedas is not None:
        contador = 0
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                contador += 1
        return contador
    else:
        for vehiculo in vehiculos:
            impresion(vehiculo)

def main():
    vehiculos = []
    
    # Instancias
    coche_1 = Coche("Rojo", 4, 150, 1500)
    vehiculos.append(coche_1)
    coche_2 = Coche("Azul", 4, 200, 1600)
    vehiculos.append(coche_2)
    coche_3 = Coche("Verde", 4, 180, 2000)
    vehiculos.append(coche_3)
    camioneta_1 = Camioneta("Blanco", 4, 100, 3000, 1500)
    vehiculos.append(camioneta_1)
    camioneta_2 = Camioneta("Negar", 4, 120, 3500, 1600)
    vehiculos.append(camioneta_2)
    camioneta_3 = Camioneta("Gris", 4, 110, 2800, 1400)
    vehiculos.append(camioneta_3)
    bicicleta_1 = Bicicleta("Amarillo", 2, "Urbana")
    vehiculos.append(bicicleta_1)
    bicicleta_2 = Bicicleta("Naranja", 2, "Deportiva")
    vehiculos.append(bicicleta_2)
    bicicleta_3 = Bicicleta("Violeta", 0, "Urbana")
    vehiculos.append(bicicleta_3)
    motocicleta_1 = Motocicleta("Cafe", 2, "Deportiva", 250, 1200)
    vehiculos.append(motocicleta_1)
    motocicleta_2 = Motocicleta("Negra", 2, "Deportiva", 200, 1000)
    vehiculos.append(motocicleta_2)
    motocicleta_3 = Motocicleta("Blanca", 2, "Urbana", 160, 800)
    vehiculos.append(motocicleta_3)
    
    # Menu
    while True:
        print("""    Menu 
                1. Catalogar vehiculos
                2. Mostrar cantidad de vehiculos por ruedas
                3. Salir
                """)
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            catalogar(None, vehiculos)
        elif opcion == 2:
            numero_ruedas = int(input("Ingrese el numero de ruedas: "))
            total = catalogar(numero_ruedas, vehiculos)
            print(f"Se han encontrado {total} vehiculos con {numero_ruedas} ruedas")            
        elif opcion == 3:
            print("Cerrando...")
            break
        else:
            print("Opcion invalida")

main()