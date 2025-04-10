import os
os.system("cls")

# range(inicio, fim, incremento):
for count in range(1,10,1):
    print(count, end = " ")

print()

inicio = 0
fim = 20

for count in range(inicio, fim + 1, 1):
    print(count, end = " ")

print()

for count in range (fim, inicio - 1, -1):
    print (count, end = " ")