"""
Programa: Jogo pedra papel e tesoura
Autor: Thiago Lira
Versão: 3.8.3
Fazendo: 04/07/2020
Descrição: Um pequeno jogo pedra papel e tesoura, em outras regioes conhecido como Jokenpô.
"""

from random import *
jogo = ('pedra', 'papel', 'tesoura')
maquina = randint(0, 2)

print('Olá, vamos brincar')
print('Escolha uma das opção!')
print("""
    [0]: Pedra
    [1]: Papel
    [2]: Tesoura
""")

usuario = int(input('Qual vocẽ escolhe? '))

print('O jogador escolheu {}!'.format(jogo[usuario]))
print('O computador escolheu {}!'.format(jogo[maquina]))

if maquina == 0: #Maquina escolheu pedra.
    if usuario == 0:
        print('Empate')
    elif usuario == 1:
        print('Você venceu, parabéns!')
    elif usuario == 2:
        print('O computador ganhou!')
elif maquina == 1: #Maquina escolheu papel
    if usuario == 0:
        print('O computador ganhou!')
    elif usuario == 1:
        print('Empate')
    elif usuario == 2:
        print('Você venceu, parabéns!')
elif maquina == 2: #Maquina escolheu tesoura
    if usuario == 0:
        print('Você venceu, Parabéns!')
    elif usuario == 1:
        print('O computador ganhou!')
    elif usuario == 2:
        print('Empate!')
