import utils_listaV
import os

def main():

    palavras = load_palavras()
    
    menu = '''
        Selecione a operação
    1 - Palavra com no mínimo N caracteres
    2 - Palavras sem determinado caracter
    3 - Palavras sem letras proibidas
    4 - Palavras somente com letras permitidas
    5 - Palavras com letras obrigatórias
    6 - Palavras em orde alfabética
    0 - Sair

Opção >>> '''

    option = utils_listaV.obter_entrada_menu(menu)

    while option != 0:
        if option == 1:
            filtrar_tamanho(palavras)
        elif option == 2:
            filtrar_caracterproibido(palavras)
        elif option == 3:
            filtrar_letrasproibidas(palavras)
        elif option == 4:
            filtrar_letraspermitidas(palavras)
        elif option == 5:
            filtrar_letrasobrigatorias(palavras)
        elif option == 6:
            ordem_alfabetica(palavras)

        input('>continue...')
        os.system('cls')
        option = utils_listaV.obter_entrada_menu(menu)

    print('. . .')


def filtrar_tamanho(palavras):
    tam = utils_listaV.obter_inteiro_positivo('Informe o tamanho min das palavras: ')

    palavras_filtradas = utils_listaV.filtrar(palavras, lambda x:len(x) >= tam)
    utils_listaV.exibir_palavras(palavras_filtradas)


def filtrar_caracterproibido(palavras):
    proibido = input('Informe o caracter proibido: ')

    palavras_filtradas = utils_listaV.filtrar(palavras, lambda palavra:utils_listaV.char_proibido(palavra, proibido))
    utils_listaV.exibir_palavras(palavras_filtradas)


def filtrar_letrasproibidas(palavras):
    proibidas = input('Informe as letras proibidas: ').strip()

    palavras_filtradas = utils_listaV.filtrar(palavras, lambda palavra:utils_listaV.palavras_sem_letras(palavra, proibidas))
    utils_listaV.exibir_palavras(palavras_filtradas)


def filtrar_letraspermitidas(palavras):
    permitidas = input('Informe as letras permitidas: ').strip()

    palavras_filtradas = utils_listaV.filtrar(palavras, lambda palavra: not utils_listaV.palavras_sem_letras(palavra, permitidas))
    utils_listaV.exibir_palavras(palavras_filtradas)


def filtrar_letrasobrigatorias(palavras):
    obrigatorias = input('Informe as letras obrigatórias: ').strip()

    palavras_filtradas = utils_listaV.filtrar(palavras, lambda palavra: utils_listaV.palavras_obrigatorias(palavra, obrigatorias))
    utils_listaV.exibir_palavras(palavras_filtradas)


def ordem_alfabetica(palavras):
    palavras_filtradas = utils_listaV.filtrar(palavras, lambda palavra: utils_listaV.abcdarian(palavra))
    utils_listaV.exibir_palavras(palavras_filtradas)


def load_palavras():
    return utils_listaV.mapear(open('br-sem-acentos.txt').readlines(), lambda x:x.strip())


main()