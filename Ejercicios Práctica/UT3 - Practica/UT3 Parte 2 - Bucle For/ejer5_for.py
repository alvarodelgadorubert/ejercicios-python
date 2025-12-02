a=int(input("Introduce primer número: "))
b=int(input("Introduce segundo número: "))
if a>b:a,b=b,a
for num in range(a,b+1):
    if num%2==0: print(num)