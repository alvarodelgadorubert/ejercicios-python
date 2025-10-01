sueldo_base = float(input("Ingresa el sueldo base: "))
venta1 = float(input("Ingresa el monto de la primera venta: "))
venta2 = float(input("Ingresa el monto de la segunda venta: "))
venta3 = float(input("Ingresa el monto de la tercera venta: "))
comisiones = (venta1 + venta2 + venta3) * 0.10
total_mes = sueldo_base + comisiones
print(f"Comisiones: {comisiones:.2f}")
print(f"Total del mes: {total_mes:.2f}")