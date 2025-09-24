import random
numero_random= random.randint(0,9)
numero=int(input("Ingrese un numero en el rango de 0 a 9 para ver si adivina el numero "))
contador=0
while True:
    if numero_random==numero:
        print(f"Encontraste el numero, en {contador+1} intentos")
        break
    else:
        contador+=1
        numero=int(input("Fallaste intentalo de nuevo "))