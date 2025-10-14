import random
import string

nombre = '  Ana  '
apellido = '  López '

# Limpiar espacios, convertir a minúsculas
nombre_limpio = nombre.strip().lower()
apellido_limpio = apellido.strip().lower()

# Eliminar acentos del apellido
apellido_sin_acentos = apellido_limpio.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

# Extraer las 3 primeras letras de cada parte
parte_nombre = nombre_limpio[:3]
parte_apellido = apellido_sin_acentos[:3]

# Generar dos dígitos aleatorios
dos_digitos = "".join(random.choices(string.digits, k=2))

# Unir todo para formar el nombre de usuario
usuario_generado = parte_nombre + parte_apellido + dos_digitos

# Imprimir el resultado
print(f"Nombre de usuario generado: {usuario_generado}")