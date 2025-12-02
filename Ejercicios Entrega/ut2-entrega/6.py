email = 'admin.redes@centro.edu'

# Encontrar las posiciones de '@' y '.'
pos_arroba = email.find('@')
pos_punto = email.find('.', pos_arroba) # Busca el punto después de la arroba

# Extraer las tres partes
usuario = email[:pos_arroba]
dominio = email[pos_arroba + 1 : pos_punto]
tld = email[pos_punto + 1 :]

# Imprimir las partes
print(f"Usuario: {usuario}")
print(f"Dominio: {dominio}")
print(f"TLD: {tld}")