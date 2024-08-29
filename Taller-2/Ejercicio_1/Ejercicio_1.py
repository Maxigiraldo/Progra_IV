# Ejercicio 1 Maximiliano Giraldo Ocampo
# Impportamos la libreria io
from io import *

# Creamos una lista vacia para almacenar los numeros ingresados
lista_ingreso = []

# Creamos una lista vacia para almacenar la suma de los digitos de los numeros ingresados
def ingreso():
    print("Ingrese un numero de dos cifras, para finalizar ingrese 0")
    estado = True
    while estado:
        num = int(input("Ingrese un numero: "))
        if num == 0:
            estado = False
        else:
            # Verificamos que el numero ingresado sea de dos cifras
            if num > 9 and num < 100:
                lista_ingreso.append(num)
            else:
                print("El numero ingresado no es de dos cifras")

# Creamos una lista vacia para almacenar la suma de los digitos de los numeros ingresados
lista_suma = []

# Creamos una funcion para sumar los digitos de los numeros ingresados
def suma():
    for numero in lista_ingreso:
        suma = 0
        # Obtenemos el primer digito del numero
        numero_1 = numero // 10
        # Obtenemos el segundo digito del numero
        numero_2 = numero % 10
        suma = numero_1 + numero_2
        lista_suma.append(suma)    
    print (lista_suma)

# Creamos una funcion para ingresar los resultados en un archivo
def ingreso_archivo():
    archivo = open("numeros.txt", "a")
    for suma in lista_suma:
        archivo.write(f"{suma}\n")
    archivo.close()
    
# Llamamos a las funciones
ingreso()
suma()
ingreso_archivo()
