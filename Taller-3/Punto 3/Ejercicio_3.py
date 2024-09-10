# Por Maximiliano Giraldo Ocampo
# Clase empleado
class Empleado:
    # Constructor
    def __init__(self, nombre, genero, edad, fecha_ingreso, valor_hora, horas_trabajadas):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.fecha_ingreso = fecha_ingreso
        self.valor_hora = valor_hora
        self.horas_trabajadas = horas_trabajadas
    
    # Métodos
    # Calcular salario
    def calcular_salario(self):
        return self.valor_hora * self.horas_trabajadas
    
    # Calcular antigüedad
    def antiguedad(self):
        return 2024 - self.fecha_ingreso
    
    # Calcular cuando se pensiona
    def pension(self):
        if self.genero.upper() == 'M':
            return 62 - self.edad
        else:
            return 57 - self.edad
    
    # Calcular cuanto se paga de salud
    def salud(self):
        salario = self.calcular_salario()
        return salario * 0.04
    
    # Calcular cuanto se paga de pensión
    def pension(self):
        salario = self.calcular_salario()
        return salario * 0.04
    
    # Calcular pensión anual
    def pension_anual(self):
        return self.pension() * 12
    
    # Guardar datos en archivo
    def guardar_datos(self, archivo):
        with open(archivo, 'a') as file:
            file.write(f"Nombre: {self.nombre}\n")
            file.write(f"Género: {self.genero}\n")
            file.write(f"Edad: {self.edad}\n")
            file.write(f"Fecha de ingreso: {self.fecha_ingreso}\n")
            file.write(f"Valor hora: {self.valor_hora}\n")
            file.write(f"Horas trabajadas: {self.horas_trabajadas}\n")
            file.write(f"Salario: {self.calcular_salario()}\n")
            file.write(f"Antigüedad: {self.antiguedad()}\n")
            file.write(f"Pensión: {self.pension()}\n")
            file.write(f"Salud: {self.salud()}\n")
            file.write(f"Pensión anual: {self.pension_anual()}\n")
            file.write("\n")

# Ingreso de empleados
def ingreso():
    empleados = []
    while True:
        nombre = input("Ingrese el nombre del empleado: ")
        genero = input("Ingrese el género del empleado (M/F): ")
        edad = int(input("Ingrese la edad del empleado: "))
        while True:
            fecha_ingreso = int(input("Ingrese la fecha de ingreso del empleado: "))
            if fecha_ingreso < 2000 or fecha_ingreso > 2024:
                print("Fecha de ingreso invalida.")
            else:
                break
        valor_hora = float(input("Ingrese el valor de la hora del empleado: "))
        horas_trabajadas = int(input("Ingrese las horas trabajadas del empleado: "))
        empleado = Empleado(nombre, genero, edad, fecha_ingreso, valor_hora, horas_trabajadas)
        empleados.append(empleado)
        empleado.guardar_datos('empleados.txt')
        continuar = input("Desea ingresar otro empleado? (S/N): ")
        if continuar == 'N':
            break
    return empleados

ingreso()