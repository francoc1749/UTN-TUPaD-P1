num1=int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))
suma=0
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
contador=num1+1
while contador<num2:
    suma+=contador
    contador+=1
print(f"La suma de los numeros enteros es {suma}")