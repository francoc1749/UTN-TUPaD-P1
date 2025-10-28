import csv
ruta_completa="C:/Users/54261/Documents/GitHub/UTN-TUPaD-P1/Trabajo con escritura de archivos/alumnos.csv"

with open(ruta_completa, "r") as archivos:
    # Usamos el método .read() para leer todo el alumnosos del archivo
    alumnos = archivos.read()
archivos.close()

def agregar(ruta,Nombre,Apellido,Legajo,NotaPromedio):
    with open(ruta_completa, "a") as Agregar_a_archivo:
        archivos.write("agregar_alumno\n")
        Agregar_a_archivo.close




while True:
    print("1. Ver alumnos")
    print("2. Agregar alumno")
    print("3. Generar y mostrar archivo de aprobados ")
    print("4. Salir")
    opcion= (input("Ingrese una opción: "))
    if opcion=="1":
        print(alumnos)
    elif opcion=="2":
        Nombre_Agregado=input("Ingrese el nombre del alumno:")
        Apellido_Agregado=input("Ingrese el apellido del alumno:")
        Legajo_Agregado=input("Ingrese el legajo del alumno: ")
        NotaPromedio_Agregado=input("Ingrese la nota de Promedio del alumno:")
        agregar_alumno=agregar(ruta_completa,Nombre_Agregado,Apellido_Agregado,Legajo_Agregado,NotaPromedio_Agregado)
    elif opcion=="3":
        nombre = nombre.get('Nombre', 'N/A')





