import random
secreto=random.randint(1,100)
intentos=10
for i in range(1,intentos+1):
    n=int(input(f"Intento {i}: "))
    if n==secreto:
        print("¡Acertaste!")
        break
    print("Mayor" if n<secreto else "Menor")
else:
    print("No acertaste. Era", secreto)