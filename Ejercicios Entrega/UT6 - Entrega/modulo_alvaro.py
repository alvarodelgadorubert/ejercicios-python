import random

def mayor(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def es_mayusculas(cad):
    return cad.isupper()

def dia_escrito(n):
    if n == 1:
        return "Lunes"
    elif n == 2:
        return "Martes"
    elif n == 3:
        return "Miércoles"
    elif n == 4:
        return "Jueves"
    elif n == 5:
        return "Viernes"
    elif n == 6:
        return "Sábado"
    elif n == 7:
        return "Domingo"
    else:
        return "Día no válido"

def num_dias_mes(mes):
    if mes == 2:
        return 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    else:
        return 0

def calcula_coste_llamada(tipo, minutos):
    coste = 0.0
    if tipo == 1:
        coste = minutos * 0.10
    elif tipo == 2:
        coste = minutos * 0.08
    elif tipo == 3:
        coste = minutos * 0.05
    return coste

def calcula_coste_transporte(peso, zona):
    coste_base = 0.0
    coste_adicional = 0.0
    tramos_peso = peso // 100

    if zona == 1:
        coste_base = 5.00
    elif zona == 2:
        coste_base = 8.00
    elif zona == 3:
        coste_base = 10.00
    elif zona == 4:
        coste_base = 15.00
    elif zona == 5:
        coste_base = 20.00
    else:
        return 0.0

    coste_adicional = tramos_peso * 0.50
    return coste_base + coste_adicional

def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res

def pares_entre(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i)

def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def adivina_numero(intentos):
    secreto = random.randint(1, 100)
    print("Adivina un número entre 1 y 100")
    for i in range(intentos):
        try:
            intento = int(input(f"Intento {i+1} de {intentos}: "))
        except ValueError:
            print("Entrada no válida. Pierdes un intento.")
            continue

        if intento == secreto:
            print("¡Acertaste!")
            return True
        elif intento < secreto:
            print("Demasiado bajo")
        else:
            print("Demasiado alto")

    print(f"Perdiste. El número era {secreto}")
    return False

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primeros_primos(n):
    primos_encontrados = 0
    candidato = 2
    
    while primos_encontrados < n:
        if es_primo(candidato):
            print(candidato)
            primos_encontrados += 1
        candidato += 1