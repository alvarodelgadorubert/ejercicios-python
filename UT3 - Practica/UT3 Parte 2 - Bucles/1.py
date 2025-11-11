numero = int(input())

if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print(1)
else:
    factorial = 1
    contador = 1
    while contador <= numero:
        factorial *= contador
        contador += 1
    print(factorial)