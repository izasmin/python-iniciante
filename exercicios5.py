#faça um algoritmo que solicite ao usuário números e os armazene em uma matriz 6×6. Em seguida, crie um vetor que armazene os elementos da diagonal principal da matriz.
vet = [0]*6
mat = [0]*6
for x in range(6):
    mat[x] = [0]*6

for lin in range(6):
    for col in range(6):
        mat[lin][col] = input('Digite um valor: ')
print mat

for lin in range(6):
    for col in range(6):
        print lin,col
        if lin == col:
            print 'DP', lin, col
            vet[lin] = mat[lin][col]
print vet

#tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50, mostre a média dos elementos da diagonal secundária.
import random

tam = 10
m = [0]*tam
for i in range(tam):
    m[i] = [0]*tam
for i in range(tam):
    for j in range(tam):
        m[i][j] = random.randint(10,50)

aux = tam-1
soma = 0

for i in range(tam):
    soma = soma + m[i][aux]
    aux = aux - 1

for i in range(tam):
    print m[i][:]
print 'Média: ', soma/float(tam)

# tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50, mostre qual é o maior valor existente na matriz desconsiderando os elementos da diagonal principal.
import random
mat = [0]*3
for i in range(3):
    mat[i] = [0]*3

for i in range(3):
    for j in range(3):
        mat[i][j] = random.randint(10,50)
print mat

maior = mat[1][0]
for i in range(3):
    for j in range(3):
        if i != j:
            if mat[i][j] > maior:
                maior = mat[i][j]
print maior

#tendo uma matriz 5×5 preenchida com valores aleatórios entre 0 e 99, mostre qual é o segundo maior valor existente na matriz.
import random
tam = 5

mat = [0]*tam
for i in range(tam):
    mat[i] = [0]*tam
print mat

for i in range(tam):
    for j in range(tam):
        mat[i][j] = random.randint(0, 99)
print mat

maior = mat[0][0]
for i in range(tam):
    for j in range(tam):
        if mat[i][j] > maior:
            maior = mat[i][j]
print maior

segundomaior = 0
for i in range(tam):
    for j in range(tam):
        if mat[i][j] > segundomaior and mat[i][j] != maior:
            segundomaior = mat[i][j]
print segundomaior

#crie um algoritmo que leia um valor e a partir disso faça: (1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado; (2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; (3) se for os valores 6, 7 e 8, mostre o valor dividido 9.
import math

num = input('Digite um valor: ')
if num >= 1 and num <= 3:
    print num**2
elif num == 4 or num == 9:
    print math.sqrt(num)
elif num == 6 or num == 7 or num == 8:
    print num/9.0


# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   a."Telefonou para a vítima?"
#   b."Esteve no local do crime?"
#   c."Mora perto da vítima?"
#   d."Devia para a vítima?"
#   e."Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado
# como "Inocente".
############################################################################################


def gerarPerguntas():
    # armazenar quantidade resultado positivo.
    quantidade_positivo = 0

    # status da resposta.
    status = {2: "Suspeito(a)",
              3: "Cúmplice",
              4: "Cúmplice",
              5: "Assassino"}

    # armazenar uma lista de perguntas.
    lista_perguntas = ["Telefonou para a vítima?",
                       "Esteve no local do crime?",
                       "Mora perto da vítima?",
                       "Devia para a vítima?",
                       "Já trabalhou com a vítima?"]

    # fazer as perguntas.
    for index in len(lista_perguntas):
        # efetuar a pergunta.
        print(lista_perguntas[index] + " (sim ou não).")

        # Obter uma resposta.
        resposta = input("Resp.:")

        # Analisar a resposta e se for positivo incrementar o valor
        if resposta.lower() == "sim":
            # incrementar mais um.
            quantidade_positivo += 1

    # Verificar compatibilidade dos dados com o status.
    if quantidade_positivo in status:
        # Titular o status da pessoa.
        print(status[quantidade_positivo])

    else:
        print("Inocente")

