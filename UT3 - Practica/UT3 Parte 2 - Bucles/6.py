numero_str = input()
try:
    numero = int(numero_str)
except ValueError:
    numero = 0

multiplicador = 1
while multiplicador <= 10:
    resultado = numero * multiplicador
    print(resultado)
    multiplicador += 1