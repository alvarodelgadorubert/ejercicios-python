import modulo_alvaro

# --- PRUEBAS DE FUNCIONES CONDICIONALES ---
print("--- PRUEBAS DE CONDICIONALES ---")

# Ejercicio 1: mayor(n1, n2)
print(f"Mayor entre 15 y 8: {modulo_alvaro.mayor(15, 8)}")
print(f"Mayor entre 5 y 10: {modulo_alvaro.mayor(5, 10)}")

# Ejercicio 3: es_par(n)
print(f"¿Es 42 par? {modulo_alvaro.es_par(42)}")
print(f"¿Es 33 par? {modulo_alvaro.es_par(33)}")

# Ejercicio 6: es_mayusculas(cad)
print(f"¿'HOLA' en mayúsculas? {modulo_alvaro.es_mayusculas('HOLA')}")
print(f"¿'Hola' en mayúsculas? {modulo_alvaro.es_mayusculas('Hola')}")

# Ejercicio 7: potencia(base, exp)
print(f"Potencia (2, 4): {modulo_alvaro.potencia(2, 4)}")
print(f"Potencia (5, 0): {modulo_alvaro.potencia(5, 0)}")
print(f"Potencia (2, -3): {modulo_alvaro.potencia(2, -3)}")

# Ejercicio 9: ordena_mayor_menor(n1, n2, n3)
print(f"Ordenar (10, 5, 12): {modulo_alvaro.ordena_mayor_menor(10, 5, 12)}")

# Ejercicio 10: clasifica_circunferencias(...) (Imprime)
print("Clasificación de circunferencias (Secantes):")
modulo_alvaro.clasifica_circunferencias(0, 0, 5, 7, 0, 3) # Distancia 7, Suma 8, Resta 2
print("Clasificación de circunferencias (Exteriores):")
modulo_alvaro.clasifica_circunferencias(0, 0, 2, 10, 0, 3) # Distancia 10, Suma 5

# Ejercicio 11: clasifica_triangulo(a, b, c) (Imprime)
print("Clasificación de triángulo (Equilátero):")
modulo_alvaro.clasifica_triangulo(5, 5, 5)

# Ejercicio 12: es_bisiesto(anyo)
print(f"¿Es 2024 bisiesto? {modulo_alvaro.es_bisiesto(2024)}")
print(f"¿Es 1900 bisiesto? {modulo_alvaro.es_bisiesto(1900)}")

# Ejercicio 13: es_fecha_correcta(dia, mes, anyo)
print(f"¿Es 31/01/2024 correcta? {modulo_alvaro.es_fecha_correcta(31, 1, 2024)}")
print(f"¿Es 30/02/2024 correcta? {modulo_alvaro.es_fecha_correcta(30, 2, 2024)}")

# Ejercicio 14: calcula_ganancias_uva(...)
print(f"Ganancias Uva A, T1 (10kg a 5€/kg): {modulo_alvaro.calcula_ganancias_uva(5, 10, 'A', 1):.2f}€")

# Ejercicio 15: costes_viaje(n)
coste_alumno, coste_total = modulo_alvaro.costes_viaje(60)
print(f"Costes Viaje (60 alumnos): Coste/Alumno={coste_alumno:.2f}€, Coste Total={coste_total:.2f}€")

# Ejercicio 16: coste_llamada(...)
print(f"Coste Llamada (12min, Domingo, Tarde): {modulo_alvaro.coste_llamada(12, 'S', 'T'):.2f}€")

# Ejercicio 18: dia_escrito(n)
print(f"Día 4: {modulo_alvaro.dia_escrito(4)}")

# Ejercicio 19: num_dias_mes(mes)
print(f"Días de febrero (2024): {modulo_alvaro.num_dias_mes(2, 2024)}")

# Ejercicio 20: calcula_coste_transporte(peso, zona)
print(f"Coste Transporte (2500g, Zona 3): {modulo_alvaro.calcula_coste_transporte(2500, 3):.2f}€")

print("\n" + "="*40 + "\n")

# --- PRUEBAS DE FUNCIONES CON BUCLES ---
print("--- PRUEBAS DE BUCLES ---")

# Ejercicio 1: factorial(num)
print(f"Factorial de 5: {modulo_alvaro.factorial(5)}")

# Ejercicio 5: pares_entre(num1, num2) (Imprime)
print("Pares entre 10 y 20:")
modulo_alvaro.pares_entre(10, 20)

# Ejercicio 6: tabla_multiplicar(n) (Imprime)
print("Tabla de multiplicar del 7:")
modulo_alvaro.tabla_multiplicar(7)

# Ejercicio 10: adivina_numero(intentos)
# Este ejercicio es interactivo, se comenta para ejecución automática
# print("Juego Adivina Número (3 intentos):")
# modulo_alvaro.adivina_numero(3)

# Ejercicio 11: es_primo(n)
print(f"¿Es 17 primo? {modulo_alvaro.es_primo(17)}")
print(f"¿Es 15 primo? {modulo_alvaro.es_primo(15)}")

# Ejercicio 20: primeros_primos(N) (Imprime)
print("Los 10 primeros números primos:")
modulo_alvaro.primeros_primos(10)