km1=70.0; km2=150.0
vel=float(input("Velocidad: "))
for hora in range(1,1000):
    km1+=vel
    km2-=vel
    if km1>=km2:
        print("Encuentro en km", km1, "en la hora", hora)
        break