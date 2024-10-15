# --------------------------------------------------- Clases primarias ------------------------------------------
class Transporte:
    def __init__(self, capacidad, costo, velocidad, color, tipo):
        self.__capacidad = capacidad
        self.__costo = costo
        self.__velocidad = velocidad
        self.__color = color
        self.__tipo = tipo
    
    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad
    
    def get_capacidad(self):
        return self.__capacidad
    
    def set_costo(self, costo):
        self.__costo = costo
    
    def get_costo(self):
        return self.__costo
    
    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad
        
    def get_velocidad(self):
        return self.__velocidad
    
    def set_color(self, color):
        self.__color = color
        
    def get_color(self):
        return self.__color
    
    def set_tipo(self, tipo):
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
    
    def calcular_tiempo(self, distancia):
        velocidad = self.get_velocidad()
        return distancia / velocidad
    
    def calcular_costo(self, distancia):
        costo = self.get_costo()
        return distancia * costo
    
    def calcular_costo_ida_vuelta(self, distancia):
        return 2 * self.calcular_costo(distancia)
    
    def verificar_capacidad(self, num_personas):
        capacidad = self.get_capacidad()
        return num_personas <= capacidad
    
    def actualizar_costo(self, nuevo_costo):
        self.set_costo(nuevo_costo)

class Persona:
    def __init__(self, nombre, edad, sexo, telefono, direccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__telefono = telefono
        self.__direccion = direccion        
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, edad):
        self.__edad = edad
        
    def get_edad(self):
        return self.__edad

    def set_sexo(self, sexo):
        self.__sexo = sexo
        
    def get_sexo(self):
        return self.__sexo
    
    def set_telefono(self, telefono):
        self.__telefono = telefono
        
    def get_telefono(self):
        return self.__telefono
    
    def set_direccion(self, direccion):
        self.__direccion = direccion
        
    def get_direccion(self):
        return self.__direccion
    
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.get_nombre()}')
        print(f'Edad: {self.get_edad()}')
        print(f'Sexo: {self.get_sexo()}')
        print(f'Telefono: {self.get_telefono()}')
        print(f'Direccion: {self.get_direccion()}')

class Usuario(Persona):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia):
        super().__init__(nombre, edad, sexo, telefono, direccion)
        self.__saldo = saldo
        self.__distancia = distancia
        
    def set_saldo(self, saldo):
        self.__saldo = saldo
        
    def get_saldo(self):
        return self.__saldo
    
    def set_distancia(self, distancia):
        self.__distancia = distancia

    def get_distancia(self):
        return self.__distancia
        
    def agregar_saldo(self, cantidad):
        saldo = self.get_saldo()
        saldo += cantidad
        self.set_saldo(saldo)

    def verificar_saldo(self):
        return self.get_saldo() 
    
    def descontar_saldo(self, cantidad):
        saldo = self.get_saldo()
        if saldo >= cantidad:
            saldo -= cantidad
            self.set_saldo(saldo)
            return self.get_saldo()
        else:
            print('Saldo insuficiente')

# --------------------------------------------------- Clases secundarias ------------------------------------------
class Estudiante(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, universidad, carrera, semestre):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.__universidad = universidad  
        self.__carrera = carrera
        self.__semestre = semestre
    
    def set_universidad(self, universidad):
        self.__universidad = universidad
        
    def get_universidad(self):
        return self.__universidad
    
    def set_carrera(self, carrera):
        self.__carrera = carrera
        
    def get_carrera(self):
        return self.__carrera
    
    def set_semestre(self, semestre):
        self.__semestre = semestre
        
    def get_semestre(self):
        return self.__semestre
    
    def mostrar_info_universidad(self):
        print(f'Universidad: {self.get_universidad()}')
        print(f'Carrera: {self.get_carrera()}')
        print(f'Semestre: {self.get_semestre()}')

class Profesor(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, universidad, departamento, salario_hora, horas):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.__universidad = universidad
        self.__departamento = departamento
        self.__salario_hora = salario_hora
        self.__horas = horas
    
    def set_universidad(self, universidad):
        self.__universidad = universidad
        
    def get_universidad(self):
        return self.__universidad
    
    def set_departamento(self, departamento):
        self.__departamento = departamento
        
    def get_departamento(self):
        return self.__departamento
    
    def set_salario_hora(self, salario_hora):
        self.__salario_hora = salario_hora
        
    def get_salario_hora(self):
        return self.__salario_hora
    
    def set_horas(self, horas):
        self.__horas = horas
        
    def get_horas(self):
        return self.__horas
    
    def calcular_salario(self):
        return self.get_salario_horas * self.get_horas()
    
    def mostrar_info_profesor(self):
        print(f'Universidad: {self.get_universidad()}')
        print(f'Departamento: {self.get_departamento()}')
        print(f'Salario por hora: {self.get_salario_hora()}')
        print(f'Horas trabajadas: {self.get_horas()}')
    
    def incrementar_horas(self, horas_extra):
        horas = self.get_horas()
        horas += horas_extra
        self.set_horas(horas)

class Trabajador(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, empresa, cargo, salario):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.__empresa = empresa
        self.__cargo = cargo
        self.__salario = salario
    
    def set_empresa(self, empresa):
        self.__empresa = empresa
        
    def get_empresa(self):
        return self.__empresa
    
    def set_cargo(self, cargo):
        self.__cargo = cargo
        
    def get_cargo(self):
        return self.__cargo
    
    def set_salario(self, salario):
        self.__salario = salario
        
    def get_salario(self):
        return self.__salario
    
    def aumentar_salario(self, incremento):
        salario = self.get_salario()
        salario += incremento
        self.set_salario(salario)
    
    def mostrar_info_trabajador(self):
        print(f'Empresa: {self.get_empresa()}')
        print(f'Cargo: {self.get_cargo()}')
        print(f'Salario: {self.get_salario()}')

class Conductor(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, empresa, tipo_vehiculo, salario_viaje):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.__empresa = empresa
        self.__tipo_vehiculo = tipo_vehiculo
        self.__salario_viaje = salario_viaje
    
    def set_empresa(self, empresa):
        self.__empresa = empresa

    def get_empresa(self):
        return self.__empresa
    
    def set_tipo_vehiculo(self, tipo_vehiculo):
        self.__tipo_vehiculo = tipo_vehiculo
        
    def get_tipo_vehiculo(self):
        return self.__tipo_vehiculo
    
    def set_salario_viaje(self, salario_viaje):
        self.__salario_viaje = salario_viaje
        
    def get_salario_viaje(self):
        return self.__salario_viaje
    
    def tiempo_conduccion(self, distancia):
        return distancia / self.get_velocidad()
    
    def calcular_salario(self, distancia):
        return self.get_salario_viaje * self.tiempo_conduccion(distancia)
    
    def mostrar_info_conductor(self):
        print(f'Empresa: {self.get_empresa()}')
        print(f'Tipo de vehiculo: {self.get_tipo_vehiculo()}')
        print(f'Salario por viaje: {self.get_salario_viaje()}')

class Turista(Usuario, Transporte):
    def __init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia, capacidad, costo, velocidad, color, tipo, pais_origen, dias_estadia):
        Usuario.__init__(self, nombre, edad, sexo, telefono, direccion, saldo, distancia)
        Transporte.__init__(self, capacidad, costo, velocidad, color, tipo)
        self.__pais_origen = pais_origen
        self.__dias_estadia = dias_estadia
    
    def set_pais_origen(self, pais_origen):
        self.__pais_origen = pais_origen
        
    def get_pais_origen(self):
        return self.__pais_origen
    
    def set_dias_estadia(self, dias_estadia):
        self.__dias_estadia = dias_estadia
        
    def get_dias_estadia(self):
        return self.__dias_estadia
    
    def mostrar_info_turista(self):
        print(f'País de origen: {self.get_pais_origen()}')
        print(f'Días de estadía: {self.get_dias_estadia()}')
    
    def aumentar_estadia(self, dias_extra):
        dias = self.get_dias_estadia()
        dias += dias_extra
        self.set_dias_estadia(dias)