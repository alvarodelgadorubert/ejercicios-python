estudiantes: dict[str, dict[str, float]] = {
    "Ana": {"nota1": 8.5, "nota2": 7.0, "nota3": 9.0},
    "Luis": {"nota1": 5.0, "nota2": 6.5, "nota3": 4.0},
    "Marta": {"nota1": 9.0, "nota2": 10.0, "nota3": 9.5}
}

for nombre, notas in estudiantes.items():
    suma: float = sum(notas.values())
    media: float = suma / len(notas)
    print(f"La media de {nombre} es: {media:.2f}")