Hoje observei um projeto simples mas esclarecedor do funcionamento de análise de dados
Aprendendo a extrair informações de uma página web -
https://github.com/karinnecristina/Data_Science/blob/master/tripadvisor/README.md#aprendendo-a-extrair-informa%C3%A7%C3%B5es-de-uma-p%C3%A1gina-web

Tambem ler depois - https://github.com/Patotricks15/Ciencia-de-dados-projetos

Exercicios sobre listas

notas = []
contador = 1

while contador < 5:
    notas.append(float(input(f'Informe a {contador}a nota: ')))
    contador += 1

maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)

print(f'A média final é {media:.2f}. A sua maior nota foi {maior_nota:.2f} e a menor foi {menor_nota:.2f}')


Exercicio sobre listas 2
notas = []
contador = 1

while contador < 5:
    notas.append(int(input(f'Informe a {contador}ª nota: ')))
    contador += 1

media = sum(notas) / len(notas)
print(f'Sua média final foi {media}')
if media >= 7:
    print('APROVADO')
else:
    notas.append(int(input('Informe a nota da prova final: ')))

    media = sum(notas) / len(notas)
    print(f'Sua média final foi {media}')
    if media >= 5:
        print('APROVADO')
    else:
        print('REPROVADO')
