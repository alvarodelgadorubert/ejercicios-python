lista1: list[int] = []
lista2: list[int] = []

print("Introduce los valores para la primera lista:")
for i in range(5):
    num = int(input(f"Número {i+1}: "))
    lista1.append(num)

print("\nIntroduce los valores para la segunda lista:")
for i in range(5):
    num = int(input(f"Número {i+1}: "))
    lista2.append(num)

lista_resultado: list[int] = lista1 + lista2

print(f"\nLista unida: {lista_resultado}")