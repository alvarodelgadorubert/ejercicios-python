ruta = 'C:\\Users\\alumno\\Desktop\\proyecto'

# Extraer la unidad (desde el principio hasta los dos puntos)
unidad = ruta[0:ruta.find(':')]

# Encontrar las posiciones de las barras para extraer usuario y carpeta
barra_users = ruta.find('\\') # Primera barra
barra_alumno = ruta.find('\\', barra_users + 1) # Segunda barra
barra_desktop = ruta.find('\\', barra_alumno + 1) # Tercera barra
barra_proyecto = ruta.find('\\', barra_desktop + 1) # Cuarta barra

# Extraer las partes
usuario = ruta[barra_alumno + 1 : barra_desktop]
carpeta = ruta[barra_desktop + 1 : barra_proyecto]

# Imprimir cada valor
print(f"Unidad: {unidad}")
print(f"Usuario: {usuario}")
print(f"Carpeta: {carpeta}")