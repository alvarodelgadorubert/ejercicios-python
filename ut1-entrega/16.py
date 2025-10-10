distancia = float(input("Ingresa la distancia entre los vehículos (km): "))
v1 = float(input("Ingresa la velocidad del vehículo más lento (km/h): "))
v2 = float(input("Ingresa la velocidad del vehículo más rápido (km/h): "))
velocidad_relativa = v2 - v1
if velocidad_relativa > 0:
    tiempo_horas = distancia / velocidad_relativa
    tiempo_minutos = tiempo_horas * 60
    print(f"El vehículo rápido alcanzará al lento en {tiempo_minutos:.2f} minutos")
else:
    print("El vehículo detrás no es más rápido")