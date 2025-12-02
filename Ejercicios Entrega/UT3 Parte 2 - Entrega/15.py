from pathlib import Path

while True:
    try:
        A = int(input("Introduce el número de aulas (A): "))
        P = int(input("Introduce el número de PCs por aula (P): "))
        if A > 0 and P > 0:
            break
        else:
            print("Los números deben ser positivos.")
    except ValueError:
        print("Entrada no válida. Introduce números enteros.")

total_general_logs = 0

print("\n--- Conteo de Logs por Aula y PC ---")

for a in range(1, A + 1):
    aula_num_str = str(a).zfill(2)
    nombre_aula = f"AULA-{aula_num_str}"
    ruta_aula = Path.cwd() / nombre_aula
    
    total_logs_aula = 0

    if ruta_aula.is_dir():
        print(f"\nAula: {nombre_aula}")
        
        for p in range(1, P + 1):
            pc_num_str = str(p).zfill(2)
            nombre_pc = f"PC-{pc_num_str}"
            ruta_pc = ruta_aula / nombre_pc
            
            logs_pc = 0
            
            if ruta_pc.is_dir():
                for elemento in ruta_pc.iterdir():
                    if elemento.is_file() and str(elemento).endswith(".log"):
                        logs_pc += 1
                        
                print(f"  - {nombre_pc}: {logs_pc} logs")
                total_logs_aula += logs_pc
            else:
                print(f"  - {nombre_pc}: (Carpeta no encontrada)")
        
        print(f"  -> Total de logs en {nombre_aula}: {total_logs_aula}")
        total_general_logs += total_logs_aula
    else:
        print(f"\nAula: {nombre_aula} (Carpeta de aula no encontrada)")

print(f"\n======================================")
print(f"TOTAL GENERAL DE LOGS ENCONTRADOS: {total_general_logs}")