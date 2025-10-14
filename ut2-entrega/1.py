# Texto original
hostname_original = '   pc -- aula -  07  \n'

# Proceso de normalización
# 1. strip() -> Elimina espacios y saltos de línea en los bordes.
# 2. replace() -> Reemplaza los separadores por un guion.
# 3. upper() -> Convierte todo a mayúsculas.
hostname_normalizado = hostname_original.strip().replace(' -- ', '-').replace(' -  ', '-').upper()

# Impresión del resultado
print(hostname_normalizado)