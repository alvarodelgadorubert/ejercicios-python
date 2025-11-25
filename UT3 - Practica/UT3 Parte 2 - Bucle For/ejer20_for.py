def es_primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

N = int(input("¿Cuántos primos quieres mostrar?: "))

contador = 0
num = 2

while contador < N:
    if es_primo(num):
        print(num)
        contador += 1
    num += 1