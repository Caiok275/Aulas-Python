import os
os.system("cls")

soma = 0
while True:
    num = int(input("Número: "))
    if num == 0:
        break
    else:
        soma = soma + num

print(f"Soma = {soma}")



'''
print("programa com o laço repita!")
while True:
    num = input("Numero: ")
    if not num.isnumeric():
        print("Você não digitou um número.")
        continue
    else:
        num = int(num)
        break

print("Digitou um número!")
print(num, type(num))
'''