try:
    # 1. Pedir datos Circunferencia 1
    x1 = float(input("C1 - Introduce coordena X del centro: "))
    y1 = float(input("C1 - Introduce coordena Y del centro: "))
    r1 = float(input("C1 - Introduce el radio: "))

    # 2. Pedir datos Circunferencia 2
    x2 = float(input("C2 - Introduce coordena X del centro: "))
    y2 = float(input("C2 - Introduce coordena Y del centro: "))
    r2 = float(input("C2 - Introduce el radio: "))

    # 3. Calcular distancia entre centros
    # d = raíz_cuadrada( (x2-x1)^2 + (y2-y1)^2 )
    distancia_centros = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    
    # 4. Calcular suma y diferencia de radios
    suma_radios = r1 + r2
    dif_radios = abs(r1 - r2) # abs() es valor absoluto

    # 5. Clasificar
    # Usamos una pequeña tolerancia (0.00001) para comparar floats
    # en lugar de '=='
    
    if distancia_centros == 0 and r1 == r2:
        print("Son CONCÉNTRICAS.")
    elif distancia_centros > suma_radios:
        print("Son EXTERIORES.")
    elif abs(distancia_centros - suma_radios) < 0.00001:
        print("Son TANGENTES EXTERIORES.")
    elif distancia_centros < suma_radios and distancia_centros > dif_radios:
        print("Son SECANTES.")
    elif abs(distancia_centros - dif_radios) < 0.00001:
        print("Son TANGENTES INTERIORES.")
    elif distancia_centros < dif_radios:
        print("Son INTERIORES (una dentro de la otra).")

except ValueError:
    print("Error: Todos los datos deben ser números.")