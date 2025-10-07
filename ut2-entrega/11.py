nombre_completo = input("Ingresa tu nombre completo: ")

print(nombre_completo.upper())                    # Mayúsculas
print(nombre_completo.lower())                    # Minúsculas
print(nombre_completo.title())                    # Primera letra de cada palabra en mayúscula

# Contar caracteres excluyendo espacios
nombre_sin_espacios = nombre_completo.replace(" ", "")
print(f"El nombre tiene {len(nombre_sin_espacios)} caracteres (sin espacios)")