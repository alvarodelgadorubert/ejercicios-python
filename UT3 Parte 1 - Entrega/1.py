import sys
import shutil

if len(sys.argv) < 2:
    sys.exit()

try:
    umbral_porcentaje = int(sys.argv[1])
except ValueError:
    sys.exit()

try:
    uso_disco = shutil.disk_usage('/')
except FileNotFoundError:
    uso_disco = shutil.disk_usage('.') 

porcentaje_usado = (uso_disco.used / uso_disco.total) * 100

if porcentaje_usado >= umbral_porcentaje:
    print("ALERTA")
else:
    print("OK")