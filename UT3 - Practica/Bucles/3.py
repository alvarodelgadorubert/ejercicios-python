cantidad_str = input()
try:
    cantidad = int(cantidad_str)
except ValueError:
    cantidad = 0

mayores_cero = 0
menores_cero = 0
iguales_cero = 0
contador = 0

while contador < cantidad:
    try:
        numero = int(input())
    except ValueError:
        continue

    if numero > 0:
        mayores_cero += 1
    elif numero < 0:
        menores_cero += 1
    else:
        iguales_cero += 1
    
    contador += 1

print(mayores_cero)
print(menores_cero)
print(iguales_cero)