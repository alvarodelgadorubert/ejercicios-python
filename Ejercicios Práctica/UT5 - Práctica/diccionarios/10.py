catalogo: dict[str, float] = {
    "leche": 1.2,
    "pan": 0.8,
    "huevos": 2.1,
    "queso": 3.5
}

total_compra: float = 0.0

while True:
    prod: str = input("Introduce producto (o 'FIN'): ").lower()
    if prod == "fin":
        break
    
    if prod in catalogo:
        cant: int = int(input(f"¿Cuántas unidades de {prod}?: "))
        precio_uni: float = catalogo[prod]
        subtotal: float = precio_uni * cant
        total_compra += subtotal
        print(f"Desglose: {prod} x{cant} | Precio/u: {precio_uni}€ | Subtotal: {subtotal}€")
    else:
        print("Producto no disponible.")

print(f"Total a pagar: {total_compra}€")