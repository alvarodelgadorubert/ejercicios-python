from pathlib import Path

while True:
    try:
        ANIO = input("Introduce el año (ej. 2025): ")
        MES_INICIAL = int(input("Introduce el mes inicial (1-12): "))
        MES_FINAL = int(input("Introduce el mes final (1-12): "))
        NUM_DIAS = int(input("Introduce el número de días a crear por mes (ej. 5): "))
        
        if 1 <= MES_INICIAL <= 12 and 1 <= MES_FINAL <= 12 and MES_INICIAL <= MES_FINAL and NUM_DIAS > 0:
            break
        else:
            print("Entrada no válida.")
    except ValueError:
        print("Entrada no válida. Introduce números enteros para meses y días.")

ruta_base = Path.cwd() / "backups"
ruta_base.mkdir(exist_ok=True)

print("\n--- Estructura de Backups Creada ---")

for mes in range(MES_INICIAL, MES_FINAL + 1):
    mes_str = str(mes).zfill(2)
    ruta_mes = ruta_base / ANIO / mes_str
    
    ruta_mes.mkdir(parents=True, exist_ok=True)
    
    for dia in range(1, NUM_DIAS + 1):
        dia_str = str(dia).zfill(2)
        nombre_dia = f"dia_{dia_str}"
        ruta_dia = ruta_mes / nombre_dia
        
        ruta_dia.mkdir(exist_ok=True)
        
        print(ruta_dia)