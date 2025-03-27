import os
os.system("cls")

n1 = float(input("Digite um valor:"))
n2 = float(input("Digite outro valor:"))
sinal = input("Agora digite um sinal para a operação:")

#Flag - Validação de dados
possivel = True

match sinal:

    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*" |"."|"x"|"X":
        resultado = n1 * n2
    case "/":
        if n2 == 0:
            print("Não é possível dividir por 0")
            #!!!
            possivel = False
        else:
            resultado = n1 / n2
    case _:
        print("Sinal inválido...")
        #!!!
        possivel = False

if possivel:
    print(f"{n1} {sinal} {n2} = {resultado}")