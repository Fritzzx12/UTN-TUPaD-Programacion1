# Ejercicio 1 - "Caja del Kiosco"
nombre = input("Nombre del cliente: ")
while not nombre.isalpha():
    print("Error: solo se permiten letras (no puede estar vacío).")
    nombre = input("Nombre del cliente: ")

cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un número entero mayor a 0.")
    cantidad = input("Cantidad de productos: ")
cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0.0

for i in range(1, cantidad + 1):
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input(f"Producto {i} - Precio: ")
    precio = int(precio)

    descuento = input("Descuento (S/N): ").lower()
    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ").lower()

    total_sin_descuentos += precio
    if descuento == "s":
        total_con_descuentos += precio * 0.90
    else:
        total_con_descuentos += precio

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print()
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# Ejercicio 2 - "Acceso al Campus y Menú Seguro"

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and not acceso:
    intentos += 1
    usuario = input(f"Intento {intentos}/3 - Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada")
else:
    salir = False
    while not salir:
        print()
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
        else:
            opcion = int(opcion)

            if opcion == 1:
                print("Inscripto")
            elif opcion == 2:
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                else:
                    confirmacion = input("Confirmar clave: ")
                    if nueva_clave == confirmacion:
                        clave_correcta = nueva_clave
                        print("Clave cambiada con éxito.")
                    else:
                        print("Error: las claves no coinciden.")
            elif opcion == 3:
                print("¡Cada línea de código que escribís te acerca a ser programador!")
            else:
                print("Sesión finalizada. ¡Hasta luego!")
                salir = True


# Ejercicio 3 - "Agenda de Turnos con Nombres (sin listas)"

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: solo se permiten letras.")
    operador = input("Nombre del operador: ")
print(f"Bienvenido/a, {operador}")

salir = False
while not salir:
    print()
    print("--- MENÚ ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
    elif int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción fuera de rango (1-5).")
    else:
        opcion = int(opcion)

        if opcion == 1:
            dia = input("Día (1=Lunes, 2=Martes): ")
            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                print("Error: ingrese 1 o 2.")
                dia = input("Día (1=Lunes, 2=Martes): ")
            dia = int(dia)

            paciente = input("Nombre del paciente: ")
            while not paciente.isalpha():
                print("Error: solo se permiten letras.")
                paciente = input("Nombre del paciente: ")
            paciente = paciente.capitalize()

            if dia == 1:
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Error: el paciente ya tiene turno el lunes.")
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado: Lunes, Turno 1.")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado: Lunes, Turno 2.")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado: Lunes, Turno 3.")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado: Lunes, Turno 4.")
                else:
                    print("No hay cupos disponibles el lunes.")
            else:
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Error: el paciente ya tiene turno el martes.")
                elif martes1 == "":
                    martes1 = paciente
                    print("Turno reservado: Martes, Turno 1.")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado: Martes, Turno 2.")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado: Martes, Turno 3.")
                else:
                    print("No hay cupos disponibles el martes.")

        elif opcion == 2:
            dia = input("Día (1=Lunes, 2=Martes): ")
            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                print("Error: ingrese 1 o 2.")
                dia = input("Día (1=Lunes, 2=Martes): ")
            dia = int(dia)

            paciente = input("Nombre del paciente: ")
            while not paciente.isalpha():
                print("Error: solo se permiten letras.")
                paciente = input("Nombre del paciente: ")
            paciente = paciente.capitalize()

            if dia == 1:
                if lunes1 == paciente:
                    lunes1 = ""
                    print("Turno cancelado.")
                elif lunes2 == paciente:
                    lunes2 = ""
                    print("Turno cancelado.")
                elif lunes3 == paciente:
                    lunes3 = ""
                    print("Turno cancelado.")
                elif lunes4 == paciente:
                    lunes4 = ""
                    print("Turno cancelado.")
                else:
                    print("No se encontró al paciente el lunes.")
            else:
                if martes1 == paciente:
                    martes1 = ""
                    print("Turno cancelado.")
                elif martes2 == paciente:
                    martes2 = ""
                    print("Turno cancelado.")
                elif martes3 == paciente:
                    martes3 = ""
                    print("Turno cancelado.")
                else:
                    print("No se encontró al paciente el martes.")

        elif opcion == 3:
            dia = input("Día (1=Lunes, 2=Martes): ")
            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                print("Error: ingrese 1 o 2.")
                dia = input("Día (1=Lunes, 2=Martes): ")
            dia = int(dia)

            if dia == 1:
                print("Agenda del Lunes:")
                print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
                print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
                print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
                print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
            else:
                print("Agenda del Martes:")
                print("Turno 1:", martes1 if martes1 != "" else "(libre)")
                print("Turno 2:", martes2 if martes2 != "" else "(libre)")
                print("Turno 3:", martes3 if martes3 != "" else "(libre)")

        elif opcion == 4:
            ocupados_lunes = 0
            if lunes1 != "":
                ocupados_lunes += 1
            if lunes2 != "":
                ocupados_lunes += 1
            if lunes3 != "":
                ocupados_lunes += 1
            if lunes4 != "":
                ocupados_lunes += 1

            ocupados_martes = 0
            if martes1 != "":
                ocupados_martes += 1
            if martes2 != "":
                ocupados_martes += 1
            if martes3 != "":
                ocupados_martes += 1

            disponibles_lunes = 4 - ocupados_lunes
            disponibles_martes = 3 - ocupados_martes

            print("--- RESUMEN GENERAL ---")
            print(f"Lunes: {ocupados_lunes} ocupados, {disponibles_lunes} disponibles")
            print(f"Martes: {ocupados_martes} ocupados, {disponibles_martes} disponibles")

            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos: Martes")
            else:
                print("Empate: ambos días tienen la misma cantidad de turnos.")

        else:
            print(f"Sistema cerrado. ¡Hasta luego, {operador}!")
            salir = True


# Ejercicio 4 - "Escape Room: La Bóveda"

# Nombre del agente (solo letras)
nombre = input("Nombre del agente: ")
while not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0   
bloqueado = False     

print(f"Agente {nombre}, tenés que abrir las 3 cerraduras de la bóveda.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print()
    print("=== ESTADO ===")
    if alarma:
        estado_alarma = "ON"
    else:
        estado_alarma = "OFF"
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {estado_alarma}")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        else:
            print("Error: la opción debe ser 1, 2 o 3.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    if opcion == 1:
        riesgo = energia < 40
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        if forzar_seguidas >= 3:
            alarma = True
            forzar_seguidas = 0
            print("¡La cerradura se trabó! Se activó la alarma y no se abrió nada.")
        else:
            if riesgo:
                print("¡Energía baja! Hay riesgo de alarma.")
                numero = input("Elegí un número del 1 al 3: ")
                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    print("Error: ingrese un número entre 1 y 3.")
                    numero = input("Elegí un número del 1 al 3: ")
                if int(numero) == 3:
                    alarma = True
                    print("¡Mala suerte! Se activó la alarma.")

            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")
            else:
                print("La alarma impide abrir la cerradura.")

    elif opcion == 2:
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Hackeando... paso {paso}/4 - Código: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""   # se reinicia el código para el próximo desbloqueo
            print("¡Código completo! Se abrió una cerradura automáticamente.")

    else:
        forzar_seguidas = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("La alarma te desgasta: -10 de energía extra.")
        print("Descansaste un rato.")

    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

print()
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! {nombre} abrió la bóveda.")
elif bloqueado:
    print("DERROTA (bloqueo): la alarma bloqueó el sistema.")
else:
    print("DERROTA: te quedaste sin energía o sin tiempo.")


# Ejercicio 5 - "La Arena del Gladiador"

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador:
        print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")
        valido = False
        while not valido:
            if not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                opcion = input("Opción: ")
            elif int(opcion) < 1 or int(opcion) > 3:
                print("Error: La opción debe ser 1, 2 o 3.")
                opcion = input("Opción: ")
            else:
                valido = True
        opcion = int(opcion)

        if opcion == 1:
            if vida_enemigo < 20:
                danio = danio_pesado * 1.5
                print(">> ¡GOLPE CRÍTICO!")
            else:
                danio = float(danio_pesado)
            vida_enemigo = vida_enemigo - danio
            print(f">> ¡Atacaste al enemigo por {danio} puntos de daño!")

        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for golpe in range(3):
                vida_enemigo = vida_enemigo - 5
                print(" > Golpe conectado por 5 de daño")

        else:
            if pociones > 0:
                vida_jugador = vida_jugador + 30
                pociones = pociones - 1
                print(">> ¡Te curaste 30 puntos de vida!")
            else:
                print(">> ¡No quedan pociones!")

        if vida_enemigo < 0:
            vida_enemigo = 0
        turno_gladiador = False

    else:
        vida_jugador = vida_jugador - danio_enemigo
        print(f">> ¡El enemigo te atacó por {danio_enemigo} puntos de daño!")
        if vida_jugador < 0:
            vida_jugador = 0
        turno_gladiador = True
        if vida_jugador > 0:
            print("=== NUEVO TURNO ===")

print()
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
