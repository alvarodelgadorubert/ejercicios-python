try:
    # 1. Pedir los datos
    nota = float(input("Introduce la nota (0-10): "))
    edad = int(input("Introduce la edad: "))
    sexo = input("Introduce el sexo (F o M): ")

    # 2. Comprobar las condiciones
    # Comprobamos la condición principal (nota y edad)
    if nota >= 5 and edad >= 18:
        
        # Si se cumple, miramos el sexo
        if sexo.upper() == 'F':
            print("ACEPTADA")
        elif sexo.upper() == 'M':
            print("POSIBLE")
        else:
            print("NO ACEPTADA (Sexo no válido)")
            
    # Si no se cumple la condición principal
    else:
        print("NO ACEPTADA")

except ValueError:
    print("Error: La nota y la edad deben ser números.")