li=int(input("Límite inf: "))
ls=int(input("Límite sup: "))
while li>ls:
    li=int(input("Límite inf: "))
    ls=int(input("Límite sup: "))
suma=0; fuera=0; igual=False
for _ in range(1000000):
    num=int(input("Número (0 fin): "))
    if num==0: break
    if li<num<ls: suma+=num
    else: fuera+=1
    if num in (li,ls): igual=True
print(suma, fuera, igual)