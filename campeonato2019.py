"""
Programa: Analise do campeonato brasileiro de 2019.
Autor: Thiago Lira
Versão: 3.8
Fazendo: 17/07/2020
Descrição: Programa que vai fazer analise do campeonato brasileiro de 2019, usando tuplas.
"""
times = ('Flamengo - RJ', 'Santos - SP', 'Palmeiras - SP', 'Grêmio - RS','Athletico Paranaense - PR'
,'São Paulo - SP', 'Internacional - RS', 'Corinthians - SP', 'Fortaleza - CE', 'Goiás - GO', 'Bahia - BA',
'Vasco da Gama - RJ', 'Atlético - MG', 'Fluminense - RJ', 'Botafogo - RJ', 'Ceará - CE', 'Cruzeiro - MG', 
'Csa - AL', 'Chapecoense - SC', 'Avaí - SC')

print(f'Os cinco primeiro do campeonato são: {times[0:5]}')
print()
print(f'Os quatros últimos do campeonato são: {times[16:]}')
print()
print(f'Os times em ordem alfabéticas são: {sorted(times)}')