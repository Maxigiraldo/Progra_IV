# Clase principal
class FiguraGeometrica:
    def __init__(self, ancho):
        # Encapsulamiento del atributo 
        self.__ancho = ancho
    # Metodos set y get
    def set_ancho(self, ancho):
        if ancho < 0:
            print("El ancho no puede ser negativo")
        else:
            self.__ancho = ancho
    def get_ancho(self):
        return self.__ancho

# Subclases
class Cuadrado(FiguraGeometrica):
    def __init__(self, ancho):
        super().__init__(ancho)
    
    def area(self):
        ancho = self.get_ancho()
        return ancho * ancho
    
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__(ancho)
        self.__alto = alto
    
    def set_alto(self, alto):
        if alto < 0:
            print("El alto no puede ser negativo")
        else:
            self.__alto = alto
    
    def get_alto(self):
        return self.__alto
    
    def area(self):
        ancho = self.get_ancho()
        alto = self.get_alto()
        return ancho * alto

class Triangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__(ancho)
        self.__alto = alto
    
    def set_alto(self, alto):
        if alto < 0:
            print("El alto no puede ser negativo")
        else:
            self.__alto = alto
    
    def get_alto(self):
        return self.__alto
    
    def area(self):
        ancho = self.get_ancho()
        alto = self.get_alto()
        return (ancho * alto) / 2
    
class Circulo(FiguraGeometrica):
    def __init__(self, ancho):
        super().__init__(ancho)

    def area(self):
        radio = self.get_ancho()
        return 3.1416 * (radio ** 2)

def main():
    while True:
        print("Que figura desea calcular el area?")
        print("1. Cuadrado")
        print("2. Rectangulo")
        print("3. Triangulo")
        print("4. Circulo")
        print("5. Salir")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            ancho = float(input("Ancho: "))
            cuadrado = Cuadrado(ancho)
            cuadrado.set_ancho(ancho)
            print("Area: ", cuadrado.area())
        elif opcion == 2:
            ancho = float(input("Ancho: "))
            alto = float(input("Alto: "))
            rectangulo = Rectangulo(ancho, alto)
            rectangulo.set_alto(alto)
            rectangulo.set_ancho(ancho)
            print("Area: ", rectangulo.area())
        elif opcion == 3:
            ancho = float(input("Ancho: "))
            alto = float(input("Alto: "))
            triangulo = Triangulo(ancho, alto)
            triangulo.set_alto(alto)
            triangulo.set_ancho(ancho)
            print("Area: ", triangulo.area())
        elif opcion == 4:
            ancho = float(input("Radio: "))
            circulo = Circulo(ancho)
            circulo.set_ancho(ancho)
            print("Area: ", circulo.area())
        elif opcion == 5:
            break
        else:
            print("Opcion invalida")

main()