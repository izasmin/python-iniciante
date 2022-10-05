# Desafio 078

lst, aux = list(), list()
numMaior, numMenor, counter = None, None, 0

# Preenche a lista com 5 valores numericos e a exibe
for i in range(0, 5):
    lst.append(float(input(f'Digite o valor {i+1}: ')))
print(lst)

# Obtem o valor maior e o menor
numMaior, numMenor = max(lst), min(lst)

# Faz a contagem das vezes em que o maior valor aparece na lista
for i in range(0, len(lst)):
    if lst[i] == numMaior:
        aux.append(i)
print(f'O maior valor e {numMaior} e ele esta nas posicoes {aux}.')

# Faz a contagem das vezes em que o menor valor aparece na lista
aux = list()
for i in range(0, len(lst)):
    if lst[i] == numMenor:
        aux.append(i)
print(f'O menor valor e {numMenor} e ele esta nas posicoes {aux}.')

#Desafio 079

lst = list()

# Preenche a lista com 5 valores numericos e a exibe
while True:
    valor = float(input(f'Digite o valor que quer adicionar a lista: '))
    if valor in lst:
        print('\n*** Esse valor ja existe na lista. Digite outro. ***')
    else:
        lst.append(valor)
        print(lst, '\n')

        aux = int(input('Quer adicionar mais valores?\n1 - Sim\nOutro Valor - Nao\n\n>> '))
        if aux != 1:
            break

print(sorted(lst))

# Desafio 080 - solucao 1

lst = list()
i = j = cont = None

# Preenche a lista com 5 valores numericos
for i in range(0, 5):
    valor = int(input(f'Digite o valor {i+1}: '))
    if len(lst) == 0:
        lst.append(valor)
    else:
        cont = 0
        for j in range(0, len(lst)):
            if valor < lst[j]:
                lst.insert(j, valor)
                cont = 1
                break
        if cont == 0:
            lst.insert(j+1, valor)
    print(lst)

print(lst)

#Desafio 80 - metodo 2 usando bubble sort
lista = list()
contador = 0
while True:
    valor = int(input('Digite um valor: '))
    contador += 1
    if contador == 1:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        lista.append(valor)
        for b in range(len(lista)):
            for a in range(len(lista) - 1):
                if lista[b] < lista[a]:
                    aux = lista[b]
                    lista[b] = lista[a]
                    lista[a] = aux
        print('Valor adicionado ao final da lista...' if len(lista) - 1 == lista.index(valor) else f'Adicionado na posição {lista.index(valor)} da lista...')
    if contador == 5:
        break
print(lista)

#81 - Me desafiei a fazer esse exercicio sem usar o SORT tambem
lista = []
count = 0
while 1:
    num = int(input('Digite um número: '))
    if count == 0 or num < min(lista):
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num >= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
    count += 1
    flag = input('Quer continuar? [S/n]: ')
    if flag in 'Nn': break

print(f'Foram digitados {count} números.')
print(f'Lista em ordem decrescente: {lista}')
print('Nenhum valor 5 foi digitado' if 5 not in lista else f'O valor 5 foi digitado {lista.count(5)} vezes.')


#082

comp = []
impar = []
par = []
while True:
    perg = int(input('Digite um valor: '))
    comp.append(perg)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp != 'N' and resp != 'S':
        while resp != 'N' and resp != 'S':
            resp = str(input('Resposta inválida! Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    if perg % 2 == 0:
        par.append(perg)
    else:
        impar.append(perg)
print(f'Você digitou os valores {comp}')
print(f'Os valores pares são: {par}')
print(f'E os valores ímpares são: {impar}')

#83
a resolução é essa:

equacao = []
parenteseesquerda = 0
parentesedireira = 0
texto = str(input('digite a sua equação : '))
equacao.append(texto)
for palvra in equacao:
    for carcter in palvra:
        if carcter in ')':
            parentesedireira += 1
        elif carcter in '(':
            parenteseesquerda += 1
if parenteseesquerda == parentesedireira:
    print(f'está equação é válida')
else:
    print('está equação está  inválida')

#Desafio 83 - forma 2
Desafio 83
expressao = []
analisador = []

user = input('Digite uma expressão: ').strip()
expressao.append(user)
print(f'\nExpressão = {expressao}')


for k in range(0,len(expressao[0])):
    analisador.append(expressao[0][k])
print(f'Analisador = {analisador}\n')


cnt_a = cnt_b = 0
while True:
    for c in analisador:
        if '(' in c:
            cnt_a += 1
        if ')' in c:
            cnt_b += 1
    break
if cnt_a == cnt_b:
    print('Expressão válida')
else: print('Expressão inválida')
