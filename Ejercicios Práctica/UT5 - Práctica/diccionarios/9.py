contador: dict[str, int] = {}

for i in range(5):
    frase = input(f"Introduce la frase {i+1}: ").lower()
    palabras = frase.split()
    for p in palabras:
        contador[p] = contador.get(p, 0) + 1

print(contador)