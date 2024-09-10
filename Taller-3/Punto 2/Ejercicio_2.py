# Por Maximiliano Giraldo Ocampo
# Creación de la clase Rectangulo con los métodos área e imprimir_rectangulo
class Rectangulo:
    # Constructor de la clase con los atributos base y altura
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    # Método que calcular el área del rectángulo
    def area(self):
        return self.base * self.altura
    # Método que imprime el rectángulo
    def imprimir_rectangulo(self):
        for i in range(self.altura):
            if i == 0 or i == self.altura - 1:
                print(' * ' * self.base)
            else:
                print(' * ' + '   ' * (self.base - 2) + ' * ')

# Ingreso de datos para la base y altura del rectángulo que usaremos como atributos
base = int(input('Ingrese la base del rectángulo: '))
altura = int(input('Ingrese la altura del rectángulo: '))
# Creación del objeto rectangulo de la clase Rectangulo
rectangulo = Rectangulo(base, altura)
# Impresión del área del rectángulo y el rectángulo
print(f'Área del rectángulo: {rectangulo.area()}')
rectangulo.imprimir_rectangulo()
