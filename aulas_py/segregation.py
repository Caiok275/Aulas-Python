import os
os.system("cls")

sex = input("Qual o seu genero? f ou m")
if sex == 'f':
    money = 0
if sex == 'm':
    money = 50
print(f"Você pagará {money:.2f} Reais")