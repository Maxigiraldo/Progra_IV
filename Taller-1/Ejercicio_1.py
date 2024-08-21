# Iniciar lista vacia en la que se agregaran aignaturas
asignaturas = []

# Funcion para ingresar asignaturas a la lista
def ingreso_asignaturas():
  asignaturas.append(input("Ingrese la asignatura: "))

# Funcion para imprimir las asignaturas
def ver_asignaturas():
  for materias in asignaturas:
    print(f"--> {materias}")

# Menu de opciones
def main():
  while True:
    print("1. Ingresar materia")
    print("2. Ver materia")
    print("0. Salir")
    opciones = int(input("Ingrese la opcion: "))
    if opciones == 1:
      ingreso_asignaturas()
    elif opciones == 2:
      ver_asignaturas()
    else:
      break

main()