import utils

def main():
    menu = '''
        Filtro de palavras
1 - Filtrar por tamanho 
2 - Filtrar palavras sem determinado caracter
3 - Filtrar palavras sem determinadas letras
4 - Filtrar palavras somente com letras permitidas
5 - Filtras palavras com letras obrigatórias
6 - Palvras com letras em ordem alfabética
0 - Sair
'''
    
    op = int(input(menu))

    while True:
        if op == 0:
            break
        elif op == 1:
            tam = int(input('Informe o tamanho mínimo de caracteres: '))
            utils.tamanho_caracteres(tam)
        elif op == 2:
            letra = input('Informe a letra que deve ser ignorada: ')
            utils.not_caracter(letra)
        elif op == 3:
            letras_proibidas = input("Informe quais letras devem ser evitadas: ")
            utils.caracteres_proibidos(letras_proibidas)
        elif op == 4:
            letras_permitidas = input('Informe as letras que devem aparecer: ')
            utils.apenas_letras_obrigatorias(letras_permitidas)
        elif op == 5:
            letras_obrigatorias = input('Informe as letras orbigatórias: ')
            utils.todas_letras_obrigatorias(letras_obrigatorias)
        elif op == 6:
            utils.ordem_alfabetica()

        input('>> continue')
        op = int(input(menu))

    print('Encerrando...')


main()