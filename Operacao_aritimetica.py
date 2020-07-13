"""
Programa: Operação basicas matematica e tabuada
Autor: Thiago Lira
Verção: 3.8
Finalizado: 02/07/2020
Descrição: Programa quer pergunta ao o usuário qual das operação basicas
           ele vai querer realizar ou mostrar a tabuada.
"""
import time

print("""
    1: Soma
    2: Subtração
    3: Mutiplicação
    4: Divisão
    5: Potenciação
    6: Tabuada
    7: Fatorial
    8: Progressão aritmética
    9: Sair do programa
""")
digito = 0
while digito != 7:
    digito = int(input('Informe um número: '))
    if 1 == digito: #Soma
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

        s = n1 + n2

        print('A soma do número {} + {} = {}'.format(n1, n2, s))

    elif 2 == digito: #Subtração
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

        Subtração = n1 - n2

        print('A soma do número {} - {} = {}'.format(n1, n2, Subtração))

    elif 3 == digito: #Mutiplicação
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

        m = n1 * n2

        print('A soma do número {} x {} = {}'.format(n1, n2, m))

    elif 4 == digito: #Divisão
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

        d = n1 / n2

        print('A soma do número {} / {} = {}'.format(n1, n2, d))

    elif 5 == digito: #Potenciação
        base = int(input('Informe o valor da base: '))
        expoente = int(input('Informe o valor do expoente: '))

        if base != 0 and expoente == 0:
            print('A potenciação é 1')
        elif base != 0 and expoente == 1:
            print('A pontenciação é {}'.format(base))
        elif base == 1:
            print('A pontenciação é {}'.format(base))
        elif base == 0:
            print('A pontenciação é {}'.format(base))
        else:
            potencia = base ** expoente
            print('A potenciação é {}'.format(potencia))

    elif 6 == digito: #Tabuada
        n = int(input('Qual a tabuada que você quer olhar? '))
        for i in range(1, 11):
            print(i, 'x', n, '=', i*n)
    
    elif 7 == digito: #Fatorial
        num = int(input('Digite um número para calcular seu fatorial: '))
        f = 1
        for i in range(num, 1, -1):
            f *= i
        print(f)
    
    elif 8 == digito: # Progressão aritmética
        n = int(input('Digite o número de termo: '))
        r = int(input('Digite a razão: '))
        
    elif 9 == digito: #Saindo do programa
        print('Finalizando o programa...')
        time.sleep(1)
        break

    else:
        print('Você informou um número inválido!')

