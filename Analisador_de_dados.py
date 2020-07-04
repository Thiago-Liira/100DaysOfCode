"""
Programa: Analisador de dados
Autor: Thiago Lira
Versão: 3.8.3
Fazendo: 03/07/2020
Descrição: Programa quer pergunta ao o usuário o nome, idade, sexo e dizer a média das idade do grupo.
"""
h = 0
g = 0
media = 0
for i in range(1,3):
    nome = str(input('Digite seu nome: ')).split()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F]: ')).lower()

    #Média das idades:
    media += idade
    Media_calculada = media / i

    #Quantidade de pessoas dos sexo masculino e femenino:
    if sexo == 'm':
        h += 1
    else:
        g += 1
   
print('A média das idades é de: {}'.format(Media_calculada))
print('Existem {} mulheres e {} Homens'.format(g, h))