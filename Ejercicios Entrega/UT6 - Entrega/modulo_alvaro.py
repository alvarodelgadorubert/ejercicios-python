# Ejercicio 1
def calcular_porcentaje(cantidad, total):
    if total == 0:
        return 0
    return (cantidad * 100) / total

# Ejercicio 2
def pasar_a_bytes(tamano, unidad):
    if unidad == "K":
        return tamano * 1024
    elif unidad == "M":
        return tamano * 1024 * 1024
    elif unidad == "G":
        return tamano * 1024 * 1024 * 1024
    else:
        return tamano
    
# Ejercicio 3
def formato_bytes(bytes):
    if bytes < 1024:
        return str(bytes) + "B"
    elif bytes < 1024 * 1024:
        return str(round(bytes / 1024, 2)) + "K"
    elif bytes < 1024 * 1024 * 1024:
        return str(round(bytes / (1024 * 1024), 2)) + "M"
    else:
        return str(round(bytes / (1024 * 1024 * 1024), 2)) + "G"

# Ejercicio 4
from datetime import datetime

def formato_backup(fecha):
    return "backup_" + fecha.strftime("%Y_%m_%d") + ".zip"

ahora = datetime.now()
nombre_backup = formato_backup(ahora)

# Ejercicio 5
from pathlib import Path

def es_directorio(ruta):
    p = Path(ruta)
    return p.is_dir()

# Ejercicio 6
import platform

def detectar_so():
    so = platform.system()
    if so == "Windows":
        return "winget"
    elif so == "Linux":
        return "apt"
    elif so == "Darwin":
        return "brew"
    else:
        return "Gestor no definido"
    
# Ejercicio 7
def es_hora_laboral(hora):
    return hora >= 9 and hora < 18