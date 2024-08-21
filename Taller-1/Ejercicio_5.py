# Iniciar lista para el ingreso de cadenas
lista = []

# Bucle para ingresar las palabras que el usuario desee
while True:
    cadena = input("Ingrese una palabra o SALIR para terminar: ")
    if cadena.upper() == "SALIR":
        break
    else:
        lista.append(cadena)

# Variable para la cadena mayor
cadena_mayor = lista[0]

# Variable para la cadena menor
cadena_menor = lista[0]

# Bucles para comparar las palabras para detectar la mayor y la menor y cambiarlas dependiendo el caso
for palabra in lista:
    if len(palabra) > len(cadena_mayor):
        cadena_mayor = palabra

for palabra in lista:
    if len(palabra) < len(cadena_menor):
        cadena_menor = palabra

# Impresion de las cadenas
print(f"Cadena mayor: {cadena_mayor}")
print(f"Cadena menor: {cadena_menor}")
