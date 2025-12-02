try:
    # 1. Pedir número de alumnos
    num_alumnos = float(input("Introduce el número total de alumnos: "))

    costo_por_alumno = 0.0
    pago_total_compania = 0.0

    # 2. Calcular costos
    if num_alumnos <= 0:
        print("No hay viaje si no hay alumnos.")
    
    elif num_alumnos < 30:
        pago_total_compania = 2850
        costo_por_alumno = pago_total_compania / num_alumnos
        
    elif num_alumnos >= 30 and num_alumnos <= 49:
        costo_por_alumno = 95
        pago_total_compania = costo_por_alumno * num_alumnos
        
    elif num_alumnos >= 50 and num_alumnos <= 99:
        costo_por_alumno = 70
        pago_total_compania = costo_por_alumno * num_alumnos
        
    else: # 100 alumnos o más
        costo_por_alumno = 65
        pago_total_compania = costo_por_alumno * num_alumnos

    # 3. Mostrar resultados (si hay viaje)
    if num_alumnos > 0:
        print(f"El pago total a la compañía de viajes es: {pago_total_compania:.2f} euros.")
        print(f"Cada alumno debe pagar: {costo_por_alumno:.2f} euros.")

except ValueError:
    print("Error: El número de alumnos debe ser un entero.")