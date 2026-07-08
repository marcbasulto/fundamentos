peliculas_db = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}

cartelera_db = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}


def validar_codigo_nuevo(codigo, peliculas):
    codigo_limpio = codigo.strip().upper()
    if codigo_limpio == "" or codigo_limpio in peliculas:
        return False
    return True

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_duracion(duracion_str):
    try:
        val = int(duracion_str)
        return val > 0
    except ValueError:
        return False

def validar_clasificacion(clasificacion):
    return clasificacion.strip().upper() in ['A', 'B', 'C']

def validar_idioma(idioma):
    return idioma.strip() != ""

def validar_es_3d(es_3d_str):
    return es_3d_str.strip().lower() in ['s', 'n']

def validar_precio(precio_str):
    try:
        val = int(precio_str)
        return val > 0
    except ValueError:
        return False

def validar_cupos(cupos_str):
    try:
        val = int(cupos_str)
        return val >= 0
    except ValueError:
        return False


def cupos_genero(genero_buscar, peliculas, cartelera):
    total_cupos = 0
    genero_buscar = genero_buscar.strip().lower()
    
    for cod, datos in peliculas.items():
        genero_peli = datos[1].lower()
        if genero_peli == genero_buscar:
            if cod in cartelera:
                total_cupos += cartelera[cod][1]
                
    print(f"El total de cupos disponibles es: {total_cupos}")

def busqueda_precio(p_min, p_max, peliculas, cartelera):
    resultados = []
    for cod, datos_cartelera in cartelera.items():
        precio = datos_cartelera[0]
        cupos = datos_cartelera[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            if cod in peliculas:
                titulo = peliculas[cod][0]
                resultados.append(f"{titulo}--{cod}")
                
    if len(resultados) > 0:
        resultados.sort()  
        print(f"Las películas encontradas son: {resultados}")
    else:
        print("No hay películas en ese rango de precios.")

def buscar_codigo_existente(codigo, cartelera):
    cod_upper = codigo.strip().upper()
    if cod_upper in cartelera:
        return cod_upper
    return None

def actualizar_precio(codigo, nuevo_precio, cartelera):
    cod_validado = buscar_codigo_existente(codigo, cartelera)
    if cod_validated := buscar_codigo_existente(codigo, cartelera):
        cartelera[cod_validated][0] = nuevo_precio
        return True
    return False

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    cod_upper = codigo.strip().upper()
    if cod_upper in peliculas:
        return False
        
    bool_3d = True if es_3d.strip().lower() == 's' else False
    
    peliculas[cod_upper] = [titulo.strip(), genero.strip().lower(), int(duracion), clasificacion.strip().upper(), idioma.strip(), bool_3d]
    cartelera[cod_upper] = [int(precio), int(cupos)]
    return True

def eliminar_pelicula(codigo, peliculas, cartelera):
    cod_upper = codigo.strip().upper()
    if cod_upper in peliculas:
        del peliculas[cod_upper]
        if cod_upper in cartelera:
            del cartelera[cod_upper]
        return True
    return False

def leer_opcion_menu():  
    print("========== Menu Principal ==========")
    print("1. Cupos por genero.")
    print("2. Busqueda de peliculas de rango de precio.")
    print("3. Actualizar precio de pelicula.")
    print("4. Agregar pelicula.")
    print("5. Eliminar pelicula.")
    print("6. Salir.")
    try:
        opcion = int(input("Ingrese una opción (1-6): "))
        if 1 <= opcion <= 6:
            return opcion
    except ValueError:
            print("Opción inválida. Debe ser un número entre 1 y 6.")
            return None
def menu_principal(peliculas, cartelera):
    while True:
        opcion = leer_opcion_menu()
        if opcion is None:
            continue
        if opcion == 1:
            genero = input("Ingrese el género a buscar: ")
            cupos_genero(genero, peliculas, cartelera)
        elif opcion == 2:
            try:
                p_min = int(input("Ingrese el precio mínimo: "))
                p_max = int(input("Ingrese el precio máximo: "))
                busqueda_precio(p_min, p_max, peliculas, cartelera)
            except ValueError:
                print("Precios inválidos. Deben ser números enteros.")
        elif opcion == 3:
            codigo = input("Ingrese el código de la película a actualizar: ")
            nuevo_precio_str = input("Ingrese el nuevo precio: ")
            if validar_precio(nuevo_precio_str):
                nuevo_precio = int(nuevo_precio_str)
                if actualizar_precio(codigo, nuevo_precio, cartelera):
                    print(f"Precio de la película {codigo} actualizado a {nuevo_precio}.")
                else:
                    print(f"No se encontró la película con código {codigo}.")
            else:
                print("Precio inválido. Debe ser un número entero positivo.")
        elif opcion == 4:
            codigo = input("Ingrese el código de la nueva película: ")
            titulo = input("Ingrese el título de la película: ")
            genero = input("Ingrese el género de la película: ")
            duracion_str = input("Ingrese la duración en minutos: ")
            clasificacion = input("Ingrese la clasificación (A, B, C): ")
            idioma = input("Ingrese el idioma de la película: ")
            es_3d_str = input("¿Es 3D? (s/n): ")
            precio_str = input("Ingrese el precio de la entrada: ")
            cupos_str = input("Ingrese la cantidad de cupos disponibles: ")

            if (validar_codigo_nuevo(codigo, peliculas) and
                validar_titulo(titulo) and
                validar_genero(genero) and
                validar_duracion(duracion_str) and
                validar_clasificacion(clasificacion) and
                validar_idioma(idioma) and
                validar_es_3d(es_3d_str) and
                validar_precio(precio_str) and
                validar_cupos(cupos_str)):
                duracion = int(duracion_str)
                precio = int(precio_str)
                cupos = int(cupos_str)
                if agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d_str, precio, cupos, peliculas, cartelera):
                    print(f"Película {codigo} agregada exitosamente.")
                else:
                    print(f"Error al agregar la película. El código {codigo} ya existe.")
            else:
                print("Error en la validación de los datos ingresados. Por favor, revise los campos.")
        elif opcion == 5:
            codigo = input("Ingrese el código de la película a eliminar: ")
            if eliminar_pelicula(codigo, peliculas, cartelera):
                print(f"Película {codigo} eliminada exitosamente.")
            else:
                print(f"No se encontró la película con código {codigo}.")
        elif opcion == 6:
            print("Programa Finalizado.")
            break
        
if __name__ == "__main__":
    menu_principal(peliculas_db, cartelera_db)