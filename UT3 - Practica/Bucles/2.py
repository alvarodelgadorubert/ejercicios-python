suma = 0
contador = 0
numero = -1

while numero != 0:
    try:
        numero = int(input())
    except ValueError:
        continue # Ignora entradas no numéricas

    if numero != 0:
        suma += numero
        contador += 1

if contador > 0:
    media = suma / contador
    print(suma)
    print(media)
else:
    print(0)
    print(0)