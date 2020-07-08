"""
Programa: Em que nome eu estou pensando
Autor: Thiago Lira
Versão: 3.8
Fazendo: 06/07/2020
Descrição: Um pequeno jogo, onde contêm na lista alguns nome e o jogador tem que
           adivinhar em qual nome o computador pensou.
"""
import random
import time

nome = ('Julia', 'Ana', 'Camila', 'Fernanda', 'Roberto', 'Emanuel','Matheus', 'Pedro')
computador = random.choice(nome)

print('Olá, vamos brincar')
time.sleep(2)
print('Escolha um nome!')
print("""
      Julia - Ana - Camila - Fernanda - Roberto - Emanuel - Matheus - Pedro
      """)
time.sleep(1)      
print('Em que nome eu estou pensando? ')

# O usuário tem 3 tentativas para acertar 
for i in range(1,4):
    jogador = str(input('Em qual nome estou pensando: ')).title()
    
    if jogador in nome: #Verifica se contêm o nome 
        if computador == jogador:
            print('Parabens você acertou!!!')
            print('O nome em que eu pensei foi: {}'.format(computador))
        elif computador != jogador: 
            print('Você errou!')
            print('O nome em que eu pensei foi: {}'.format(computador))
    else:
        print('Não contem esse nome na lista!')