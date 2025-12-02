total_compra = float(input("Ingresa el total de la compra: "))
descuento = total_compra * 0.15
total_pagar = total_compra - descuento
print(f"Descuento: {descuento:.2f}")
print(f"Total a pagar: {total_pagar:.2f}")