# Iniciar lista vacia en la que se agregaran aignaturas
asignaturas = []
# Iniciar lista vacia con las notas totales
notas_totales = []

# Ingreso de las asignaturas
print("Ingrese las asignaturas, ingrese SALIR para terminar:")
while True:
    materia_nueva = input("Ingrese la asignatura: ")
    if materia_nueva.upper() != 'SALIR':
        asignaturas.append(materia_nueva)
    else:
        break

# Ingreso de las notas
print("Ingreso de notas")
for i in range(len(asignaturas)):
    print(f"-> {asignaturas[i]}")
    # Crear una lista donde se ingresaran las notas de cada materia
    notas = []
    for j in range(4):
        notas.append(float(input("Ingrese la nota: ")))
    # Añadir la lista de las notas de la materia en la lista de todas las notas
    notas_totales.append(notas)

# Crear lista donde se agregaran los promedios de cada materia
promedio_total = []

# Mostrar los resultados de las materias
print("Resultado de notas")
for i in range(len(asignaturas)):
    print(asignaturas[i])
    promedio = 0
    # Mostrar las notas y sumarlas para el promedio
    for j in range(len(notas_totales[i])):
        print(f"nota{j + 1} - {notas_totales[i][j]:.1f}")
        promedio += notas_totales[i][j]
    # Promedio final de la materia y muestra en pantalla si perdio o paso la materia
    promedio /= len(notas_totales[i])
    print(f"el promedio de {asignaturas[i]} es de {promedio:.1f} - ")
    if promedio < 3:
        print("Asignatura perdida")
    else:
        print("Asignatura ganada")
    promedio_total.append(promedio)

# Variable que se usara para calcular el promedio del semestre
promedio_semestre = 0

for nota in promedio_total:
    promedio_semestre += nota

promedio_semestre /= len(promedio_total)

# Mostrar si paso o perdió el semestre
if promedio_semestre < 3:
    print(f"Promedio general: {promedio_semestre:.1f} - semestre perdido")
elif promedio_semestre < 4:
    print(f"Promedio general: {promedio_semestre:.1f} - semestre ganado")
else:
    print(f"Promedio general: {promedio_semestre:.1f} - Felicidades seras becado")