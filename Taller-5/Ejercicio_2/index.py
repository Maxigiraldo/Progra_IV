# Problema relacionado con el transporte
# ------------------------------------- Clases principales ---------------------------------------------
class Transporte:
    def __init__(self, capacidad, costo, velocidad, color, tipo):
        self.capacidad = capacidad
        self.costo = costo
        self.velocidad = velocidad
        self.color = color
        self.tipo = tipo
    
    def calcular_tiempo(self, distancia):
        return distancia / self.velocidad
    
    def calcular_costo(self, distancia):
        return distancia * self.costo
    
    def calcular_costo_ida_vuelta(self, distancia):
        return 2 * self.calcular_costo(distancia)
    
    def verificar_capacidad(self, num_personas):
        return num_personas <= self.capacidad
    
    def actualizar_costo(self, nuevo_costo):
        self.costo = nuevo_costo

class Persona:
    def __init__(self, nombre, edad, sexo, telefono, direccion):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.telefono = telefono
        self.direccion = direccion        
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Sexo: {self.sexo}')
        print(f'Telefono: {self.telefono}')
        print(f'Direccion: {self.direccion}')

class Usuario(Persona):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia):
        super().__init__(nombre, edad, sexo, telefono, direccion)
        self.saldo = saldo
        self.distancia = distancia
        
    def agregar_saldo(self, cantidad):
        self.saldo += cantidad

    def verificar_saldo(self):
        return self.saldo
    
    def descontar_saldo(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente.")

# --------------------------------------------------- Clases secundarias ------------------------------------------
class Estudiante(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, universidad, carrera, semestre):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.universidad = universidad  
        self.carrera = carrera
        self.semestre = semestre
    
    def mostrar_info_universidad(self):
        print(f'Universidad: {self.universidad}')
        print(f'Carrera: {self.carrera}')
        print(f'Semestre: {self.semestre}')

class Profesor(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, universidad, departamento, salario_hora, horas):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.universidad = universidad
        self.departamento = departamento
        self.salario_hora = salario_hora
        self.horas = horas
    
    def calcular_salario(self):
        return self.salario_hora * self.horas
    
    def mostrar_info_profesor(self):
        print(f'Universidad: {self.universidad}')
        print(f'Departamento: {self.departamento}')
        print(f'Salario por hora: {self.salario_hora}')
        print(f'Horas trabajadas: {self.horas}')
    
    def incrementar_horas(self, horas_extra):
        self.horas += horas_extra

class Trabajador(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, empresa, cargo, salario):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.empresa = empresa
        self.cargo = cargo
        self.salario = salario
    
    def aumentar_salario(self, incremento):
        self.salario += incremento
    
    def mostrar_info_trabajador(self):
        print(f'Empresa: {self.empresa}')
        print(f'Cargo: {self.cargo}')
        print(f'Salario: {self.salario}')

class Conductor(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, empresa, tipo_vehiculo, salario_viaje):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.empresa = empresa
        self.tipo_vehiculo = tipo_vehiculo
        self.salario_viaje = salario_viaje
    
    def tiempo_conduccion(self, distancia):
        return distancia / self.velocidad
    
    def calcular_salario(self, distancia):
        return self.salario_viaje * self.tiempo_conduccion(distancia)
    
    def mostrar_info_conductor(self):
        print(f'Empresa: {self.empresa}')
        print(f'Tipo de vehiculo: {self.tipo_vehiculo}')
        print(f'Salario por viaje: {self.salario_viaje}')

class Turista(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, pais_origen, dias_estadia):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.pais_origen = pais_origen
        self.dias_estadia = dias_estadia
    
    def mostrar_info_turista(self):
        print(f'País de origen: {self.pais_origen}')
        print(f'Días de estadía: {self.dias_estadia}')
    
    def aumentar_estadia(self, dias_extra):
        self.dias_estadia += dias_extra

# Lista de instancias
lista_usuarios = []

# Guardar datos generales de un usuario
def guardar_datos(usuario):
    with open('usuarios.txt', 'a') as archivo:
        for usuario in lista_usuarios:
            archivo.write(f'''
                            Nombre: {usuario.nombre}
                            Telefono: {usuario.telefono}
                            Saldo: {usuario.saldo}
                            Tipo: {usuario.tipo}
                            Dirección: {usuario.direccion}\n\n
                            ''')

# ----------------------------------- Menus -----------------------------------------
def menu_principal():
    print("-- Menu de opciones --")
    print("1. Agregar usuario")
    print("2. Interactuar con usuario")
    print("3. Guardar datos")
    print("4. Salir")

def menu_clases():
    print("Ingrese el tipo de usuario:")
    print("1. Estudiante")
    print("2. Profesor")
    print("3. Trabajador")
    print("4. Conductor")
    print("5. Turista")

def menu_general(usuario):
    print("-- Usuario --")
    print("1. Mostrar información de usuario")
    print("2. Agregar saldo")
    print("3. Verificar saldo")
    print("4. Descontar saldo")
    print("-- Transporte --")
    print("5. Calcular tiempo")
    print("6. Calcular costo")
    print("7. Verificar capacidad")
    print("8. Actualizar costo")
    print("9. Salir")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        usuario.mostrar_informacion()
    elif op == 2:
        cantidad = float(input("Ingrese la cantidad a agregar: "))
        usuario.agregar_saldo(cantidad)
        print("Saldo agregado con éxito.")
    elif op == 3:
        print(f'Saldo: {usuario.verificar_saldo()}')
    elif op == 4:
        cantidad = float(input("Ingrese la cantidad a descontar: "))
        usuario.descontar_saldo(cantidad)
        print("Saldo descontado con éxito.")
    elif op == 5:
        distancia = usuario.distancia
        print(f'Tiempo: {usuario.calcular_tiempo(distancia)}')
    elif op == 6:
        distancia = usuario.distancia
        print(f'Costo: {usuario.calcular_costo(distancia)}')
    elif op == 7:
        num_personas = int(input("Ingrese el número de personas: "))
        if usuario.verificar_capacidad(num_personas):
            print("Capacidad suficiente.")
        else:
            print("Capacidad insuficiente.")
    elif op == 8:
        nuevo_costo = float(input("Ingrese el nuevo costo: "))
        usuario.actualizar_costo(nuevo_costo)
        print("Costo actualizado con éxito.")
    elif op == 9:
        pass
    else:
        print("Opción no válida.")

def menu_profesor(usuario):
    print("-- Profesor opciones --")
    print("1. Mostrar información de profesor")
    print("2. Calcular salario")
    print("3. Incrementar horas")
    print("4. Salir")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        usuario.mostrar_info_profesor()
    elif op == 2:
        print(f'Salario: {usuario.calcular_salario()}')
    elif op == 3:
        horas_extra = int(input("Ingrese las horas extra: "))
        usuario.incrementar_horas(horas_extra)
        print("Horas incrementadas con éxito.")
    elif op == 4:
        pass

def menu_trabajador(usuario):
    print("-- Trabajador opciones --")
    print("1. Mostrar información de trabajador")
    print("2. Aumentar salario")
    print("3. Salir")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        usuario.mostrar_info_trabajador()
    elif op == 2:
        incremento = float(input("Ingrese el incremento: "))
        usuario.aumentar_salario(incremento)
        print("Salario aumentado con éxito.")
    elif op == 3:
        pass    

def menu_conductor(usuario):
    print("-- Conductor opciones --")
    print("1. Mostrar información de conductor")
    print("2. Calcular salario")
    print("3. Tiempo de conducción")
    print("4. Salir")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        usuario.mostrar_info_conductor()
    elif op == 2:
        distancia = usuario.distancia
        print(f'Salario: {usuario.calcular_salario(distancia)}')
    elif op == 3:
        distancia = usuario.distancia
        print(f'Tiempo de conducción: {usuario.tiempo_conduccion(distancia)}')
    elif op == 4:
        pass

def menu_turista(usuario):
    print("-- Turista opciones --")
    print("1. Mostrar información de turista")
    print("2. Aumentar estadía")
    print("3. Salir")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        usuario.mostrar_info_turista()
    elif op == 2:
        dias_extra = int(input("Ingrese los días extra: "))
        usuario.aumentar_estadia(dias_extra)
        print("Estadía aumentada con éxito.")
    elif op == 3:
        pass

# ------------------------------------------ Crear instancias ---------------------------------------------
# Funcion para agregar datos de un usuario segun el tipo y crear una instancia
def tipo_usuario(opcion, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo):
    if opcion == 1:
        print("-- Datos de estudiante --")
        universidad = input("Universidad: ")
        carrera = input("Carrera: ")
        semestre = int(input("Semestre: "))
        usuario = Estudiante(nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, universidad, carrera, semestre)
        lista_usuarios.append(usuario)
    elif opcion == 2:
        print("-- Datos de profesor --")
        universidad = input("Universidad: ")
        departamento = input("Departamento: ")
        salario_hora = float(input("Salario por hora: "))
        horas = int(input("Horas trabajadas: "))
        usuario = Profesor(nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, universidad, departamento, salario_hora, horas)
        lista_usuarios.append(usuario)
    elif opcion == 3:
        print("-- Datos de trabajador --")
        empresa = input("Empresa: ")
        cargo = input("Cargo: ")
        salario = float(input("Salario: "))
        usuario = Trabajador(nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, empresa, cargo, salario)
        lista_usuarios.append(usuario)
    elif opcion == 4:
        print("-- Datos de conductor --")
        empresa = input("Empresa: ")
        tipo_vehiculo = input("Tipo de vehiculo: ")
        salario_viaje = float(input("Salario por viaje: "))
        usuario = Conductor(nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, empresa, tipo_vehiculo, salario_viaje)
        lista_usuarios.append(usuario)
    elif opcion == 5:
        print("-- Datos de turista --")
        pais_origen = input("País de origen: ")
        dias_estadia = int(input("Días de estadía: "))
        usuario = Turista(nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, pais_origen, dias_estadia)
        lista_usuarios.append(usuario)

# Funcion para agregar datos generales de un usuario
def agregar_usuario():
    print("-- Datos usuario --")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo: ")
    telefono = input("Telefono: ")
    direccion = input("Direccion: ")
    saldo = float(input("Saldo: "))
    distancia = float(input("Distancia (que tan lejos está de su destino en Km): "))
    print("-- Datos de transporte --")
    tipo = input("Tipo: ")
    costo = float(input("Costo(si el transporte es propio ponga 0): "))
    velocidad = float(input("Velocidad (Km/h): "))
    color = input("Color: ")
    capacidad = int(input("Capacidad: "))
    menu_clases()
    opcion = int(input("Ingrese una opción: "))
    tipo_usuario(opcion, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo)
    print("Usuario agregado con éxito.")

# ------------------------------------- Main -----------------------------------------
# Funcion principal que nos permite interactuar con el programa
def main():
    while True:
        menu_principal()
        opcion = int(input("Ingrese una opción: "))
        print("\n")
        if opcion == 1:
            agregar_usuario()
            print("\n")
        elif opcion == 2:   
            nombre = input("Ingrese el nombre del usuario: ")
            print("-- Desea saber informacion general o especifica --")
            print("1. Informacion general")
            print("2. Informacion especifica")
            op = int(input("Ingrese una opción: "))
            print("\n")
            for usuario in lista_usuarios:
                if usuario.nombre == nombre:    
                    if op == 1:         
                        menu_general(usuario)
                    elif op == 2:
                        if isinstance(usuario, Estudiante):
                            print("-- Información de estudiante --")
                            usuario.mostrar_info_universidad()
                        elif isinstance(usuario, Profesor):
                            menu_profesor(usuario)
                        elif isinstance(usuario, Trabajador):
                            menu_trabajador(usuario)
                        elif isinstance(usuario, Conductor):
                            menu_conductor(usuario)
                        elif isinstance(usuario, Turista):
                            menu_turista(usuario)
            print("\n")
        elif opcion == 3:
            guardar_datos(lista_usuarios)
            print("Datos guardados con éxito.\n")
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

main()