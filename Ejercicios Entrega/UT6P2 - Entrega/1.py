import platform
import os
from datetime import datetime

fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
so = platform.system()
cpus = os.cpu_count()

with open("system_report.txt", "w") as f:
    f.write(f"Informe: {fecha_hora}\n")
    f.write(f"Sistema: {so}\n")
    f.write(f"CPUs: {cpus}\n")