#Faça um programa em Python que leia n números inteiros e positivos a apartir do teclado,
# até que o usuário digite 0. Ao final, informe o maior número digitado.
maior=-1
numero=int(input("Entre com um número inteiro e positivo:"))
while numero>=0:
   if numero>maior:
       maior=numero
   numero=int(input("Entre com um número inteiro e positivo:"))
print("o número", maior,"é o maior número digitado")

# Crie um programa em linguagem Python que permite ao usuário inserir os valores dos produtos
# comprados por um cliente. O programa deve terminar quando o usuário inserir o valor 0.
# Se o usuário digitar um valor negativo não deve ser processado e um novo valor deve ser
# solicitado como entrada. Ao final, informe o valor total a pagar, lembrando que,
# caso as vendas ultrapassem o total de R$ 1.000,00, deverá ser aplicado um desconto de 10%.

total=0
valor=float(input("Informe o valor do produto: R$"))
while valor!=0:
    if valor<0:
        print("Valor inválido.")
    else:
        total=total+valor;
    valor=float(input("Informe o valor do produto: R$"))
if total>1000:
    total-=total*0.1
print("Total a pagar: R$", total)

#A soma dos números pares de 1 a 7
soma = 0
cont = 0
for c in range (1,7):
    num = int(input())
    if num % 2 == 0
    soma += num
    cont += 1

    printf("Soma dos impares de 1 a 1000: %d\n\n", soma);
}

#Na primeira, você sabe quanto dinheiro quer poupar no total e quanto dinheiro vai poupar por mês, mas não sabe quantos meses vai levar até chegar nesse valor.
montante = .0  #  Valor do saldo corrente
objetivo = 10_000
capital = 300  #  Valor aplicado a cada mês
txJuros = .3 / 100  #  rendimento de 0,3% ao mês
meses = 0

while montante < objetivo:
    montante += capital  #  Aplicação no início do período
    juro = montante * txJuros #  Juros compostos
    montante += juro
    meses += 1
    print(f'Montante no mês {meses} = R${montante:.2f}')

print(f'Número de meses: {meses}')

#Na segunda situação você não tem um montante final em mente, mas se compromete a poupar o mesmo valor durante os próximos 12 meses. Esse seria um caso de uso do laço for.
montante = .0  #  Valor do saldo corrente
capital = 300  #  Valor aplicado em cada período
txJuros = .3 / 100  #  rendimento de 0,3% ao mês
meses = 12

for mes in range(meses):
    montante += capital
    juro = montante * txJuros #  Juros compostos
    montante += juro
    print(f'Montante no mês {mes + 1} = R${montante:.2f}')

