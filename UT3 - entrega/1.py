import sys
import shutil

if len(sys.argv) >= 2:
    umbral = int(sys.argv [1])
else:
    umbral = 85

total, usado, libre = shutil.disk_usage("/")
print(total)
print(usado)
print(libre)

porcentaje = int(usado * 100 / total)

print(porcentaje)

print("Uso: ", porcentaje)