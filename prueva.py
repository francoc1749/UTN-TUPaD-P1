import csv # Usamos el módulo CSV para manejar los datos estructurados

ruta_completa = "C:/Users/54261/Documents/GitHub/UTN-TUPaD-P1/Trabajo con escritura de archivos/alumnos.csv"

# ----------------------------------------------------------------------
# FUNCIONES PRINCIPALES
# ----------------------------------------------------------------------

def cargar_alumnos(ruta):
    """Carga los alumnos desde el archivo CSV y los devuelve como una lista de diccionarios."""
    alumnos_lista = []
    try:
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo:
            # Usa csv.reader para leer el archivo. skipinitialspace=True ignora espacios
            lector = csv.DictReader(archivo)
            for fila in lector:
                alumnos_lista.append(fila)
    except FileNotFoundError:
        print(f"\n[ERROR] El archivo no se encontró en: {ruta}")
    return alumnos_lista

def agregar_alumno_a_archivo(ruta, nombre, apellido, legajo, nota):
    """Agrega un nuevo alumno al archivo CSV."""
    # El modo 'a' es para APPEND (agregar).
    # newline='' es crucial para evitar líneas en blanco entre filas en CSV
    try:
        with open(ruta, mode='a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            # Escribimos una nueva fila de datos
            escritor.writerow([nombre, apellido, legajo, nota])
        print(f"\n[ÉXITO] Alumno {nombre} {apellido} agregado.")
    except Exception as e:
        print(f"\n[ERROR] No se pudo escribir en el archivo: {e}")

# ----------------------------------------------------------------------
# BUCLE PRINCIPAL
# ----------------------------------------------------------------------

while True:
    print("\n--- MENÚ DE GESTIÓN DE ALUMNOS ---")
    print("1. Ver alumnos (Nombres y Apellidos)")
    print("2. Agregar alumno")
    print("3. Generar y mostrar reporte (No implementado)")
    print("4. Salir")
    
    # 💥 CORRECCIÓN CRÍTICA: Se usa solo input(), no print(input())
    opcion = input("Ingrese una opción (1-4): ") 
    
    if opcion == "1":
        # 1. Ver alumnos
        alumnos = cargar_alumnos(ruta_completa)
        if alumnos:
            print("\n--- LISTA DE ALUMNOS ---")
            # 💡 RESPUESTA a tu pregunta: Iteramos sobre la lista para mostrar cada nombre
            for alumno in alumnos:
                # Usamos .get() por seguridad
                nombre = alumno.get('Nombre', 'N/A')
                apellido = alumno.get('Apellido', 'N/A')
                print(f"- {nombre} {apellido} (Legajo: {alumno.get('Legajo', 'N/A')})")
        else:
            print("\nNo hay alumnos cargados o el archivo está vacío.")

    elif opcion == "2":
        # 2. Agregar alumno
        print("\n--- AGREGAR NUEVO ALUMNO ---")
        # 💥 CORRECCIÓN CRÍTICA: Se usa solo input()
        Nombre_Agregado = input("Ingrese el nombre del alumno: ")
        Apellido_Agregado = input("Ingrese el apellido del alumno: ")
        Legajo_Agregado = input("Ingrese el legajo del alumno: ")
        NotaPromedio_Agregado = input("Ingrese la nota de Promedio del alumno: ")
        
        # Llamamos a la función con la ruta y los datos
        agregar_alumno_a_archivo(ruta_completa, Nombre_Agregado, Apellido_Agregado, Legajo_Agregado, NotaPromedio_Agregado)
        
    elif opcion == "3":
        # 3. Generar y mostrar reporte
        print("\nOpción 'Generar y mostrar reporte' aún no implementada.")
        
    elif opcion == "4":
        # 4. Salir
        print("\n¡Hasta luego!")
        break
        
    else:
        print("\nOpción no válida. Por favor, ingrese un número del 1 al 4.")