diccionario: dict[str, str] = {
    'python': 'Lenguaje de programación',
    'algoritmo': 'Conjunto de instrucciones',
    'variable': 'Espacio de memoria para almacenar datos'
}

palabra: str = input("Introduce una palabra: ").lower()

if palabra in diccionario:
    print(f"{palabra}: {diccionario[palabra]}")
else:
    print("La palabra no existe en el diccionario.")