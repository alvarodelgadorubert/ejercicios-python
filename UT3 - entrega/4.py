import sys

# Comprobamos si se ha pasado un argumento (el hostname)
if len(sys.argv) < 2:
    print("Debes indicar un hostname como argumento.")
    sys.exit()

# Guardamos el argumento en una variable
hostname = sys.argv[1]

# Comprobamos las condiciones del ejercicio
if hostname.startswith("PC-") and len(hostname) >= 7:
    print("VÁLIDO")
else:
    print("NO VÁLIDO")