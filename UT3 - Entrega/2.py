from datetime import datetime

ahora = datetime.now()
hora_actual = ahora.hour

if hora_actual < 12:
    print("Backup de mañana")
elif hora_actual < 20:
    print("Backup de tarde")
else:
    print("Backup nocturno")