try:
    # 1. Pedir los datos
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes: "))
    ano = int(input("Introduce el año: "))

    fecha_correcta = True
    dias_del_mes = 0

    # 2. Comprobar año y mes
    if ano <= 0:
        fecha_correcta = False
    elif mes < 1 or mes > 12:
        fecha_correcta = False
    
    # 3. Si año y mes son válidos, comprobar día
    else:
        # Calcular días del mes
        if mes == 2: # Febrero
            # Comprobar si es bisiesto
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                dias_del_mes = 29
            else:
                dias_del_mes = 28
        
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11: # Meses con 30 días
            dias_del_mes = 30
            
        else: # Meses con 31 días
            dias_del_mes = 31
            
        # Comprobar el día
        if dia < 1 or dia > dias_del_mes:
            fecha_correcta = False

    # 4. Mostrar resultado final
    if fecha_correcta:
        print(f"La fecha {dia}/{mes}/{ano} es CORRECTA.")
    else:
        print(f"La fecha {dia}/{mes}/{ano} es INCORRECTA.")

except ValueError:
    print("Error: Día, mes y año deben ser números enteros.")