palabra: str = input("Introduce una palabra: ")
frecuencia: dict[str, int] = {}

for letra in palabra:
    if letra in frecuencia:
        frecuencia[letra] += 1
    else:
        frecuencia[letra] = 1

print(frecuencia)