nombre_archivo = 'backup_2025_09_03.tar.gz'

# Extraer las partes de la fecha
inicio_fecha = nombre_archivo.find('_') + 1
fin_fecha = nombre_archivo.find('.')
fecha_original = nombre_archivo[inicio_fecha:fin_fecha] # '2025_09_03'

# Extraer año, mes y día
año = fecha_original[:4]
mes = fecha_original[5:7]
dia = fecha_original[8:10]

# Formatear la fecha como se pide
fecha_formateada = f"{dia}-{mes}-{año}"
print(f"Fecha extraída: {fecha_formateada}")

# Cambiar la extensión del archivo original a .zip
nuevo_nombre_archivo = nombre_archivo.replace('.tar.gz', '.zip')
print(f"Nuevo nombre de archivo: {nuevo_nombre_archivo}")