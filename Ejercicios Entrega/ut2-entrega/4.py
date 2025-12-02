ip = '  192.168.001.010  '

# Limpiar espacios en los bordes
ip_limpia = ip.strip()

# Contar el número de puntos
cantidad_puntos = ip_limpia.count('.')
print(f"La IP contiene {cantidad_puntos} puntos.")

# Extraer el primer octeto (desde el inicio hasta el primer '.')
primer_punto = ip_limpia.find('.')
primer_octeto = ip_limpia[:primer_punto]

# Extraer el último octeto (desde el último '.' hasta el final)
ultimo_punto = ip_limpia.rfind('.') # rfind busca desde la derecha
ultimo_octeto = ip_limpia[ultimo_punto + 1:]

# Imprimir los octetos extraídos
print(f"Primer octeto: {primer_octeto}")
print(f"Último octeto: {ultimo_octeto}")