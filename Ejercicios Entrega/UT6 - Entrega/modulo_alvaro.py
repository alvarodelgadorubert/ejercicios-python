import math

# --- EJERCICIOS DE CONDICIONALES ---

def mayor(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

def es_par(n):
    return n % 2 == 0

def es_mayusculas(cad):
    return cad.isupper()

def potencia(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        resultado = 1
        for _ in range(exp):
            resultado *= base
        return resultado
    else: # exp < 0
        resultado = 1
        for _ in range(abs(exp)):
            resultado *= base
        return 1 / resultado

def ordena_mayor_menor(n1, n2, n3):
    lista = sorted([n1, n2, n3], reverse=True)
    return tuple(lista)

def clasifica_circunferencias(x1, y1, r1, x2, y2, r2):
    distancia_centros = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    suma_radios = r1 + r2
    resta_radios = abs(r1 - r2)

    if distancia_centros > suma_radios:
        print("Las circunferencias son exteriores.")
    elif distancia_centros == suma_radios:
        print("Las circunferencias son tangentes exteriores.")
    elif distancia_centros > resta_radios and distancia_centros < suma_radios:
        print("Las circunferencias son secantes.")
    elif distancia_centros == resta_radios and distancia_centros != 0:
        print("Las circunferencias son tangentes interiores.")
    elif distancia_centros < resta_radios and distancia_centros != 0:
        print("Las circunferencias son interiores.")
    elif distancia_centros == 0 and r1 != r2:
        print("Las circunferencias son concéntricas.")
    elif distancia_centros == 0 and r1 == r2:
        print("Las circunferencias son la misma circunferencia (coincidentes).")

def clasifica_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("El triángulo es Equilátero.")
        elif a == b or a == c or b == c:
            print("El triángulo es Isósceles.")
        else:
            print("El triángulo es Escaleno.")
    else:
        print("Esas longitudes no forman un triángulo.")

def es_bisiesto(anyo):
    return (anyo % 400 == 0) or (anyo % 4 == 0 and anyo % 100 != 0)

def es_fecha_correcta(dia, mes, anyo):
    if not 1 <= mes <= 12 or not 1 <= dia <= 31:
        return False

    dias_en_mes = num_dias_mes(mes, anyo) # Reutilizamos la lógica de días
    return dia <= dias_en_mes

def calcula_ganancias_uva(precio_kilo, kilos, tipo, tamanyo):
    incremento = 0.0

    if tipo.upper() == 'A':
        if tamanyo == 1:
            incremento = 0.20
        elif tamanyo == 2:
            incremento = 0.30
    elif tipo.upper() == 'B':
        if tamanyo == 1:
            incremento = -0.30
        elif tamanyo == 2:
            incremento = -0.50

    precio_final = precio_kilo + incremento
    ganancias = precio_final * kilos
    return ganancias

def costes_viaje(n):
    coste_total_bus = 0
    if n >= 100:
        coste_total_bus = 2000
    elif n >= 50:
        coste_total_bus = 4000
    elif n >= 30:
        coste_total_bus = 95
        coste_total_bus *= n
    else: # n < 30
        coste_total_bus = 4000 / n
        coste_total_bus *= 30

    coste_alumno = coste_total_bus / n
    return (coste_alumno, coste_total_bus)

def coste_llamada(tiempo, es_domingo, turno):
    coste = 0.0

    # Primeros 3 minutos
    if tiempo <= 3:
        coste += 3.00
        minutos_extra = 0
    else:
        coste += 3.00
        minutos_extra = tiempo - 3

    # Minutos extra
    if minutos_extra > 0:
        if tiempo <= 5:
            coste += minutos_extra * 0.50
        elif tiempo <= 8:
            coste += minutos_extra * 0.40
        elif tiempo <= 10:
            coste += minutos_extra * 0.30
        else: # tiempo > 10
            coste += minutos_extra * 0.20

    # Turno
    if turno.upper() == 'M':
        coste *= 1.15 # Incremento del 15%
    elif turno.upper() == 'T':
        coste *= 1.10 # Incremento del 10%

    # Domingo
    if es_domingo.upper() == 'S':
        coste *= 1.03 # Incremento del 3%

    return coste

def dia_escrito(n):
    dias = {
        1: "lunes",
        2: "martes",
        3: "miércoles",
        4: "jueves",
        5: "viernes",
        6: "sábado",
        7: "domingo"
    }
    return dias.get(n, "Número de día inválido")

def num_dias_mes(mes, anyo=2024): # anyo por defecto para bisiesto en la fecha correcta
    if mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(anyo) else 28
    else:
        return 31

def calcula_coste_transporte(peso, zona):
    tarifas = {
        1: 1.1,
        2: 2.2,
        3: 4.6,
        4: 5.4,
        5: 7.5
    }

    if zona in tarifas:
        coste_base_por_kg = tarifas[zona]
        peso_kg = peso / 1000
        coste_final = coste_base_por_kg * peso_kg
        return coste_final
    else:
        return "Zona de transporte inválida"

# --- EJERCICIOS DE BUCLES ---

def factorial(num):
    if num < 0:
        return "El factorial no está definido para números negativos"
    if num == 0:
        return 1
    
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

def pares_entre(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
        
    for n in range(num1, num2 + 1):
        if n % 2 == 0:
            print(n, end=" ")
    print() # Para salto de línea al final

def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def adivina_numero(intentos):
    import random
    numero_secreto = random.randint(1, 100)
    
    for i in range(intentos):
        try:
            intento_usuario = int(input(f"Intento {i + 1} de {intentos}: Adivina el número (1-100): "))
            
            if intento_usuario == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número en {i + 1} intentos.")
                return True
            elif intento_usuario < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            else:
                print("Demasiado alto. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")

    print(f"¡Se acabaron los intentos! El número secreto era {numero_secreto}.")
    return False

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primeros_primos(N):
    if N <= 0:
        return

    primos_encontrados = 0
    num = 2
    
    while primos_encontrados < N:
        if es_primo(num):
            print(num, end=" ")
            primos_encontrados += 1
        num += 1
    print()