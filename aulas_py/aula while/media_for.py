import os
os.system("cls")

soma = 0
qtd_num = int(input("Quantos números?"))
for count in range(1, qtd_num + 1, 1):
    num = float(input(f"Número {count}: "))
    soma = soma + num
else:
    media = soma / qtd_num

print(f"Media = {media}")