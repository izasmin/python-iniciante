# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao
# usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a
# seguir para obter o preço de cada produto:

# Código Preço
# 1 0,50
# 2 1,00
# 3 4,00
# 5 7,00
# 9 8,00
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

prod = int(input("Código: "))
qt = int(input("Quantidade:"))
if prod == 1:
    valor = 0.5 * qt
    print("O valor é: {}".format(valor))
elif prod == 2:
    valor = 1 * qt
    print("O valor é: {}".format(valor))
elif prod == 3:
    valor = 4 * qt
    print("O valor é: {}".format(valor))
elif prod == 5:
    valor = 7 * qt
    print("O valor é: {}".format(valor))
elif prod == 9:
    valor = 8 * qt
    print("O valor é: {}".format(valor))
else:
    print("Código Inválido")

#Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao
#usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a
#seguir para obter o preço de cada produto:

#Código Preço
#1 0,50
#2 1,00
#3 4,00
#5 7,00
#9 8,00
#Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro
#código deve gerar a mensagem de erro “Código inválido”.

apagar = 0
while True:
    cod = int(input("Código da mercadoria ou 0 para sair " ))
    valor = 0
    if cod == 0:
        break
    elif cod == 1:
        valor= 0.5
    elif cod == 2:
        valor = 1
    elif cod == 3:
        valor = 4
    elif cod == 5:
        valor = 7
    elif cod == 9:
        valor = 8
    else:
        print("Código Inválido")
    if valor != 0:
        qt = int(input("Quantidade:"))
        apagar = apagar + (valor * qt)
    print(f"Total a pagar R$(apagar: 8.2f)")

#Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se
#continua o mesmo caso seus dígitos sejam invertidos. Exemplos: 454, 10501

s = input("Digite o número a verificar, sem espaços: ")
i = 0
f = len(s)-1
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print(f"(s) é palíndromo")
else:
    print(f"(s) não é palíndromo")