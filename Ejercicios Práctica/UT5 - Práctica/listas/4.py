numeros: list[int] = []

while len(numeros) < 10:
    num = int(input("Introduce un número entero (negativo para parar): "))
    if num < 0:
        break
    numeros.append(num)

print(f"Lista final: {numeros}")