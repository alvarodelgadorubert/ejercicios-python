try:
    # 1. Pedir el número del dado
    cara = int(input("Introduzca número del dado (1-6): "))

    # 2. Comprobar la cara opuesta
    if cara == 1:
        print('En la cara opuesta está el "seis".')
    elif cara == 2:
        print('En la cara opuesta está el "cinco".')
    elif cara == 3:
        print('En la cara opuesta está el "cuatro".')
    elif cara == 4:
        print('En la cara opuesta está el "tres".')
    elif cara == 5:
        print('En la cara opuesta está el "dos".')
    elif cara == 6:
        print('En la cara opuesta está el "uno".')
    else:
        # 3. Caso de error
        print("ERROR: número incorrecto.")

except ValueError:
    print("Error: Debe introducir un número entero.")