# -------------------------------------------------------------------
# UTN - Tecnicatura Universitaria en Programación
# Práctica: Manejo de Archivos (Ejercicios 1-6)
# -------------------------------------------------------------------

# Importamos 'os' para verificar si el archivo existe
import os

# Usamos una constante para el nombre del archivo
NOMBRE_ARCHIVO = "productos.txt"

# --- Ejercicio 1: Crear archivo inicial (si no existe) ---
def inicializar_archivo():
    """
    Verifica si 'productos.txt' existe. Si no, lo crea
    con tres productos de ejemplo.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"Creando archivo inicial '{NOMBRE_ARCHIVO}'...")
        try:
            # Usamos 'with open()' en modo 'w' (write) para crear el archivo
            with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as f:
                # Escribimos los 3 productos iniciales
                f.write("Lapicera,120.5,30\n")
                f.write("Cuaderno,350.0,50\n")
                f.write("Goma de borrar,80.75,100\n")
            print("Archivo creado con datos iniciales.")
        except IOError as e:
            print(f"Error grave: No se pudo crear el archivo: {e}")

# --- Ejercicio 4: Cargar productos en una lista de diccionarios ---
def cargar_productos():
    """
    Lee el archivo 'productos.txt' (modo 'r') y carga los datos
    en una lista de diccionarios.
    Devuelve la lista de productos.
    """
    productos = [] # La lista que vamos a llenar
    try:
        # Abrimos el archivo en modo 'r' (read)
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as f:
            for linea in f:
                # Usamos .strip() para quitar saltos de línea (\n) [cite: 19]
                linea = linea.strip()
                if linea: # Nos aseguramos de que la línea no esté vacía
                    # Usamos .split(",") para separar los datos [cite: 19]
                    partes = linea.split(',')
                    
                    if len(partes) == 3:
                        try:
                            # Creamos el diccionario para este producto 
                            producto = {
                                "nombre": partes[0],
                                "precio": float(partes[1]), # Convertimos a número (float)
                                "cantidad": int(partes[2])  # Convertimos a número (int)
                            }
                            # Agregamos el diccionario a la lista
                            productos.append(producto)
                        except ValueError:
                            # Error si precio/cantidad no son números
                            print(f"Error: La línea '{linea}' tiene formato incorrecto y será omitida.")
                    else:
                        print(f"Error: La línea '{linea}' no tiene 3 campos y será omitida.")
                         
    except FileNotFoundError:
        print(f"Advertencia: El archivo '{NOMBRE_ARCHIVO}' no se encontró.")
        # Si no existe, llamamos a la función del Ej. 1 para crearlo
        inicializar_archivo()
        # E intentamos cargar de nuevo (ahora debería tener los datos iniciales)
        return cargar_productos()
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        
    print(f"Se cargaron {len(productos)} productos desde '{NOMBRE_ARCHIVO}'.")
    return productos

# --- Ejercicio 2: Leer y mostrar productos ---
def mostrar_productos(lista_de_productos):
    """
    Recibe la lista de productos (de memoria) y los muestra
    con el formato solicitado[cite: 20].
    """
    if not lista_de_productos:
        print("\nNo hay productos cargados en la lista.")
        return
        
    print("\n--- Listado de Productos en Memoria ---")
    for p in lista_de_productos:
        # Damos el formato "Producto: ... | Precio: ... | Cantidad: ..." [cite: 20]
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    print("---------------------------------------\n")

# --- Ejercicio 3: Agregar productos desde teclado ---
def agregar_producto(lista_de_productos):
    """
    Pide datos de un nuevo producto al usuario  y lo agrega
    a la LISTA de productos (en memoria).
    Devuelve la lista actualizada.
    """
    print("\n--- Agregar Nuevo Producto ---")
    try:
        # Pedimos los datos al usuario
        nombre = input("Ingrese nombre: ").strip()
        precio = float(input("Ingrese precio: "))
        cantidad = int(input("Ingrese cantidad: "))
        
        # Creamos el diccionario para el nuevo producto
        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        
        # Lo añadimos a la lista (que está en memoria)
        lista_de_productos.append(nuevo_producto)
        print(f"\n¡Producto '{nombre}' agregado a la lista!")
        
    except ValueError:
        print("Error: Precio y cantidad deben ser números. Producto no agregado.")
    
    # Devolvemos la lista actualizada
    return lista_de_productos

# --- Ejercicio 5: Buscar producto por nombre ---
def buscar_producto(lista_de_productos):
    """
    Pide un nombre al usuario y busca el producto en la lista[cite: 30].
    Si lo encuentra, muestra sus datos[cite: 31].
    Si no, muestra un mensaje de error.
    """
    print("\n--- Buscar Producto ---")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    
    encontrado = None
    # Recorremos la lista de diccionarios
    for p in lista_de_productos:
        # Buscamos sin diferenciar mayúsculas/minúsculas
        if p['nombre'].lower() == nombre_buscar:
            encontrado = p
            break # Encontramos el producto, dejamos de buscar
    
    if encontrado:
        # Si lo encuentra, mostrar todos sus datos [cite: 31]
        print("\n--- Producto Encontrado ---")
        print(f"  Nombre: {encontrado['nombre']}")
        print(f"  Precio: ${encontrado['precio']}")
        print(f"  Cantidad: {encontrado['cantidad']}")
    else:
        # Si no existe, mostrar un mensaje de error 
        print(f"\nError: Producto '{nombre_buscar}' no encontrado en la lista.")

# --- Ejercicio 6: Guardar los productos actualizados ---
def guardar_productos_en_archivo(lista_de_productos):
    """
    Sobrescribe (modo 'w') el archivo 'productos.txt' con todos los
    productos de la lista actualizada.
    """
    try:
        # Usamos modo 'w' (write) para sobrescribir todo el contenido 
        with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as f:
            for p in lista_de_productos:
                # Convertimos el diccionario de nuevo al formato "nombre,precio,cantidad"
                linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
                f.write(linea)
        
        print(f"Datos guardados exitosamente en '{NOMBRE_ARCHIVO}'.")
    except IOError as e:
        print(f"Error al guardar los datos en el archivo: {e}")

# --- Programa Principal (Menú interactivo) ---
def main():
    """
    Función principal que ejecuta el menú y coordina las demás funciones.
    """
    
    # 1. (Ej 1 y 4)
    # Al iniciar, cargamos los productos.
    # La función 'cargar_productos' ya llama a 'inicializar_archivo' si es necesario.
    productos = cargar_productos()
    
    while True:
        print("\n====== MENÚ DE GESTIÓN DE PRODUCTOS ======")
        print("1. Mostrar todos los productos (Ej. 2)")
        print("2. Agregar un producto (Ej. 3 y 6)")
        print("3. Buscar un producto (Ej. 5)")
        print("4. Salir")
        print("==========================================")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            # Ej. 2: Mostrar
            mostrar_productos(productos)
        
        elif opcion == '2':
            # Ej. 3: Agregar
            productos = agregar_producto(productos)
            # Ej. 6: Guardar los cambios inmediatamente
            guardar_productos_en_archivo(productos)
        
        elif opcion == '3':
            # Ej. 5: Buscar
            buscar_producto(productos)
            
        elif opcion == '4':
            print("\nSaliendo del programa. ¡Adiós!")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# -------------------------------------------------------------------
# Ejecutar el programa principal
# -------------------------------------------------------------------
if __name__ == "__main__":
    main()