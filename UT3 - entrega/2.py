from datetime import datetime

f = datetime.now()

if f.hour < 12:
    print("Backup de mañana")
elif f.hour < 20:
    print("Backup de tarde")
else:
    print("Backup nocturno")