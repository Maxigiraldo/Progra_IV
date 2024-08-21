# Iniciar lista para las cadenas
cadenas = []

# Bucle para que el usuario ingrese las cadenas que desee
for i in range(10):
    cadena = input("Ingrese una cadena: ")
    cadenas.append(cadena)

# Variable para llevar el conteo
caracteres = 0

# Bucle para contar las letras que no sean vocales
for cadena in cadenas:
    for caracter in cadena:
        if caracter.lower() not in "aeiou":
            caracteres += 1

# Mostrar resultados
print(f"El total de caracteres que no son vocales son: {caracteres}")
