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

# Variable para el caracter que el usuario ingresará
caracter = input("Ingrese una caracter: ")

# Busqueda e impresión de las palabras que contengan dicho caracter, a su vez si son pares o no
for cadena in cadenas:
    for letras in cadena:
        if letras == caracter:
            if len(cadena) % 2 == 0:
                print(f" --> {cadena} par")
                break
            else:
                print(f" --> {cadena} impar")
                break
