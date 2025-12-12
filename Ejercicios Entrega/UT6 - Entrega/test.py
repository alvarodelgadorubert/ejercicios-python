import modulo_alvaro

print("--- Condicionales ---")

print("Mayor (10, 5):", modulo_alvaro.mayor(10, 5))
print("Mayor (10, 20):", modulo_alvaro.mayor(10, 20))

print("Es Par (4):", modulo_alvaro.es_par(4))
print("Es Par (7):", modulo_alvaro.es_par(7))

print("Es Mayúsculas ('HOLA'):", modulo_alvaro.es_mayusculas("HOLA"))
print("Es Mayúsculas ('Hola'):", modulo_alvaro.es_mayusculas("Hola"))

print("Día Escrito (3):", modulo_alvaro.dia_escrito(3))
print("Día Escrito (7):", modulo_alvaro.dia_escrito(7))
print("Día Escrito (8):", modulo_alvaro.dia_escrito(8))

print("Días del Mes (2, 4, 1):")
print(modulo_alvaro.num_dias_mes(2))
print(modulo_alvaro.num_dias_mes(4))
print(modulo_alvaro.num_dias_mes(1))

print("Coste Llamada (Tipo 1, 10 min):", modulo_alvaro.calcula_coste_llamada(1, 10))
print("Coste Llamada (Tipo 3, 20 min):", modulo_alvaro.calcula_coste_llamada(3, 20))

print("Coste Transporte (550g, Zona 1):", modulo_alvaro.calcula_coste_transporte(550, 1))
print("Coste Transporte (1000g, Zona 4):", modulo_alvaro.calcula_coste_transporte(1000, 4))


print("\n--- Bucles ---")

print("Factorial de 5:", modulo_alvaro.factorial(5))

print("Pares entre 5 y 15 (Imprime):")
modulo_alvaro.pares_entre(5, 15)

print("Tabla de multiplicar del 7 (Imprime):")
modulo_alvaro.tabla_multiplicar(7)

print("7 es primo:", modulo_alvaro.es_primo(7))
print("10 es primo:", modulo_alvaro.es_primo(10))

print("Adivina Número (Interactivo - 3 intentos):")
modulo_alvaro.adivina_numero(3)

print("\nPrimeros 5 números primos (Imprime):")
modulo_alvaro.primeros_primos(5)