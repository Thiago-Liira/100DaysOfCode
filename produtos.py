"""
Programa: Analisador de Produtos
Autor: Thiago Lira
Versão: 3.8
Fazendo: 12/07/2020
Descrição: Programa quer vai analisar alguns tipos de produtos.
"""
while True:
    produto = str(input('Informe o nome do produto: '))
    while len(produto) < 3:
        produto = str(input('Informe o nome do produto: ')).strip()

    preço = float(input('Informe o preço do produto: '))
    while preço < 0:
        #print('O produto não pode ser negativo!!')
        preço = float(input('Informe o preço do produto: '))
    

    resposta = ' '
    while resposta not in 'SNsn' :
        resposta = str(input('Deseja continuar cadastrando produto [S/N]: ')).upper()[0]        
    if resposta == 'N':
        break