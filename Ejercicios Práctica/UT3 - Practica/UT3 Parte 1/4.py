dividendo = float(input("Introduce el dividendo (número 1): "))
divisor = float(input("Introduce el divisor (número 2): "))

if divisor == 0:
    print("Error: ¡No se puede dividir por cero!")
else:
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado}")