import os
os.system("cls")

nota1 = float(input("Nota 1: "))   
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Nota 2: "))
    if nota2 >= 0 and nota2 <= 10:
        media = (nota1+nota2)/2
        if media >=6:
            print(f"Média {media} - aprovado")
        else:
            print(f"Média {media} - Reprovado")
    else:
        print(f"Nota {nota2} inválida")
else:
    print(f"Nota {nota1} inválida")