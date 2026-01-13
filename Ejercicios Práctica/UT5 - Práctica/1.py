import random

lista_numeros: list[int] = [0] * 10

for i in range(len(lista_numeros)):
    lista_numeros[i] = random.randint(1, 10)

for num in lista_numeros:
    print(f"Número: {num}, Cuadrado: {num**2}, Cubo: {num**3}")