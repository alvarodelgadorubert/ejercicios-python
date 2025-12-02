try:
    # 1. Pedir base y exponente
    base = float(input("Introduce la base: "))
    exponente = float(input("Introduce el exponente (entero): "))

    resultado = 0

    # 2. Caso 1: Exponente positivo
    if exponente > 0:
        resultado = base ** exponente
        print(f"El resultado es: {resultado}")

    # 3. Caso 2: Exponente es cero
    elif exponente == 0:
        resultado = 1
        print(f"El resultado es: {resultado}")

    # 4. Caso 3: Exponente negativo
    else:
        # exponente negativo es 1 / (base ** exponente positivo)
        resultado = 1 / (base ** -exponente) 
        print(f"El resultado es: {resultado}")

except ValueError:
    print("Error: La base debe ser un número y el exponente un entero.")