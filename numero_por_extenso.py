"""
Programa: Número por extenso
Autor: Thiago Lira
Versão: 3.8
Fazendo: 17/07/2020
Descrição: Programa onde o usuário digita um número e retorna para ele o número por extenso.
"""
numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Qual número você deseja ver por extenso entre 0 e 20: '))

while 0 < n > 20: #Validando se o usuário digitou o número certo
    n = int(input('Qual número você deseja ver por extenso entre 0 e 20: '))

for i in range(0, len(numero)):
    if i == n:
        print(f'{numero[i]}')
   
