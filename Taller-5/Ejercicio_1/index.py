class PersonalUniversitario:
    def __init__(self, nombre, edad, fecha_ingreso, identificacion, genero, correo):
        self.nombre = nombre
        self.edad = edad
        self.fecha_ingreso = fecha_ingreso
        self.identificacion = identificacion
        self.genero = genero
        self.correo = correo
    
    def antiguedad(self):
        return 2024 - self.fecha_ingreso
    

class Profesor(PersonalUniversitario):
    def __init__(self, nombre, edad, fecha_ingreso, identificacion, genero, correo, horas, sueldo_hora, tipo, departamento, grado_academico, experiencia):
        # Inicializar atributos de PersonalUniversitario
        PersonalUniversitario.__init__(self, nombre, edad, fecha_ingreso, identificacion, genero, correo)
        # Inicializar atributos de Profesor
        self.horas = horas
        self.sueldo_hora = sueldo_hora
        self.tipo = tipo
        self.departamento = departamento    
        self.grado_academico = grado_academico
        self.experiencia = experiencia
        
    def salario(self):
        if self.tipo == 'auxiliar':
            valor = 1.25
        elif self.tipo == 'asistente':
            valor = 2
        elif self.tipo == 'asociado':
            valor = 2.25
        elif self.tipo == 'titular':
            valor = 2.5
        return self.horas * self.sueldo_hora * valor
    
    def mostrar_materias(self):
        if self.tipo == 'titular':
            return ['Inteligencia Artificial Avanzada', 'Teoría de la computacion', 'Seminario de Investigacion en Ciencias Computacionales']
        elif self.tipo == 'asociado':
            return ['Algoritmos y Estructuras de Datos II', 'Disenio de Compiladores', 'Sistemas Distribuidos']
        elif self.tipo == 'asistente':
            return ['Matematicas Basicas', 'Fundamentos de Programacion', 'Algoritmos y Logica']
        elif self.tipo == 'auxiliar':
            return ['Calculo Multivariable', 'POO', 'Introduccion a Bases de Datos']

class Estudiante(PersonalUniversitario):
    def __init__(self, nombre, edad, fecha_ingreso, identificacion, genero, correo, carrera, creditos, promedio, beca, semestre, actividades_extracurriculares):
        # Inicializar atributos de PersonalUniversitario
        PersonalUniversitario.__init__(self, nombre, edad, fecha_ingreso, identificacion, genero, correo)
        # Inicializar atributos de Estudiante
        self.carrera = carrera
        self.creditos = creditos
        self.promedio = promedio
        self.beca = beca
        self.semestre = semestre
        self.actividades_extracurriculares = actividades_extracurriculares

class AyudanteProfesor(Profesor, Estudiante):
    def __init__(self, nombre, edad, fecha_ingreso, identificacion, genero, correo, horas, sueldo_hora, tipo, departamento, grado_academico, experiencia, carrera, creditos, promedio, beca, semestre, actividades_extracurriculares):
        # Llamar al constructor de Profesor
        Profesor.__init__(self, nombre, edad, fecha_ingreso, identificacion, genero, correo, horas, sueldo_hora, tipo, departamento, grado_academico, experiencia)
        # Llamar al constructor de Estudiante
        Estudiante.__init__(self, nombre, edad, fecha_ingreso, identificacion, genero, correo, carrera, creditos, promedio, beca, semestre, actividades_extracurriculares)

# Crear instancias
persona_1 = AyudanteProfesor('Juan', 25, 2019, 123456, 'M', 'juan@gmail', 20, 10, 'auxiliar', 'Ingenieria', 'Maestria', 2, 'Ingenieria', 100, 4.5, 'Si', 5, 'Deportes')
persona_2 = Estudiante('Juan', 25, 2019, 123456, 'M', 'juan@gmail', 'Ingenieria', 100, 4.5, 'Si', 5, 'Deportes')
persona_3 = Profesor('Juan', 25, 2019, 123456, 'M', 'juan@gmail', 20, 10, 'auxiliar', 'Ingenieria', 'Maestria', 2)

lista_personas = [persona_1, persona_2, persona_3]

# Pruebas
print(persona_1.salario())
print(persona_2.antiguedad())
print(persona_3.mostrar_materias())

def guardar_datos(persona):
    with open('personal.txt', 'a') as archivo:
        for persona in lista_personas:
            archivo.write(f'{persona.nombre}, {persona.fecha_ingreso}, {persona.correo}\n')
            # isinstance verifica si un objeto es una instancia de una clase, lo usamos para verificar si la persona es un estudiante o un profesor asi poder guardar los datos correspondientes 
            if isinstance(persona, Estudiante):
                archivo.write(f'{persona.carrera}, {persona.creditos}, {persona.promedio}, {persona.beca}\n')
                archivo.write('\n')
            elif isinstance(persona, Profesor):
                archivo.write(f'{persona.horas}, {persona.sueldo_hora}, {persona.tipo}, {persona.departamento}, {persona.grado_academico}, {persona.experiencia}\n')
                archivo.write('\n')

guardar_datos(lista_personas)



