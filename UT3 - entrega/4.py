import sys

if len(sys.argv) < 2:
    print("Debes indicar un hostname como argumento.")
    sys.exit()

hostname = sys.argv[1]

if hostname.startswith("PC-") and len(hostname) >= 7:
    print("VÁLIDO")
else:
    print("NO VÁLIDO")