import random
import string

# Definir los conjuntos de caracteres
letras = string.ascii_letters
digitos = string.digits
simbolos_especiales = '!#$%&*'

# Seleccionar aleatoriamente la cantidad necesaria de cada tipo
# random.choices() devuelve una lista de k elementos elegidos de la población
cuatro_letras = random.choices(letras, k=4)
cuatro_digitos = random.choices(digitos, k=4)
dos_simbolos = random.choices(simbolos_especiales, k=2)

# Unir todas las listas de caracteres en una sola
lista_caracteres = cuatro_letras + cuatro_digitos + dos_simbolos

# Mezclar los caracteres para que no aparezcan agrupados
random.shuffle(lista_caracteres)

# Convertir la lista de caracteres a una cadena de texto
password = "".join(lista_caracteres)

# Imprimir la contraseña generada
print(f"Contraseña generada: {password}")