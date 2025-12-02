etiqueta = 'PC-AULA-23'

# Verificar si la cadena empieza con 'PC-'
comienza_con_pc = etiqueta.startswith('PC-')
print(f"¿Empieza por 'PC-'?: {comienza_con_pc}")

# Encontrar las posiciones de los guiones para trocear
primer_guion = etiqueta.find('-')
segundo_guion = etiqueta.find('-', primer_guion + 1)

# Extraer las partes usando troceado (slicing)
aula = etiqueta[primer_guion + 1 : segundo_guion]
numero = etiqueta[segundo_guion + 1 :]

# Imprimir las partes obtenidas
print(f"Parte del aula: {aula}")
print(f"Parte del número: {numero}")