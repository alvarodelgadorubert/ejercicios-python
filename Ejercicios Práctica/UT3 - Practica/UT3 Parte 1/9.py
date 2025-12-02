try:
    # 1. Pedir los tres números
    n1 = float(input("Introduce el primer número: "))
    n2 = float(input("Introduce el segundo número: "))
    n3 = float(input("Introduce el tercer número: "))

    # 2. Lógica de condicionales para ordenar
    # Suponemos un orden y lo corregimos
    
    # Declaramos variables para guardar el orden
    mayor = 0.0
    medio = 0.0
    menor = 0.0

    if n1 >= n2 and n1 >= n3:
        mayor = n1
        if n2 >= n3:
            medio = n2
            menor = n3
        else:
            medio = n3
            menor = n2
    elif n2 >= n1 and n2 >= n3:
        mayor = n2
        if n1 >= n3:
            medio = n1
            menor = n3
        else:
            medio = n3
            menor = n1
    else: # n3 es el mayor
        mayor = n3
        if n1 >= n2:
            medio = n1
            menor = n2
        else:
            medio = n2
            menor = n1

    # 3. Mostrar el resultado
    print(f"Ordenados de mayor a menor: {mayor}, {medio}, {menor}")

except ValueError:
    print("Error: Debes introducir tres números.")