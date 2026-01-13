notas: list[float] = []

for i in range(5):
    while True:
        nota = float(input(f"Introduce la nota {i+1} (0-10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Error: La nota debe estar entre 0 y 10.")

for i in range(len(notas)):
    print(f"Nota {i+1}: {notas[i]}")

print(f"Nota media: {sum(notas) / len(notas)}")
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")