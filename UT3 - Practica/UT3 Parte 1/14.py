try:
    # 1. Pedir datos
    precio_inicial = float(input("Introduce el precio inicial por kg: "))
    kilos = float(input("Introduce los kilos a vender: "))
    tipo = input("Introduce el tipo de uva (A o B): ")
    tamano = int(input("Introduce el tamaño (1 o 2): "))

    # 2. Ajustar precio según tipo y tamaño
    precio_final_kg = precio_inicial

    if tipo.upper() == 'A':
        if tamano == 1:
            precio_final_kg = precio_final_kg + 0.20
        elif tamano == 2:
            precio_final_kg = precio_final_kg + 0.30
        
    elif tipo.upper() == 'B':
        if tamano == 1:
            precio_final_kg = precio_final_kg - 0.30
        elif tamano == 2:
            precio_final_kg = precio_final_kg - 0.50
    
    # 3. Calcular ganancia final
    ganancia_total = precio_final_kg * kilos

    print(f"El precio final por kg es: {precio_final_kg:.2f} euros.")
    print(f"La ganancia total por el embarque es: {ganancia_total:.2f} euros.")

except ValueError:
    print("Error: Precio, kilos y tamaño deben ser números.")