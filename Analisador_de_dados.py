"""
Programa: Analisador de dados
Autor: Thiago Lira
Versão: 3.8
Fazendo: 03/07/2020
Descrição: Programa quer pergunta ao o usuário o nome, idade, sexo e altura e dizer
           a média da idade e altura do grupo.
"""
h = 0
g = 0
media_idade = 0
media_altura = 0
for i in range(1,6):
    nome = str(input('Digite seu nome: ')).split()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F]: ')).upper().strip()[0]
    altura = float(input('Qual a sua altura? '))

    #Média das idades:
    media_idade += idade
    Media_calculada = media_idade / i

    #Quantidade de pessoas dos sexo masculino e femenino:
    if sexo == 'M':
        h += 1
    else:
        g += 1

    # Média das alturas
    media_altura += altura
    alturas = media_altura / i
   
print(f'A média das idades é de: {Media_calculada}')
print(f'Existem {g} mulheres e {h} Homens')
print(f'A média das alturas do grupo é de {alturas}')