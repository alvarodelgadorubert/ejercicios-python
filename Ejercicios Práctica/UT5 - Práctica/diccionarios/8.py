personas: dict[str, int] = {"Ana": 22, "Luis": 19, "Marta": 30}

nombre_joven: str = min(personas, key=lambda k: personas[k])

print(f"La persona más joven es: {nombre_joven}")