suma = 0.0
count = 0
for _ in range(1000000):
    x = float(input("Introduce un número (0 para terminar): "))
    if x == 0:
        break
    suma += x
    count += 1
if count>0:
    print("Suma =", suma, "Media =", suma/count)
else:
    print("No se introdujeron números distintos de cero.")