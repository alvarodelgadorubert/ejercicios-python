ip_base = input("Introduce la IP base (ej: '192.168.1.'): ")

while True:
    try:
        inicio_octeto = int(input("Introduce el inicio del último octeto: "))
        fin_octeto = int(input("Introduce el fin del último octeto: "))
        
        if 0 <= inicio_octeto <= 255 and 0 <= fin_octeto <= 255 and inicio_octeto <= fin_octeto:
            break
        else:
            print("Rango inválido. El rango debe ser 0-255 y estar ordenado.")
    except ValueError:
        print("Entrada no válida. Introduce números enteros.")

print("\n--- IPs con Último Octeto Par ---")

for octeto in range(inicio_octeto, fin_octeto + 1):
    if octeto % 2 == 0:
        print(f"{ip_base}{octeto}")