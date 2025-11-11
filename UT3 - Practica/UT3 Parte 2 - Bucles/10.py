import random

# Generar un número aleatorio entre 1 y 100
numero_a_adivinar = random.randint(1, 100)
intentos_maximos = 10
intentos_restantes = intentos_maximos
adivinado = False

while intentos_restantes > 0 and not adivinado:
    try:
        intento = int(input())
    except ValueError:
        print(f"Te quedan {intentos_restantes} intentos.")
        continue

    if intento == numero_a_adivinar:
        intentos_usados = intentos_maximos - intentos_restantes + 1
        print(f"Acertaste en {intentos_usados} intentos.")
        adivinado = True
    elif intento < numero_a_adivinar:
        intentos_restantes -= 1
        if intentos_restantes > 0:
            print(f"El número a adivinar es mayor que {intento}.")
            print(f"Te quedan {intentos_restantes} intentos.")
    else: # intento > numero_a_adivinar
        intentos_restantes -= 1
        if intentos_restantes > 0:
            print(f"El número a adivinar es menor que {intento}.")
            print(f"Te quedan {intentos_restantes} intentos.")

if not adivinado:
    print(f"Se agotaron los intentos. El número era {numero_a_adivinar}.")