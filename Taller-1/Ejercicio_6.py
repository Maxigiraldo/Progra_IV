# Iniciar lista para las cadenas
cadenas = []

# Iniciar variable booleana para el bucle while
estado = True

# Bucle para que el usuario ingrese las cadenas que desee
while estado:
    cadena = input("Ingrese una cadena, ingrese SALIR para acabar: ")
    if cadena.upper() == 'SALIR':
        estado = False
    else:
        cadenas.append(cadena)

# Valor entero que el usuario ingresara para usarlo como longitud de cadenas
longitud = int(input("Ingrese la longitud de las cadenas que desea buscar: "))

# Bucle en el que se itera por toda la lista  buscando las cadenas de la longitud ingresada por el usuario
for cadena in cadenas:
    if longitud == len(cadena):
        print(f" --> {cadena}")