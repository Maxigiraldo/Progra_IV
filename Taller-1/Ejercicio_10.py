# Lista inicial
Lista = ["casa", "programacion", "utp", "universidad", "utp", "casa", "casa", " thj", "vbh", "456", "987"]


# Funcion para borrar las cadenas repetidas
def borrar_repetidos():
    Lista_unica = []
    for elemento in Lista:
        if elemento not in Lista_unica:
            Lista_unica.append(elemento)
    return Lista_unica

# Funcion para eliminar las cadenas sin vocales
def borrar_sin_vocales():
    Lista_vocales = []
    for elemento in Lista:
        contador = 0
        for caracter in elemento:
            if caracter in "aeiou":
                contador += 1
        if contador > 0:
            Lista_vocales.append(elemento)
    return Lista_vocales

# Funcion para organizar por nivel alfabetico
def organizar_alfabeticamente(Lista):
    n = len(Lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if Lista[j] > Lista[j+1]:
                Lista[j], Lista[j+1] = Lista[j+1], Lista[j]
    return Lista

Lista = borrar_repetidos()
print(Lista)
Lista = borrar_sin_vocales()
print(Lista)
print(organizar_alfabeticamente(Lista))