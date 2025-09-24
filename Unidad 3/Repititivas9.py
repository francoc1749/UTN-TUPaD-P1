cantidad_numeros=10
suma=0
contador=0

for i in range(cantidad_numeros):
    numero=int(input("Ingrese numeros enteros:"))
    suma+=numero
print(f"La media de los numeros ingrados es de {suma//cantidad_numeros}")