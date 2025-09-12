nivel_terrremoto = float(input("ingrese la magnitud del terrremoto: "))
if nivel_terrremoto<3:
    print("Muy leve")
elif nivel_terrremoto<4:
    print("Leve")
elif nivel_terrremoto<5:
    print("Moderado")
elif nivel_terrremoto<6:
    print("Fuerte")
elif nivel_terrremoto<7:
    print("Muy Fuerte")
elif nivel_terrremoto>=7:
    print("Extremo")