"""
Programa: Analisador de dados
Autor: Thiago Lira
Versão: 3.8
Fazendo: 03/07/2020
Descrição: Programa quer pergunta ao o usuário o nome, idade, sexo e altura e dizer
           a média da idade e altura do grupo.
"""
fim = 'S'
h = 0
g = 0
media_idade = 0
media_altura = 0
while fim == 'S':
    
    nome = str(input('Informe seu nome: ')).strip()
    while len(nome) < 3:
        nome = str(input('Informe seu nome: ')).strip()
    
    idade = int(input('Digite sua idade: '))
    while (idade < 0):
        idade = int(input('Digite a idade correta, por favor: '))
    
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while (sexo != 'F') and (sexo != 'M'):
        sexo = str(input('Digite seu sexo: [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        h += 1
    else:
        g += 1
    
    relacionamento = str(input('Qual o seu estado civil: ')).upper().strip()[0]
    while (relacionamento != 'S') and (relacionamento != 'C') and (relacionamento != 'D') and (relacionamento != 'V'):
        relacionamento = str(input('Qual o seu estado civil: ')).upper().strip()[0]
      
    altura = float(input('Qual a sua altura? '))
    while altura < 0:
        altura = float(input('Qual a sua altura? '))
        
    fim= str(input('Quer continuar cadastrando?[S/N] ')).upper().strip()[0]
   
