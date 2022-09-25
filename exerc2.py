#Aprovado ou Reprovado
nota=int(input("Digite para saber se foi aprovado ou reprovado: "))
if nota<4:
    print("Reprovado")
elif nota >4 and nota<=6:
    print("Exame")
else:
    print("Aprovado")
#Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
# Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias,
# e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
nota1 = int(input(" Sua nota: "))
nota2 = int(input(" Sua nota: "))
nota3 = int(input(" Sua nota: "))
if nota1 > 7 and nota2 > 7 and nota3 > 7:
    print("Aprovado")
else:
    print("Reprovado")
#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
valor = int(input(" Em metros: "))
mm = valor*1000
print("O valor convertido em mm é {}".format(mm))


#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
#Calcule o total em segundos. FORMA 1.
dia= int(input("Digite: "))
hora= int(input("Digite: "))
min= int(input("Digite: "))
seg= int(input("Digite: "))
conv_dia =  dia*86400
conv_hora = hora*3600
conv_min = min*60
total = conv_dia + conv_hora + conv_min + seg
print("O total de {} dia e {}:{}:{} em segundos é {}".format(dia,hora,min,seg, total))

#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
#Calcule o total em segundos. FORMA 2.
dia= int(input("Digite: "))
hora= int(input("Digite: "))
min= int(input("Digite: "))
seg= int(input("Digite: "))

total = dia * 24 *3600 + hora * 3600 + min * 60 + seg
print("Em segundos é %10d" % (total))

#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá.
#Exiba o total em dias.
qt = int(input("Quantos cigarros em 1 dia?: "))
anos = float(input("Quantos anos?: "))
menos_tempo_min = qt*10 * (anos*365)
menos_tempo_dias = menos_tempo_min/(24*60)

print("O TOTAL DE DIAS PERDIDOS É DE: %8.2f" % menos_tempo_dias)

#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80
#km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da
#multa, cobrando R$ 5 por km acima de 80 km/h.

vel = float(input("Sua velocidade: "))

if vel > 80:
    multa = (vel - 80) * 5
    print("{}".format(valor))
else:
    print("Livre, pode passar")

#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
#0,45 para viagens mais longas.
km = int(input("Seus km:"))
if km <= 200:
    valor1 = km * 0.45
    print("Seu valor é: {}".format(valor1))
else:
    valor2 = km * 0.50
    print("Seu valor é: {}".format(valor2))

# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba
# os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

inicio = float(input("Deposito inicial:"))
taxa_de_juros = float(input("Digite a taxa: "))
mes = 1
saldo = inicio
while mes <= 24:
    saldo = saldo + (saldo * (taxa_de_juros / 100))
    print(f"Seu investimento do mes {mes} é de: {saldo:5.2f}")
    mes = mes + 1
    print(f"O ganho obtido com juros foi R${saldo - inicio: 8.2f}")
