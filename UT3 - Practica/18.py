try:
    # 1. Pedir el número de día
    dia_num = int(input("Introduce un número del día (1 al 7): "))

    # 2. Imprimir el día correspondiente
    if dia_num == 1:
        print("Lunes")
    elif dia_num == 2:
        print("Martes")
    elif dia_num == 3:
        print("Miércoles")
    elif dia_num == 4:
        print("Jueves")
    elif dia_num == 5:
        print("Viernes")
    elif dia_num == 6:
        print("Sábado")
    elif dia_num == 7:
        print("Domingo")
    else:
        # 3. Caso de error
        print("Error: El número debe estar entre 1 y 7.")

except ValueError:
    print("Error: Debe introducir un número entero.")