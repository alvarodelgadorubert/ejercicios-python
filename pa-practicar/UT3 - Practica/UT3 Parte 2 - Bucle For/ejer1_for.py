n = int(input("Introduce un número: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! = {fact}")