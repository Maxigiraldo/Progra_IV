from objetos import estudiante1, estudiante2, estudiante3, profesor1, profesor2, trabajador1, trabajador2, conductor1, conductor2, turista1, turista2
from clases import Estudiante, Profesor, Trabajador, Conductor, Turista
# ----------------------------------- Menus -----------------------------------------
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
        distancia = usuario.get_distancia()
        print(f'Tiempo: {usuario.calcular_tiempo(distancia)}')
    elif op == 6:
        distancia = usuario.get_distancia()
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
        distancia = usuario.get_distancia()
        print(f'Salario: {usuario.calcular_salario(distancia)}')
    elif op == 3:
        distancia = usuario.get_distancia()
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

# ----------------------------------- Usuario -----------------------------------------
def usuario_busqueda():
    print("Usuarios disponibles:")
    print("1. Juan")
    print("2. Ana")
    print("3. Carlos")
    print("4. María")
    print("5. Luis")
    print("6. Sofía")
    print("7. Fernando")
    print("8. Javier")
    print("9. Lucía")
    print("10. Pedro")
    print("11. Elena")
    print("12. Salir")
    usuario = int(input("Ingrese el numero del usuario: "))
    if usuario == 1:
        return estudiante1
    elif usuario == 2:
        return estudiante2
    elif usuario == 3:
        return estudiante3
    elif usuario == 4:
        return profesor1
    elif usuario == 5:
        return profesor2
    elif usuario == 6:
        return trabajador1
    elif usuario == 7:
        return trabajador2
    elif usuario == 8:
        return conductor1
    elif usuario == 9:
        return conductor2
    elif usuario == 10:
        return turista1
    elif usuario == 11:
        return turista2
    elif usuario == 12:
        return None
    else:
        print("Usuario no válido.")
        return None

# ----------------------------------- Main -----------------------------------------
def main():
    while True:
        usuario = usuario_busqueda()
        if usuario == None:
            print("Saliendo...")
            break
        print("Usuario seleccionado:", usuario.get_nombre())
        print("Qué desea hacer?")
        print("1. Consultar información de usuario general")
        print("2. Consultar información específica")
        print("3. Salir")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            menu_general(usuario)
        elif opcion == 2:
            if isinstance(usuario, Estudiante):
                usuario.mostrar_informacion()
            elif isinstance(usuario, Profesor):
                menu_profesor(usuario)
            elif isinstance(usuario, Trabajador):
                menu_trabajador(usuario)
            elif isinstance(usuario, Conductor):
                menu_conductor(usuario)
            elif isinstance(usuario, Turista):
                menu_turista(usuario)
            else:
                print("Usuario no válido.")
                break
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

main()