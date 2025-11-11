from datetime import datetime

hoy = datetime.now()
dia_semana = hoy.weekday()

if dia_semana == 5 or dia_semana == 6:
    print("Ventana de mantenimiento")
else:
    print("Operación normal")