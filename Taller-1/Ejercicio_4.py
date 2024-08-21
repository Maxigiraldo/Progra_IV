# Variable para que el usuario inicie el tamaño de la lista
cantidad_lista = int(input("Ingrese la cantidad de numeros que desea agregar: "))

# lista de los numeros a agregar
numeros = []

# Bucle en el que el usuario agregara los numero a una lista
for i in range(cantidad_lista):
    numeros.append(int(input("Ingrese un numero: ")))

# Bucle para mostrar los numero junto su cuadrado y cubo respectivamente
for numero in numeros:
    print(f"{numero} - {numero ** 2} - {numero ** 3}")