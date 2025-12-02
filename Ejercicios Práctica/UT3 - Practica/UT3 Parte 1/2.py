# Pedimos al usuario que introduzca un número
numero = float(input("Introduce un número: "))

# Comprobamos si es positivo, negativo o cero
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")