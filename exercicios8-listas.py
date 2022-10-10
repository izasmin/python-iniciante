# Exercício 1 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nota = []

for i in range(1,5):
  numero = float(input(f'Digite a {i}ª nota: '))
  nota.append(numero)

media = sum(nota) / len(nota)
print(f'As notas tiradas foram: {nota}.')
print(f'A média final é igual a {media}.')

# Exercício 2 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

consoantes = []
vogais = ['A', 'E', 'I', 'O', 'U']

for i in range(5):
  letra = input('Digite uma letra: ').upper()
  if letra in vogais:
    pass
  else:
    consoantes.append(letra)

print(f'Foram digitadas {len(consoantes)} consoantes.')
print(f'As consoantes digitadas foram: {consoantes}.')

# Exercício 3 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []

for i in range(10):
  numero = int(input('Digite um número: '))
  vetor.append(numero)

vetor.sort()

print('\n')
print(vetor)

# Exercício 4 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range (1, 4):
  anos = int(input(f'Informe a idade da {i}ª pessoa: '))
  idade.append(anos)
  centimetros = float(input(f'Informe a altura da {i}ª pessoa: '))
  altura.append(centimetros)

idade.reverse()
altura.reverse()

print()
print(idade)
print(altura)

# Exercício 5 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
# elementos intercalados dos dois outros vetores.

vetor_1 = []
vetor_2 = []
vetor_3 = []

for _ in range (5):
  numero = float(input('Digite um número do primeiro conjunto: '))
  vetor_1.append(numero)

print()

for _ in range (5):
  numero = float(input('Digite um número do segundo conjunto: '))
  vetor_2.append(numero)

print()

for i in range(5):
  vetor_3.append(vetor_1[i])
  vetor_3.append(vetor_2[i])

print(vetor_3)

# Exercício 6 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior
# à média de altura desses alunos.

idades = []
alturas = []
contador = 0

for i in range (1, 6):
  anos = int(input(f'Quantos anos o aluno {i} tem? '))
  tamanho = float(input(f'Qual é a altura do aluno {i}? '))
  idades.append(anos)
  alturas.append(tamanho)

print()
media_alturas = sum(alturas) / len(alturas)
print(f'A altura média é: {media_alturas:.2f} m.')

for i in range(5):
  if (idades[i] > 13) and (alturas[i] < media_alturas):
    contador += 1

print(f'Existem {contador} alunos com MAIS DE 13 anos e com altura INFERIOR à altura média dos alunos.')

# Exercício 7 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das
# temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperatura = []
meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

for i in range (1,13):
  temp = float(input(f'Informe a temperatura média do mês {i}: '))
  temperatura.append(temp)
  anual = sum(temperatura) / len(temperatura)

print()
print(f'A temperatura média anual foi de {anual} ºC.')
print()

for i in range(12):
  if temperatura[i] > anual:
    print(f'{i + 1} - {meses[i]} teve a temperatura média: {temperatura[i]} ºC.')

# Exercício 8 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

csi = []
respostas = 0

telefonou = input('Telefonou para a vítima? [S / N] ').upper()
csi.append(telefonou)
local = input('Esteve no local do crime? [S / N] ').upper()
csi.append(local)
mora = input('Mora perto da vítima? [S / N] ').upper()
csi.append(mora)
devia = input('Devia para a vítima? [S / N] ').upper()
csi.append(devia)
trabalhou = input('Já trabalhou com a vítima? [S / N] ').upper()
csi.append(trabalhou)

quantidade = len(csi)
for i in range(quantidade):
  if csi[i] == 'S':
    respostas += 1

print()

if respostas == 2:
  print('SUSPEITO')
elif 2 < respostas < 5:
  print('CUMPLICE')
elif respostas == 5:
  print('ASSASSINO')
else:
  print('INOCENTE')

# Exercício 9 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe 200.00
# por semana mais 9% de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de 3000.00 em uma semana recebe 200.00 mais
# 9% de 3000.00, ou seja, um total de 470.00. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos
# seguintes intervalos de valores:

# 200 - 299
# 300 - 399
# 400 - 499
# 500 - 599
# 600 - 699
# 700 - 799
# 800 - 899
# 900 - 999
# 1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

comissao = []
cont = 0

funcionarios = int(input('Informe a quantidade de salários que deseja verificar: '))

print()

for i in range(funcionarios):
  vendas = float(input(f'Informe o valor das vendas dessa semana do funcionário {i + 1}: R$'))
  calculo = 200 + (vendas * 0.09)
  comissao.append(calculo)
  print(f'R${calculo:.2f}')

print()

for i in range(200, 999, 100):
  for s in range(len(comissao)):
    if i <= comissao[s] < (i + 100):
      cont += 1
  print(f'R${i:.2f} - R${i + 99:.2f} -> {cont}')
  cont = 0

for _ in range(len(comissao)):
  if comissao[_] > 1000:
    cont += 1
print(f'R$1000.00 em diante -> {cont}')

# https://github.com/fernandoalvesrufino/exercicios_resolvidos_da_python_brasil/tree/main/4_exercicio_listas

# Exercício 10 - Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo.
# Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi
# contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número,
# entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido
# for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa
# deverá exibir:

# O total de votos computados;

# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

print('Enquete: Quem foi o melhor jogador?')
melhores_jogadores = []
maior_voto = 0
melhor_jogador = 0
melhor_porcentagem = 0

while True:
    try:
        jogador = float(input('Número do jogador: '))
    except ValueError:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    else:
        if 0 < jogador < 24:
            melhores_jogadores.append(jogador)
        elif jogador == 0:
            break
        else:
            print('Informe um valor entre 1 e 23 ou 0 para sair!')

print()
print('Resultado da votação: ')
print()
print(f'Foram computados {len(melhores_jogadores)} votos.')
print()
print('Jogador          Votos          %')
melhores_jogadores.sort()

for i in range(24):
    contador = 0
    for _ in range(len(melhores_jogadores)):
        if i == melhores_jogadores[_]:
            contador += 1

    porcentagem = (contador / len(melhores_jogadores)) * 100

    if contador > maior_voto:
        melhor_jogador = i
        melhor_porcentagem = porcentagem
        maior_voto = contador

    if contador != 0:
        print(f'{i:4}{contador:16}{porcentagem:14.1f}%.')

print()
print(
    f'O melhor jogador foi o número {melhor_jogador}, com {maior_voto} votos, correspondendo a {melhor_porcentagem:.1f}% do total de votos.')

# Exercício 11 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os
# valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular
# a percentual de cada um dos concorrentes e informar o vencedor da enquete.

vetor = []
maior = 0

sistema_operacional = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro' ]

print('Enquete: Qual o melhor Sistema Operacional para uso em servidores? ')
print('''
1 - Windows Server
2 - Unix
3 - Linux
4 - Netware
5 - Mac OS
6 - Outro
''')

while True:
  try:
    nota = int(input('Informe qual o melhor Sistema Operacional para uso em servidores, na sua opinião: '))
  except ValueError:
    print('Você deve escolher uma opção entre 1 e 6'.upper())
  else:
    if nota == 0:
      break
    elif 0 < nota < 7:
      vetor.append(nota-1)
    else:
      print('Você deve escolher uma opção entre 1 e 6'.upper())

print()
print('Sistema Operacional     Votos     %')
print('-------------------     -----    ---')
for i in range(6):
  contador = 0
  for _ in range(len(vetor)):
    if i == vetor[_]:
      contador += 1
  porcentagem = (contador / len(vetor)) * 100
  print(f'{sistema_operacional[i]:14}{contador:13}{porcentagem:9.1f}')

  if contador > maior:
    maior = contador
    maior_porcentagem = porcentagem
    melhor_sistema = sistema_operacional[i]

print()
print('-------------------     -----    ---')
print(f'Total            {len(vetor):10}')

print(f'O Sistema Operacional mais votado foi o {melhor_sistema}, com {maior} votos, correspondendo a {maior_porcentagem:.1f}% dos votos.')

# Exercício 12 - As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que
# passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono. Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

# a. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
# b. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:

# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono;
# A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

salario = []
abono = []
minimo = 0
maior = 0

while True:
  valor = float(input('Salário: '))
  if valor == 0:
    break
  else:
    salario.append(valor)
    beneficio = valor * 0.2
    if beneficio <= 100:
      minimo += 1
      beneficio = 100
      abono.append(beneficio)
    else:
      abono.append(beneficio)
    if beneficio > maior:
      maior = beneficio

print()
print('    Salário      -      Abono')
for i in range(len(salario)):
  print(f'R$ {salario[i]:10.2f}    - R$ {abono[i]:10.2f}')

print()

print(f'Número de funcionários processados: {len(salario)}')
print(f'Valor total gasto com o pagamento do abono: R$ {sum(abono):.2f}')
print(f'A quantidade de funcionários que receberá o valor mínimo é: {minimo}')
print(f'O maior valor pago como abono foi: R$ {maior:.2f}')

# Exercício 13 - Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:

# - O modelo do carro mais econômico;
# - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando
# um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados
# são fictícios e podem mudar a cada execução do programa.

modelo = []
km = []
litros = []
preco = []
menor = 0
melhor_autonomia = 0

for i in range(5):
  print(f'Veículo {i+ 1}')
  marca = input('Nome: ')
  modelo.append(marca)
  autonomia = float(input('Km por litro: '))
  km.append(autonomia)
  print()
  calculo = 1000 / autonomia
  litros.append(calculo)
  valor = calculo * 2.25
  preco.append(valor)
  if km[i] > melhor_autonomia:
    melhor_autonomia = km[i]
    menor = i

print('Relatório final: ')
for i in range(5):
  print(f'{i + 1} - {modelo[i]:15} - {km[i]:10.3f} - {litros[i]:10.2f} litros - R$ {preco[i]:10.2f}')


print(f'O menor consumo é o da {modelo[menor]}')

# Exercício 14 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas
# encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para
# verificar o que se pode aproveitar deles.

# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo:
# um número de identificação do mouse o tipo de defeito:

# - necessita da esfera;
# - necessita de limpeza;
# - necessita troca do cabo ou conector;
# - quebrado ou inutilizado
# - Uma identificação igual a zero encerra o programa.

# Ao final o programa deverá emitir o seguinte relatório:

identificacao = []
a = 0
b = 0
c = 0
d = 0

print(f'''
Defeitos:
[A] Necessita da esfera;
[B] Necessita de limpeza; 
[C] Necessita troca do cabo ou conector; 
[D] Quebrado ou inutilizado 
''')

while True:
  codigo = int(input('Identificação do mouse: '))
  if codigo == 0:
    break
  elif codigo < 0:
    print('Informe um código positivo válido ou digite 0 para encerrar.')
  elif codigo > 0:
    identificacao.append(codigo)
    while True:
      classificacao = input('Selecione o tipo de defeito: [A], [B], [C] ou [D] ').upper()
      if classificacao == 'A':
        a += 1
        break
      elif classificacao == 'B':
        b += 1
        break
      elif classificacao == 'C':
        c += 1
        break
      elif classificacao == 'D':
        d += 1
        break
      else:
        print('Informe um tipo de defeito entre A, B, C ou D!')
  else:
    print('Informe um código positivo válido ou digite 0 para encerrar.')

total = a + b + c + d
pa = (a / total) * 100
pb = (b / total) * 100
pc = (c / total) * 100
pd = (d / total) * 100

print()
print(f'Quantidade de mouses: {len(identificacao)}')
print(f'''
         Situação                                   Qtd                     %
[A] Necessita da esfera:                              {a}                   {pa:.1f}
[B] Necessita de limpeza:                             {b}                   {pb:.1f}
[C] Necessita troca do cabo ou conector:              {c}                   {pc:.1f}
[D] Quebrado ou inutilizado:                          {d}                   {pd:.1f}
''')

# Exercício 15 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema,
# o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da
# Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

lista_de_dados = []


def transformar_em_megabytes(tamanho_em_bytes: str) -> float:
    return int(tamanho_em_bytes) / (2 ** 10) ** 2


with open('sample_data/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_megabytes(linha[16:])
        lista_de_dados.append((usuario, tamanho_em_disco))

cabecalho = '''ACME Inc.           Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
'''
with open('sample_data/relatório.txt', 'w') as arquivo:
    tamanho_total_consumido = sum([tamanho for _, tamanho in lista_de_dados])
    media = tamanho_total_consumido / len(lista_de_dados)
    arquivo.writelines(cabecalho)
    for indice, dados in enumerate(lista_de_dados, start=1):
        usuario, tamanho_em_disco = dados
        arquivo.writelines(
            f'{indice:<4} {usuario} {tamanho_em_disco:9.2f} MB'
            f'{tamanho_em_disco / tamanho_total_consumido:16.2%}\n'
        )
    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {media:.2f} MB')

# Exercício 16 - Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes
# cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

aleatorio = []

for i in range(100):
  numero = random.randint(1, 6)
  aleatorio.append(numero)

for i in range(1,7):
  print(f'{i} - {aleatorio.count(i)}')