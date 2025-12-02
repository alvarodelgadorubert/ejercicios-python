try:
    # 1. Pedir datos
    duracion = int(input("Duración de la llamada (minutos enteros): "))
    dia = input("Día de la semana (ej: Domingo, Lunes...): ")
    turno = input("Turno (Mañana o Tarde): ")

    # 2. Calcular costo base (por duración)
    costo_base = 0.0
    
    if duracion <= 5:
        costo_base = duracion * 1.00
    elif duracion <= 8: # Entre 6 y 8 minutos
        costo_base = (5 * 1.00) + ((duracion - 5) * 0.80)
    elif duracion <= 10: # Entre 9 y 10 minutos
        costo_base = (5 * 1.00) + (3 * 0.80) + ((duracion - 8) * 0.70)
    else: # Más de 10 minutos
        costo_base = (5 * 1.00) + (3 * 0.80) + (2 * 0.70) + ((duracion - 10) * 0.50)

    # 3. Calcular impuesto
    impuesto_porc = 0.0
    
    # usamos .lower() para que "domingo" y "Domingo" funcionen
    if dia.lower() == "domingo":
        impuesto_porc = 0.03 # 3%
    else:
        if turno.lower() == "mañana":
            impuesto_porc = 0.15 # 15%
        else: # Asumimos "tarde"
            impuesto_porc = 0.10 # 10%
            
    valor_impuesto = costo_base * impuesto_porc
    costo_total = costo_base + valor_impuesto

    # 4. Mostrar desglose
    print(f"\n--- Resumen de la llamada ---")
    print(f"Costo base por tiempo: {costo_base:.2f} euros.")
    print(f"Impuesto ({impuesto_porc * 100}%): {valor_impuesto:.2f} euros.")
    print(f"TOTAL A PAGAR: {costo_total:.2f} euros.")

except ValueError:
    print("Error: La duración debe ser un número entero.")