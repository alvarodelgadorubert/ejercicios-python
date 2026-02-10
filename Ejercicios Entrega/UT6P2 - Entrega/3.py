try:
    with open("admin_log.txt", "r") as f:
        lineas = f.readlines()
        
    print(f"Total de líneas: {len(lineas)}")
    if lineas:
        print(f"Última línea: {lineas[-1].strip()}")
except FileNotFoundError:
    print("El archivo admin_log.txt no existe.")