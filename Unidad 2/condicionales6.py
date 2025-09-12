import statistics as stats
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = stats.mean(numeros_aleatorios)
mediana = stats.median(numeros_aleatorios)
modas = stats.multimode(numeros_aleatorios)
if len(modas) == 1:
    moda_repr = modas[0]
    hay_moda_unica = True
else:
    moda_repr = min(modas)  
    hay_moda_unica = False
# 4) Diagnóstico de sesgo
# Regla clásica: media > mediana > moda (sesgo +) y media < mediana < moda (sesgo -)
if hay_moda_unica:
    if media > mediana and mediana > moda_repr:
        sesgo = "Sesgo positivo (asimetría a la derecha)"
    elif media < mediana and mediana < moda_repr:
        sesgo = "Sesgo negativo (asimetría a la izquierda)"
    else:
        sesgo = "Sin sesgo claro (posible simetría o patrón no estricto)"
else:
    # Con múltiples modas, la regla estricta se debilita.
    # Usamos una heurística: comparar solo media y mediana.
    if media > mediana:
        sesgo = "Sesgo positivo (basado en media > mediana; múltiples modas)"
    elif media < mediana:
        sesgo = "Sesgo negativo (basado en media < mediana; múltiples modas)"
    else:
        sesgo = "Sin sesgo claro (múltiples modas y media≈mediana)"

# 5) Salida
print(f"Datos: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda(s): {modas}")
print(f"Diagnóstico: {sesgo}")