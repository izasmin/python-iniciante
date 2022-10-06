#84
# Esse 84 complicou pra mim, na questão dos condicionais, pois ainda tenho dificuldade em fazer o "sort manual" (ou seja, ordenar uma lista sem o sort). Com o sort é só botar dentro de cada lista o peso antes do nome. As demais questões foram bem mais fáceis.


# Lista geral de participantes do campeonato
lisP = []
# Informações particulares
infPa = []
# contador de participantes adicionados
cPart = 0

while True:
    cPart += 1
    infPa.append(str(input(f'Digite o nome do {cPart}° participante:  ')))
    infPa.insert(0, float(input('Agora digite o peso do mesmo:  ')))
    lisP.append(infPa[:])
    infPa.clear()
    dec = int(input('\nDigite:\n [ 1 ] para adicionar outro participante, ou\n [ 2 ] para fechar o cadastro\n  -->  '))
    while dec != 1 and dec != 2:
        dec = int(input('Número inválido. Digite 1 pra continuar a cadastrar pessoas, ou 2 pra parar:  '))
    if dec == 2:
        break
    print('\n \n \n' + '-' * 35)

lisP.sort(reverse=True)

# maiores valores em lista
mVals = []
for val in lisP:
    mVals.append(val[0])

print(f'\n \n \n \n \nQuantidade de participantes: {cPart}\n \nMais pesados:  ', end='')

# informações do participante
for info in lisP:
    if info[0] == max(mVals):
        print(f'[{info[1]}]  ', end='')

print('\n \nMais leves:  ', end='')

for info in lisP:
    if info[0] == min(mVals):
        print(f'[{info[1]}]  ', end='')

#85

valor = list()
par = list()
impar = list()
for cont in range(0, 7):
    v = int(input('Informe um valor: '))
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
par.sort()
impar.sort()
valor.append(par[:])
valor.append(impar[:])
print(valor)

#86

for c in range(0,3):
    for x in range(0,3):
        matriz[c].append(int(input(f'Valor [{c}][{x}]: ')))

for c in range(0,3):
    for x in range(0,3):
        print(f'[{matriz[c][x]}]', end='')
    print()

#87

#88
#88 resolução aprimorada
from random import randint

qtd = int(input('Quantos jogos? '))
jogos = [[0, 0, 0, 0, 0, 0] for i in range(qtd)]
print(f'SORTEANDO {qtd} JOGOS...')
for i in range(qtd):
    pos = 0
    while pos < 6:
        rand = randint(1, 60)
        if rand not in jogos[i]:
            jogos[i][pos] = rand
            pos += 1
    print(f'Jogo {i+1}: {sorted(jogos[i])}')

#89
lisprin = [[], [[], []], []]
s = 0
se = 0
while True:
    s = s+1
    nom = str(input(f"Digite o nome do {s}º aluno(a): "))
    not1 = float(input(f"Digite a 1º nota do {s}º aluno(a): "))
    not2 = float(input(f"Digite a 2º nota do {s}º aluno(a): "))
    m = (not1 + not2)/2
    lisprin[0].append(nom)
    lisprin[1][0].append(not1)
    lisprin[1][1].append(not2)
    lisprin[2].append(m)
    cont = str(input("Você quer continuar[S/N]? "))
    if cont == "N":
        break
print("Boletim com a média de cada 1:")
for c in range(0, len(lisprin[0])):
    print("{}".format(lisprin[0][c]), end="")
    print(".............", "{}".format(lisprin[2][c]))
while True:
    most = str(input("Digite o nome do aluno que quer ver suas notas individualmente[Caso queira sair do programa, digite [S]]: "))
    if most in "Ss":
        break
    else:
        for c in range(0, len(lisprin[0])):
            if lisprin[0][c] == most:
                print(lisprin[0][c])
                print("Nota1: ", lisprin[1][0][c])
                print("Nota2: ", lisprin[1][1][c])