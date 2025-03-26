import os
os.system("cls")

nome = "Edson de Oliveira"
idade = 50
altura = 1.71

#Com .format
print("Nome: {0}\nIdade:  {1}\nAltura: {2}".format(nome, idade, altura))

#Com .format alias
print("Nome: {a}\nIdade:  {b}\nAltura: {c}".format(a=nome, b=idade, c=altura))

#Com f print
print(f"Nome: {nome}\nIdade:  {idade}\nAltura: {altura}")

#Com Triple Quotes
print(f"""
Nome: {nome}
Idade:  {idade}
Altura: {altura}
""")

#Com %
print("Nome: %s \nIdade:  %d \nAltura: %f" % (nome, idade, altura))

numero_dec = 337
print("Decimal: %d | Octal: %o | Hexadecimal: %x" % (numero_dec,numero_dec,numero_dec))

#fomatação dados numericos
val1 = 55
val2 = 34.6555
val3 = 6688.3
val4 = 444.44

print(f'''
Valor 1: {val1:10.2f}
Valor 2: {val2:10.2f}
Valor 3: {val3:10.2f}
Valor 4: {val4:10.2f}
''')