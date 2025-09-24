numero=int(input("Ingrese el numero que desea saber los digitos:"))
cantidad_digitos=0
n=abs(numero)
while n>0:
    n //= 10
    cantidad_digitos+=1
print(f"La cantidad de digitos es de {cantidad_digitos}")