suma = 0
with open("numeros.txt", "r") as f:
    for linea in f:
        suma += int(linea.strip())
print(f"Suma total: {suma}")