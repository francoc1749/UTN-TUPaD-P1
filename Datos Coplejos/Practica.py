# -------------------------------------------------------------------
# UTN - Tecnicatura Universitaria en Programación
# Práctico 6: Estructuras de datos complejas
# -------------------------------------------------------------------

# --- Ejercicio 1 ---
# Añadir frutas al diccionario 
print("--- Ejercicio 1 ---")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Diccionario original: {precios_frutas}")

# Añadimos las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"Diccionario con nuevas frutas: {precios_frutas}\n")


# --- Ejercicio 2 ---
# Actualizar precios del diccionario resultante 
print("--- Ejercicio 2 ---")
# Usamos el diccionario modificado del ejercicio anterior
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Una forma alternativa y compacta de actualizar múltiples valores es con update()
# precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})

print(f"Diccionario con precios actualizados: {precios_frutas}\n")


# --- Ejercicio 3 ---
# Crear una lista solo con las frutas (claves) 
print("--- Ejercicio 3 ---")
# Usamos el diccionario modificado del ejercicio anterior
# El método .keys() devuelve las claves
# La función list() convierte ese resultado en una lista
lista_frutas = list(precios_frutas.keys())

print(f"Lista de frutas: {lista_frutas}\n")


# --- Ejercicio 4 ---
# Almacenar y consultar números telefónicos 
print("--- Ejercicio 4 ---")
contactos = {}
print("Por favor, ingrese 5 contactos:")

# Bucle para cargar 5 contactos
for i in range(5):
    # Pedimos nombre (clave) y número (valor)
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero
    print(f"Contacto '{nombre}' agregado.")

print(f"\nAgenda de contactos creada: {contactos}")

# Pedir un nombre y mostrar el número
nombre_consulta = input("\nIngrese un nombre para buscar su número: ")

# Usamos el método .get() para consultar
# .get(clave, valor_por_defecto)
# Esto evita un error si el nombre (clave) no existe
numero_encontrado = contactos.get(nombre_consulta, "Contacto no encontrado.")
print(f"Resultado de la búsqueda: {numero_encontrado}\n")


# --- Ejercicio 5 ---
# Palabras únicas y recuento de palabras de una frase [cite: 33, 34, 35]
print("--- Ejercicio 5 ---")
frase_usuario = input("Ingrese una frase: ")

# .split() divide la frase en una lista de palabras
palabras = frase_usuario.lower().split() # .lower() para no diferenciar mayúsculas

# 1. Palabras únicas (usando un set)
# Un set, por definición, no permite elementos duplicados
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

# 2. Diccionario con la cantidad de veces que aparece cada palabra
recuento_palabras = {}
for palabra in palabras:
    if palabra in recuento_palabras:
        # Si la palabra ya está en el diccionario, sumamos 1
        recuento_palabras[palabra] += 1
    else:
        # Si es la primera vez que aparece, la añadimos con valor 1
        recuento_palabras[palabra] = 1

print(f"Recuento de palabras: {recuento_palabras}\n")


# --- Ejercicio 6 ---
# Promedio de notas de alumnos (guardadas en tuplas) [cite: 41, 42]
print("--- Ejercicio 6 ---")
alumnos_notas = {}
print("Ingrese los datos de 3 alumnos:")

for _ in range(3):
    nombre_alumno = input("Nombre del alumno: ")
    try:
        # Pedimos las 3 notas
        nota1 = float(input(f"Ingrese nota 1 de {nombre_alumno}: "))
        nota2 = float(input(f"Ingrese nota 2 de {nombre_alumno}: "))
        nota3 = float(input(f"Ingrese nota 3 de {nombre_alumno}: "))
        
        # Guardamos las notas como una TUPLA en el diccionario
        alumnos_notas[nombre_alumno] = (nota1, nota2, nota3)
        print(f"Notas de {nombre_alumno} guardadas.")
    except ValueError:
        print("Error: Ingrese solo números para las notas. Alumno no agregado.")

print("\n--- Promedio de cada alumno ---")
# Iteramos sobre el diccionario (alumno = clave, notas_tupla = valor)
for alumno, notas_tupla in alumnos_notas.items():
    # sum() suma todos los elementos de la tupla
    # len() nos da la cantidad de elementos (3)
    promedio = sum(notas_tupla) / len(notas_tupla)
    # :.2f formatea el número para mostrar solo 2 decimales
    print(f"Promedio de {alumno}: {promedio:.2f}")

print("") # Salto de línea


# --- Ejercicio 7 ---
# Operaciones con sets de estudiantes [cite: 50, 51, 52, 53]
print("--- Ejercicio 7 ---")
# Sets de ejemplo
parcial_1_aprobados = {"Juan", "Ana", "Luis", "Sofía", "Pedro", "Maria"}
parcial_2_aprobados = {"Ana", "Luis", "Carmen", "Diego", "Sofía", "Juan"}

print(f"Aprobaron Parcial 1: {parcial_1_aprobados}")
print(f"Aprobaron Parcial 2: {parcial_2_aprobados}")

# 1. Mostrar los que aprobaron ambos parciales (Intersección)
ambos_parciales = parcial_1_aprobados.intersection(parcial_2_aprobados)
# Alternativa: ambos_parciales = parcial_1_aprobados & parcial_2_aprobados
print(f"\nAprobaron ambos parciales: {ambos_parciales}")

# 2. Mostrar los que aprobaron solo uno de los dos (Diferencia simétrica)
solo_un_parcial = parcial_1_aprobados.symmetric_difference(parcial_2_aprobados)
# Alternativa: solo_un_parcial = parcial_1_aprobados ^ parcial_2_aprobados
print(f"Aprobaron solo uno de los dos parciales: {solo_un_parcial}")

# 3. Mostrar la lista total de estudiantes (Unión)
total_aprobados = parcial_1_aprobados.union(parcial_2_aprobados)
# Alternativa: total_aprobados = parcial_1_aprobados | parcial_2_aprobados
print(f"Total de estudiantes que aprobaron al menos un parcial: {total_aprobados}\n")


# --- Ejercicio 8 ---
# Gestión de stock de productos [cite: 54, 55, 56, 57]
print("--- Ejercicio 8 ---")
stock_productos = {"Manzana": 100, "Banana": 150, "Naranja": 80, "Pera": 120}

# Usamos un bucle while True para que el menú se repita
# hasta que el usuario elija la opción de salir
while True:
    print("\n--- Gestión de Stock ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock (producto existente)")
    print("3. Agregar un nuevo producto y su stock")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        # Consultar stock 
        producto = input("Ingrese el nombre del producto a consultar: ")
        # Usamos .get() para una consulta segura
        stock_actual = stock_productos.get(producto, f"Error: El producto '{producto}' no existe.")
        print(f"Respuesta: {stock_actual}")
            
    elif opcion == '2':
        # Agregar unidades (si existe) 
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            try:
                cantidad_str = input(f"Ingrese cantidad a AGREGAR a {producto}: ")
                cantidad = int(cantidad_str)
                stock_productos[producto] += cantidad
                print(f"¡Stock actualizado! {producto} ahora tiene {stock_productos[producto]} unidades.")
            except ValueError:
                print("Error: Debe ingresar un número.")
        else:
            print(f"Error: El producto '{producto}' no existe. Use la opción 3 para agregarlo.")
            
    elif opcion == '3':
        # Agregar nuevo producto (si no existe) 
        producto = input("Ingrese el nombre del NUEVO producto: ")
        if producto not in stock_productos:
            try:
                cantidad_str = input(f"Ingrese el stock inicial para {producto}: ")
                cantidad = int(cantidad_str)
                stock_productos[producto] = cantidad
                print(f"¡Producto '{producto}' agregado con {cantidad} unidades!")
            except ValueError:
                print("Error: Debe ingresar un número.")
        else:
            print(f"Error: El producto '{producto}' ya existe. Use la opción 2 para actualizar su stock.")
            
    elif opcion == '4':
        # Salir del bucle
        print("Saliendo del programa de stock.\n")
        break
        
    else:
        print("Opción no válida. Por favor, intente de nuevo.")


# --- Ejercicio 9 ---
# Agenda con claves de tupla (día, hora) [cite: 58, 70]
print("--- Ejercicio 9 ---")
# Ejemplo de agenda con claves (dia, hora) [cite: 64, 65, 66]
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Turno con el dentista",
    ("viernes", "18:00"): "Gimnasio"
}

print(f"Agenda actual: {agenda}")
print("\nConsultar agenda:")
# Pedimos los datos al usuario
dia = input("Ingrese el día a consultar (ej: lunes): ").lower()
hora = input("Ingrese la hora a consultar (ej: 10:00): ")

# Creamos la tupla que servirá como clave
clave_consulta = (dia, hora)

# Consultamos usando .get() para manejar el caso de que no haya evento
evento = agenda.get(clave_consulta, "No hay eventos programados en esa fecha y hora.")
print(f"Evento encontrado: {evento}\n")


# --- Ejercicio 10 ---
# Invertir un diccionario de países y capitales [cite: 71, 72, 73]
print("--- Ejercicio 10 ---")
# Diccionario original [cite: 75]
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Perú": "Lima",
    "Colombia": "Bogotá"
}

print(f"Diccionario original: {paises_capitales}")

# Creamos el diccionario invertido vacío
capitales_paises = {}

# Iteramos sobre los pares (clave, valor) del diccionario original
# (pais será la clave, capital será el valor)
for pais, capital in paises_capitales.items():
    # Invertimos los roles:
    # La capital (valor original) es la nueva clave
    # El pais (clave original) es el nuevo valor
    capitales_paises[capital] = pais
    
print(f"Diccionario invertido: {capitales_paises}\n")

print("--- Fin del Práctico 6 ---")# -------------------------------------------------------------------
