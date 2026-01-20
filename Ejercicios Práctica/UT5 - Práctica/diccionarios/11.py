texto: str = input("Introduce un texto: ").lower()
vocales: dict[str, int] = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for caracter in texto:
    if caracter in vocales:
        vocales[caracter] += 1

print(vocales)