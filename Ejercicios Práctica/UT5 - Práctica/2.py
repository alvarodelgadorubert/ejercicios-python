lista_original: list[str] = []

for i in range(5):
    cadena = input(f"Introduce la cadena {i+1}: ")
    lista_original.append(cadena)

lista_invertida: list[str] = lista_original[::-1]

for elemento in lista_invertida:
    print(elemento)