import os
os.system("cls")

compra = float(input("Digite o valor da compra: "))
print(
     "---------------------------------------\n"
     "Escolha o metodo de pagamento:\n"
    f"1 - PIX (5% de desconto)\n"
     "2 - Dinheiro (mesmo valor da compra)\n"
    f"3 - Débito (acréscimo de 1%)\n"
    f"4 - Crédito (acréscimo de 2.5%)\n"
     "---------------------------------------")
paga = int(input())

match paga:
    case 1:
        total = compra - (compra*0.05)
        print(
             "---------------------------------------\n"
            f"Compra: {compra:.0f}\n"
            f"Forma de pagamento: {paga}\n"
             "\n"
            f"Valor original: {compra:.0f}\n"
            f"Valor ajustado: {total:.0f}\n"
             "---------------------------------------")
    case 2:
        print(
             "---------------------------------------\n"
            f"Compra: {compra:.0f}\n"
            f"Forma de pagamento: {paga}\n"
             "\n"
            f"Valor original: {compra:.0f}\n"
            f"Valor ajustado: {compra:.0f}\n"
             "---------------------------------------")
    case 3:
        total = compra + (compra*0.01)
        print(
             "---------------------------------------\n"
            f"Compra: {compra:.0f}\n"
            f"Forma de pagamento: {paga}\n"
             "\n"
            f"Valor original: {compra:.0f}\n"
            f"Valor ajustado: {total:.0f}\n"
             "---------------------------------------")
    case 4:
        total = compra + (compra*0.025)
        print(
             "---------------------------------------\n"
            f"Compra: {compra:.0f}\n"
            f"Forma de pagamento: {paga}\n"
             "\n"
            f"Valor original: {compra:.0f}\n"
            f"Valor ajustado: {total:.0f}\n"
             "---------------------------------------")