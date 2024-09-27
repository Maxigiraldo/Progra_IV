# Presentado por: Maximiliano Giraldo Ocampo
class Vehiculo:
    # Constructor de la clase
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    # Métodos de la clase
    def duracion_llantas(self, marca, tipo):
        if marca == "Michelin":
            if tipo == "camión":
                print("Las llantas duran 5 años")
            elif tipo == "moto":
                print("Las llantas duran 3 años")
            else:
                print("Las llantas duran 4 años")
        elif marca == "Pirelli":
            if tipo == "camión":
                print("Las llantas duran 4 años")
            elif tipo == "moto":
                print("Las llantas duran 2 años")
            else:
                print("Las llantas duran 3 años")
        else:
            if tipo == "camión":
                print("Las llantas duran 3 años")
            elif tipo == "moto":
                print("Las llantas duran 1 años")
            else:
                print("Las llantas duran 2 años")

    def combustible(self, tipo):
        if tipo == "camión":
            print("Se recomienda usar ACPM")
        elif tipo == "moto":
            print("Se recomienda usar gasolina Corriente")
        else:
            print("Se recomienda usar gasolina Extra")

class Coches(Vehiculo):
    # Constructor de la clase
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas) # Llama al constructor de la clase padre
        self.velocidad = velocidad
        self.cilindraje = cilindrada
    # Métodos de la clase
    def tiempo_viaje(self, distancia):
        tiempo = distancia/self.velocidad
        print(f"El tiempo de viaje es de: {tiempo} horas")
    
    def costo(self, km_por_litro):
        costo = (1000/km_por_litro) * 15000
        print(f"El costo mensual de gasolina es de: {costo} pesos")    

def menu():
    print("""Que desea hacer?
    1, Ingresar vehículo
    2. Calcular tiempo de viaje
    3. Calcular costo de gasolina
    4. Calcular duración de llantas
    5. Recomendación de combustible
    6. Salir""")

def tipo_vehiculo():
    print("""
    ¿Qué tipo de vehículo es?
    1. Camión
    2. Moto
    3. Carro
    """)
    tipo = int(input("Digite el tipo: "))
    if tipo == 1:
        tipo = "camión"
    elif tipo == 2:
        tipo = "moto"
    else:
        tipo = "carro"
    return tipo

vehiculos = []

# Menú de opciones
while True:
    menu()
    opcion = int(input("Digite la opción: "))
    if opcion == 1:
        color = input("Digite el color del vehículo: ")
        ruedas = int(input("Digite el número de ruedas del vehículo: "))
        velocidad = int(input("Digite la velocidad del vehículo: "))
        cilindrada = int(input("Digite el cilindrada del vehículo: "))
        # Instancia de la clase Coches
        vehiculo = Coches(color, ruedas, velocidad, cilindrada)
        vehiculos.append(vehiculo)
    elif opcion == 2:
        print("""
        ¿A dónde desea viajar?
        1. Bogotá
        2. Medellín
        3. Cali
        4. Barranquilla
        5. Cartagena
        """)
        destino = int(input("Digite el destino: "))
        if destino == 1:
            distancia = 317
        elif destino == 2:
            distancia = 231
        elif destino == 3:
            distancia = 215
        elif destino == 4:
            distancia = 707
        elif destino == 5:
            distancia = 649
        vehiculo.tiempo_viaje(distancia)
    elif opcion == 3:
        km_por_litro = float(input("Digite los km por litro del vehículo: "))
        vehiculo.costo(km_por_litro)
    elif opcion == 4:
        print("""
        ¿De qué marca son las llantas?
        1. Michelin
        2. Pirelli
        3. Goodyear
        """)
        marca = int(input("Digite la marca: "))
        if marca == 1:
            marca = "Michelin"
        elif marca == 2:
            marca = "Pirelli"
        else:
            marca = "Goodyear"
        tipo = tipo_vehiculo()
        vehiculo.duracion_llantas(marca, tipo)
    elif opcion == 5:
        tipo = tipo_vehiculo()
        vehiculo.combustible(tipo)
    elif opcion == 6:
        archivo = open("vehiculo.txt", "a")
        for vehiculo in vehiculos:
            archivo.write("--------------\n")
            archivo.write(f"Color: {vehiculo.color}\n")
            archivo.write(f"Número de ruedas: {vehiculo.ruedas}\n")
            archivo.write(f"Velocidad: {vehiculo.velocidad}\n")
            archivo.write(f"Cilindrada: {vehiculo.cilindrada}\n")
            archivo.write("--------------\n")
        archivo.close()   
        break
    else:
        print("Opción no válida")
