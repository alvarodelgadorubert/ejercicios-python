meses: list[str] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num_mes: int = 0
while num_mes < 1 or num_mes > 12:
    num_mes = int(input("Introduce un número de mes (1-12): "))

indice: int = num_mes - 1
print(f"El mes es {meses[indice]} y tiene {dias[indice]} días.")