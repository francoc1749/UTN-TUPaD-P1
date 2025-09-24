numero=int(input("Ingrese un numero:"))
numero_inicial=0
suma=0
contador=0
while numero_inicial<=numero:
    suma+=numero_inicial
    numero_inicial+=1
print(f"La suma de numeros es de {suma}")