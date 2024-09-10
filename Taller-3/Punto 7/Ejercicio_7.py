# Por Maximiliano Giraldo Ocampo
# Libreria que nos permite realizar procesos como stdin, stdout, stderr, etc.
import subprocess

# Función que imprime el menu de opciones
def imprimir_menu():
    print("Ingrese el numero del ejercicio que desea ejecutar: ")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Salir")

# Función principal, en esta función usamos el método de la librería run de subprocess para ejecutar los scripts de los ejercicios
def main():
    while True:
        imprimir_menu()
        option = int(input())
        if option == 1:
            subprocess.run(["python3", "../Punto 1/Ejercicio_1.py"])
        elif option == 2:
            subprocess.run(["python3", "../Punto 2/Ejercicio_2.py"])
        elif option == 3:
            subprocess.run(["python3", "../Punto 3/Ejercicio_3.py"])
        elif option == 4:
            subprocess.run(["python3", "../Punto 4/Ejercicio_4.py"])
        elif option == 5:
            subprocess.run(["python3", "../Punto 5/Ejercicio_5.py"])
        elif option == 6:
            subprocess.run(["python3", "../Punto 6/Ejercicio_6.py"])
        elif option == 7:
            print("Saliendo...")
            break

# Ejecutamos la función principal
main()

#Nota: Los archivos que se creen en los ejercicios se crean en la carpeta donde se encuentra el archivo de ejecución.