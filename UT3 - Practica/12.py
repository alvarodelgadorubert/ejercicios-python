try:
    # 1. Leer el año
    ano = int(input("Introduce un año: "))

    es_bisiesto = False

    # 2. Aplicar la regla
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        es_bisiesto = True

    # 3. Mostrar resultado
    if es_bisiesto:
        print(f"El año {ano} ES bisiesto.")
    else:
        print(f"El año {ano} NO es bisiesto.")

except ValueError:
    print("Error: El año debe ser un número entero.")