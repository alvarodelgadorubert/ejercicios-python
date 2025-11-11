inicio_str = input()
fin_str = input()

try:
    num1 = int(inicio_str)
    num2 = int(fin_str)
except ValueError:
    num1 = 0
    num2 = 0

if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

contador = num1
while contador <= num2:
    if contador % 2 == 0:
        print(contador)
    contador += 1