numerosEnteros = 0

while True:
    numeros = input("Ingrese números enteros (Escriba 'salir' si quiere terminar): ")
    if numeros.lower() == "salir":
        break
    try:
        numero = int(numeros)
        numerosEnteros += numero
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero o 'salir'.")

print(f"La suma de todos los números enteros es: {numerosEnteros}")
