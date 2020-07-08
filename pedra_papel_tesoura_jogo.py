"""
Programa: Jogo pedra papel e tesoura
Autor: Thiago Lira
Versão: 3.8
Fazendo: 04/07/2020
Descrição: Um pequeno jogo pedra papel e tesoura, em outras regiões conhecido como Jokenpô.
"""
import time
import random
jogo = ('pedra', 'papel', 'tesoura')
maquina = random.randint(0, 2)

print('Olá, vamos brincar')
time.sleep(2)
print('Escolha uma das opção!')
print("""
    [0]: Pedra
    [1]: Papel
    [2]: Tesoura
""")

game = True

# O usuário tem três tentativas para vencer.
for i in range(0, 3):
    usuario = int(input('Qual vocẽ escolhe? '))

    if usuario != jogo:
        print('Opção inválida')
        game = False
    else:
        game = True

    print('PE')
    time.sleep(1)
    print('DRA')
    time.sleep(1)
    print('PA')
    time.sleep(1)
    print('PEL')
    time.sleep(1)
    print('E')
    time.sleep(1)
    print('TE')
    time.sleep(1)
    print('SOU')
    time.sleep(1)
    print('RA')
    time.sleep(1)

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
