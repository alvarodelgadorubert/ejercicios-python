# Ejercicio 3
contador_hostnames = 0
hostname = ""

while hostname.upper() != "FIN":
    hostname = input("Introduce un hostname (o 'FIN' para terminar): ")
    
    if hostname.upper() != "FIN":
        contador_hostnames += 1
        
print(f"\nTotal de hostnames introducidos: {contador_hostnames}")