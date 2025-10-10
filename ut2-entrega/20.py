# Ejercicio 20
caracter = input("Escribe un carácter: ")
valor_unicode = ord(caracter)

print(f"El valor Unicode de '{caracter}' es: {valor_unicode}")

numero = int(input("Escribe un número entre 32 y 126: "))
if 32 <= numero <= 126:
    caracter_ascii = chr(numero)
    print(f"El carácter ASCII de {numero} es: '{caracter_ascii}'")
else:
    print("El número debe estar entre 32 y 126")