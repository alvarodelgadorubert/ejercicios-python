try:
    # 1. Pedir el número de mes
    mes = int(input("Introduce un número de mes (1-12): "))

    # 2. Meses con 31 días
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print("Este mes tiene 31 días.")
        
    # 3. Meses con 30 días
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print("Este mes tiene 30 días.")
        
    # 4. Febrero
    elif mes == 2:
        print("Este mes tiene 28 o 29 días (si el año es bisiesto).")
        
    # 5. Caso de error
    else:
        print("Error: El número debe estar entre 1 y 12.")

except ValueError:
    print("Error: Debe introducir un número entero.")