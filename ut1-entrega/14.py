numero = int(input("Ingresa un número de dos cifras: "))
if 10 <= numero <= 99:
    decenas = numero // 10
    unidades = numero % 10
    invertido = unidades * 10 + decenas
    print(f"El número invertido es: {invertido}")
else:
    print("El número debe tener exactamente dos cifras")