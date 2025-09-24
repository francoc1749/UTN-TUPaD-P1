pares=0
inpares=0
i=0
for i in range(0,100,1):
    numero=int(input("Ingrese un numero:"))
    if numero%2==0:
        pares+=1
    elif numero%2==1:
        inpares+=1
print(f"la cantidad de numeros pares es {pares} y de los inpares {inpares}")