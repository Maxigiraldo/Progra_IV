# Por Maximiliano Giraldo Ocampo
from math import  *
# Creacion de la clase Calculadora
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def suma(self):
        return self.numero1 + self.numero2
    
    def resta(self):
        return self.numero1 - self.numero2
    
    def multiplicacion(self):
        return self.numero1 * self.numero2
    
    def division(self):
        if self.numero2 == 0:
            return "Error: Division por cero"  
        else:
            return self.numero1 / self.numero2
    
    def potencia(self):
        return pow(self.numero1, self.numero2)
    
    def raiz(self):
        return sqrt(self.numero1)
    
    def logaritmo(self):
        return log(self.numero1)
    
    def seno(self):
        return sin(self.numero1)
    
    def coseno(self):
        return cos(self.numero1)
    
    def tangente(self):
        return tan(self.numero1)
    
    def factorial(self):
        return factorial(int(self.numero1))
    
    def exponencial(self):
        return exp(self.numero1)


# Funcion para mostrar el menu
def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Logaritmo")
    print("8. Seno")
    print("9. Coseno")
    print("10. Tangente")
    print("11. Factorial")
    print("12. Exponencial")
    print("13. Salir")
# Funcion principal    
def main():
    # Ingreso de datos
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    # Creacion de objeto
    calculadora = Calculadora(num1, num2)
    
    # Menu de opciones y calculos
    while True:
        menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            print("La suma es: ", calculadora.suma())
        elif opcion == 2:
            print("La resta es: ", calculadora.resta())
        elif opcion == 3:
            print("La multiplicacion es: ", calculadora.multiplicacion())
        elif opcion == 4:
            print("La division es: ", calculadora.division())
        elif opcion == 5:
            print("La potencia es: ", calculadora.potencia())
        elif opcion == 6:
            print("La raiz cuadrada es: ", calculadora.raiz())
        elif opcion == 7:
            print("El logaritmo es: ", calculadora.logaritmo())
        elif opcion == 8:
            print("El seno es: ", calculadora.seno())
        elif opcion == 9:
            print("El coseno es: ", calculadora.coseno())
        elif opcion == 10:
            print("La tangente es: ", calculadora.tangente())
        elif opcion == 11:
            print("El factorial es: ", calculadora.factorial())
        elif opcion == 12:
            print("La exponencial es: ", calculadora.exponencial())
        elif opcion == 13:
            break
        else:
            print("Opcion incorrecta")
        
main()