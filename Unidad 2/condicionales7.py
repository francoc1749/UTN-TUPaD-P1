palabra= str(input("Ingrese la palabra o la frase "))
ultima_letra= palabra[-1]
if ultima_letra.lower() in "aeiou":
    print(f"{palabra}!")
else:
    print(palabra)