# Ejercicio 4
from datetime import datetime, timedelta

fecha_actual = datetime.now()

for i in range(7):
    fecha_futura = fecha_actual + timedelta(days=i)
    formato_fecha = fecha_futura.strftime("%Y_%m_%d")
    nombre_backup = f"backup_{formato_fecha}.zip"
    print(nombre_backup)