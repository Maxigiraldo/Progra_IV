import random

# lista para los numeros
numeros = []

# Bucle para llenar la lista
for i in range(15):
    numeros.append(random.randint(1,20))

# Bucle para mostrar los numeros y sus potencias cuadradas y cubicas
for i in numeros:
    print(f"{i} - {i**2} - {i**3}")