"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso
(peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""
peso = float(input("Digite o peso da pesca em Kg: "))
excesso = peso - 50
multa = excesso * 4
print(f"Foram {excesso:.2f}Kg em excesso, logo, a multa é de R${multa:.2f}.")

"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax² + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo
        grau e o programa não deve fazer pedir os demais valores,
        sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raízes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz
        real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;
"""
a = float(input("Digite o valor de a: "))
if a == 0:
    print("Não é uma equação do segundo grau")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Delta menor que 0. Não há raízes reais.")
    elif delta == 0:
        raiz = (-b) / (2 * a)
        print(f"Delta é zero. A raíz é {raiz}")
    else:
        raiz1 = (-b + (delta ** (1 / 2))) / (2 * a)
        raiz2 = (-b - (delta ** (1 / 2))) / (2 * a)
        print(
            f"Delta maior que zero. A raíz 1 é {raiz1}, e a raiz 2 é {raiz2}"
        )
        
"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
é uma data válida.
"""
data = input("Digite uma data no formato dd/mm/aaaa: ")
# Isto separa os elementos da data em uma lista.
# O fim de um elemento se dá por uma /
# Como são 3 elementos, podemos fazer uma atribuição múltipla direta
dia, mes, ano = data.split("/")
# E aqui transformamos os valores em inteiros para facilitar comparações
dia, mes, ano = int(dia), int(mes), int(ano)

if ano < 0:
    print("Ano inválido!")
else:
    if mes < 1 or mes > 12:
        print("Mês inválido!")
    # Isto testa se o mês é um destes dentro da lista
    # Poderiam ser feitas diversas comparações utilizando o or
    # ex. mes == 1 or mes == 3...
    # Mas achei isso mais simples.
    elif mes in [1, 3, 5, 7, 8, 10, 12]:  # meses com 31 dias
        if dia > 0 and dia < 32:
            print("Data válida!")
        else:
            print("Dia inválido!")
    elif mes in [4, 6, 9, 11]:  # meses com 30 dias
        if dia > 0 and dia < 31:
            print("Data válida!")
        else:
            print("Dia inválido!")
    else:  # fevereiro
        if ano % 4 == 0:  # Ano bissexto
            if dia > 0 and dia < 30:
                print("Data válida!")
            else:
                print("Dia inválido!")
        else:  # Ano não bissexto
            if dia > 0 and dia < 29:
                print("Data válida!")
            else:
                print("Dia inválido!")
              
 """
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.
"""
usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")
while usuario == senha:
    print("Nome de usuario nao pode ser igual a senha!")
    usuario = input("Digite o nome de usuario: ")
    senha = input("Digite a senha: ")
 """
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem
inversa a ordem lida.
"""
PESSOAS = 5
idades = []
alturas = []
for i in range(PESSOAS):
    idades.append(int(input(f"Digite a idade da pessoa {i+1}: ")))
    alturas.append(float(input(f"Digite a altura da pessoa {i+1} em cm: ")))

# ? i começa em 4 e vai até 0 de forma decrescende
for i in range(PESSOAS - 1, -1, -1):
    print(f"A pessoa {i+1} mede {alturas[i]:.2f}cm e tem {idades[i]} ano(s)")
    
"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
a soma dos quadrados dos elementos do vetor.
"""
soma_dos_quadrados = 0
for i in range(10):
    soma_dos_quadrados += int(input(f"Digite o {i+1}º numero inteiro: ")) ** 2
print(f"A soma dos quadrados dos numeros digitados é {soma_dos_quadrados}")

"""
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores.
"""
ELEMENTOS = 10
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(ELEMENTOS):
    vetor1.append(
        int(input(f"Entre com o {i+1}º número inteiro para o vetor 1: "))
    )
for i in range(ELEMENTOS):
    vetor2.append(
        int(input(f"Entre com o {i+1}º número inteiro para o vetor 2: "))
    )
for i in range(ELEMENTOS):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print("O vetor com os elementos intercalados dos vetores 1 e 2 é: ")
for i in range(ELEMENTOS * 2):
    print(vetor3[i], end=" ")
    
  as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem
altura inferior à média de altura desses alunos.
"""
ALUNOS = 30
idades = []
alturas = []
media_de_altura = 0
abaixo_da_media = 0

for i in range(ALUNOS):
    idades.append(int(input(f"Digite a idade do aluno {i+1}: ")))
    altura = int(input(f"Digite a altura em cm do aluno {i+1}: "))
    alturas.append(altura)
    media_de_altura += altura

media_de_altura /= ALUNOS

for i in range(ALUNOS):
    if idades[i] > 13:
        if alturas[i] < media_de_altura:
            abaixo_da_media += 1

print(
    f"{abaixo_da_media} alunos com mais de 13 anos têm altura abaixo da média"
)

"""
Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as
temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]
temperaturas = []
for i in range(12):
    temperaturas.append(
        float(input(f"Digite a temperatura de {meses[i]} em ºC: "))
    )

media = sum(temperaturas) / 12
print(f"\nA média das temperaturas foi {media:.2f}ºC")
print("Meses com temperaturas acima da média: ")
for i in range(12):
    if temperaturas[i] > media:
        print(f"{i+1} - {meses[i].capitalize()} com {temperaturas[i]:.2f}ºC")
