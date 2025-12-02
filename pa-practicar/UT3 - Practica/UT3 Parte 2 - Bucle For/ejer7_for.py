base=float(input("Base: "))
exp=int(input("Exponente positivo: "))
while exp<=0:
    exp=int(input("Exponente positivo: "))
pot=1.0
for _ in range(exp):
    pot*=base
print(pot)