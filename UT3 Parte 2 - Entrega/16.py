ip_base = input("Introduce la IP base (ej: '192.168.'): ")

while True:
    try:
        subred_inicio = int(input("Introduce el inicio del rango de subred (tercer octeto): "))
        subred_fin = int(input("Introduce el fin del rango de subred (tercer octeto): "))
        max_host = int(input("Introduce el máximo host (último octeto): "))
        
        if 0 <= subred_inicio <= 255 and subred_inicio <= subred_fin and 0 <= max_host <= 255 and max_host >= 2:
            break
        else:
            print("Rango/Host inválido.")
    except ValueError:
        print("Entrada no válida. Introduce números enteros.")

print("\n--- Plan de Asignación de IPs ---")

for subred in range(subred_inicio, subred_fin + 1):
    ip_subred = f"{ip_base}{subred}"
    
    gateway_ip = f"{ip_subred}.1"
    print(f"\nSubred: {ip_subred}")
    print(f"  -> GATEWAY: {gateway_ip}")
    
    for host in range(2, max_host + 1):
        if host % 5 == 0:
            print(f"  -> Host: {host} (No asignable - Múltiplo de 5)")
            continue
        
        ip_host = f"{ip_subred}.{host}"
        print(f"  -> Host: {ip_host}")