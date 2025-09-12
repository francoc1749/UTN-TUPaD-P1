nombre= str(input("Ingrese su nombre:"))
cambio_nombre= int(input("selecciona una opcion entre 1.2.3: "))
if cambio_nombre == 1:
    print(nombre.upper())
elif cambio_nombre == 2:
    print(nombre.lower())
elif cambio_nombre==3:
    print(nombre.title())
else:
    print("No ingreso un numero entre 1.2.3:")