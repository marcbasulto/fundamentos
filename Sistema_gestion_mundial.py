def registrar_jugador(lista_jugadores):
    print("\n--- Registrar Nuevo Jugador ---")
    nombre = input("Nombre del jugador: ")
    pais = input("País: ")
    
    # Validaciones básicas de entrada
    while True:
        try:
            numero = int(input("Número de camiseta: "))
            goles = int(input("Cantidad de goles: "))
            edad = int(input("Edad: "))
            estatura = float(input("Estatura (ej. 1.85): "))
            break
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")
            
    grupo = input("Grupo (A-H): ").upper()

    # Creación del diccionario del jugador
    jugador = {
        "nombre": nombre,
        "pais": pais,
        "numero": numero,
        "goles": goles,
        "edad": edad,
        "estatura": estatura,
        "grupo": grupo
    }
    
    lista_jugadores.append(jugador)
    print(f"¡Jugador {nombre} registrado con éxito!")


def mostrar_jugadores(lista_jugadores):
    print("\n--- Lista de Jugadores Registrados ---")
    if not lista_jugadores:
        print("No hay jugadores registrados aún.")
        return

    for i, jugador in enumerate(lista_jugadores, 1):
        print(f"{i}. {jugador['nombre']} ({jugador['pais']}) - Camiseta #{jugador['numero']}")
        print(f"   Goles: {jugador['goles']} | Edad: {jugador['edad']} | Estatura: {jugador['estatura']}m | Grupo: {jugador['grupo']}")
        print("-" * 40)


def registrar_fase2(diccionario_fase2):
    print("\n--- Registrar Emparejamiento Fase II ---")
    pais1 = input("Ingrese el nombre del primer país: ").strip()
    pais2 = input("Ingrese el nombre de su rival directo: ").strip()
    
    if pais1 == "" or pais2 == "":
        print("Error: Los nombres de los países no pueden estar vacíos.")
        return

    # Registrar el emparejamiento de manera bidireccional o directa
    diccionario_fase2[pais1] = pais2
    print(f"¡Emparejamiento registrado!: {pais1} vs {pais2}")


def mostrar_fase2(diccionario_fase2):
    print("\n--- Emparejamientos de la Fase II ---")
    if not diccionario_fase2:
        print("No se han registrado emparejamientos para la Fase II.")
        return

    for pais, rival in diccionario_fase2.items():
        print(f"⚽ {pais}  VS  {rival}")


def menu():
    # Inicialización de las estructuras de datos solicitadas
    lista_jugadores = []  # Lista de diccionarios
    diccionario_fase2 = {}  # Diccionario clave: valor

    while True:
        print("\n====================================")
        print("    SISTEMA DE GESTIÓN DEL MUNDIAL  ")
        print("====================================")
        print("1. Registrar un jugador")
        print("2. Mostrar lista de jugadores")
        print("3. Registrar emparejamiento Fase II")
        print("4. Mostrar emparejamientos Fase II")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            registrar_jugador(lista_jugadores)
        elif opcion == "2":
            mostrar_jugadores(lista_jugadores)
        elif opcion == "3":
            registrar_fase2(diccionario_fase2)
        elif opcion == "4":
            mostrar_fase2(diccionario_fase2)
        elif opcion == "5":
            print("Saliendo del sistema... ¡Buen viaje mundialista!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    menu()