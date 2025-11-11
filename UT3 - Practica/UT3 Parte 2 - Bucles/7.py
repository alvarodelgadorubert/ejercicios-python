base_str = input()
try:
    base = float(base_str)
except ValueError:
    base = 0.0

while True:
    exponente_str = input()
    try:
        exponente = int(exponente_str)
        if exponente >= 0:
            break
        else:
            continue
    except ValueError:
        continue

if exponente == 0:
    resultado = 1.0
elif base == 0:
    resultado = 0.0
else:
    resultado = 1.0
    contador = 0
    while contador < exponente:
        resultado *= base
        contador += 1

print(resultado)