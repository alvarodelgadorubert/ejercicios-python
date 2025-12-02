zip_count = 0
targz_count = 0
otros_count = 0

print("Introduce nombres de archivos de backup (o 'FIN' para terminar):")

while True:
    nombre_archivo = input("> ")
    
    if nombre_archivo.upper() == "FIN":
        break
        
    nombre_archivo_lower = nombre_archivo.lower()

    if nombre_archivo_lower.endswith(".zip"):
        zip_count += 1
    elif nombre_archivo_lower.endswith(".tar.gz") or nombre_archivo_lower.endswith(".tgz"):
        targz_count += 1
    else:
        otros_count += 1
        
print("\n--- Resumen de Extensiones ---")
print(f"Archivos terminados en .zip: {zip_count}")
print(f"Archivos terminados en .tar.gz o .tgz: {targz_count}")
print(f"Archivos con otra extensión: {otros_count}")