import shutil

rutas: list[str] = []
for i in range(3):
    rutas.append(input(f"Introduce ruta del sistema {i+1}: "))

uso_disco: dict[str, dict[str, float]] = {}
for r in rutas:
    total, usado, libre = shutil.disk_usage(r)
    uso_disco[r] = {
        "total_gb": round(total / (2**30), 1),
        "usado_gb": round(usado / (2**30), 1),
        "libre_gb": round(libre / (2**30), 1)
    }

print(uso_disco)