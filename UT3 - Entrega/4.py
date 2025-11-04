import sys

if len(sys.argv) < 2:
    sys.exit()

hostname = sys.argv[1]
longitud = len(hostname)
empieza_por_pc = hostname.startswith("PC-")

es_valido = empieza_por_pc and longitud >= 7

if es_valido:
    print("VÁLIDO")
else:
    print("NO VÁLIDO")