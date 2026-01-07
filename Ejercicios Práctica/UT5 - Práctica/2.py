numeros = []
for i in range(5):
    num = int(input(f"Introduce el número {i+1}: "))
    numeros.append(num)

print(f"El mayor es: {max(numeros)}")
print(f"El menor es: {min(numeros)}")