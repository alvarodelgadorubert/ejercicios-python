# Pedir límites del intervalo y asegurar que inferior < superior
while True:
    try:
        limite_inferior = float(input())
        limite_superior = float(input())
        if limite_inferior <= limite_superior:
            break
    except ValueError:
        continue # Ignora entradas no numéricas

suma_dentro = 0.0
contador_fuera = 0
encontrado_limite = False
numero = -1.0 # Valor inicial para entrar al bucle

while numero != 0:
    try:
        numero = float(input())
    except ValueError:
        continue

    if numero == 0:
        break

    # Intervalo abierto: (limite_inferior, limite_superior)
    if numero > limite_inferior and numero < limite_superior:
        suma_dentro += numero
    else:
        contador_fuera += 1
        
    # Comprobar si es igual a los límites
    if numero == limite_inferior or numero == limite_superior:
        encontrado_limite = True

print(suma_dentro)
print(contador_fuera)
print(encontrado_limite)