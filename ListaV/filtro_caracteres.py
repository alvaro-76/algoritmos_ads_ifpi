import utils_listaV

# -> FAZENDO DA 1º FORMA APRENDIDA, DESTA FORMA, PARA CADA GIRO DO FOR, EU TENHO QUE USAR A FUNÇÃO STRIP ANTES
def main(): 
    arquivo = open('br-sem-acentos.txt')

    contador_geral = 0
    contador_filtro = 0

    tam = utils_listaV.obter_inteiro_positivo('Informe o tam. mín. de caracteres: ')

    for i in arquivo: #i significa as linhas de texto que estão sendo percorridas no arquivo txt
        palavra = i.strip() #nesta linha estou retirando os espaços em branco das linhas do arquivo txt

        if len(palavra) >= tam:
            print(palavra)
            contador_filtro += 1

        contador_geral += 1

    print(f'Palavras filtradas: {contador_filtro} de {contador_geral}')

# -> FAZENDO USANDO O MAP TRADICIONAL DO PYTHON, ONDE A FUNÇÃO STRIP JÁ FOI APLICADA NO ARQUIVO
def main2():

    palavras = map(lambda x:x.strip(), open('br-sem-acentos.txt')) # A LISTA JÁ ESTÁ FORMATADA DO JEITO QUE EU QUERO

    tam = utils_listaV.obter_inteiro_positivo('> ')

    for palavra in palavras:
        if len(palavra) >= tam:
            print(palavra)

# -> A LISTA TAMBÉM JÁ SAI FORMATADA DO JEITO QUE EU QUERO, PORÉM AQUI ESTOU UTILIZANDO UMA FUNÇÃO PRÓPRIA
# O QUE DIFERE A MAIN3 DA MAIN2 É A ORDEM DE PARAMETROS DAS FUNÇÕES
def main3():
    
    arquivo = utils_listaV.mapear(open('br-sem-acentos.txt'), lambda x:x.strip())
    #arquivo = utils_listaV.mapear(open('br-sem-acentos.txt').readlines(), lambda x:x.strip()) -> utilizando a função readlines()


    tam = utils_listaV.obter_inteiro_positivo('> ')

    for palavra in arquivo:
        if len(palavra) >= tam:
            print(palavra)


'''conclusão, a 2 e a 3 formas são mais eficientes, visto que não será necessário a função strip() a cada giro do for,
além de já implementar o uso da função map'''


def main_definitivo():
    palavras = mapear(lambda x:x.strip(), open('br-sem-acentos.txt'))
    tam = utils_listaV.obter_inteiro_positivo('> ')

    for palavra in palavras:
        if len(palavra) >= tam:
            print(palavra)


def mapear(funcao, colecao):
    new_colecao = []

    for i in colecao:
        new_item = funcao(i)
        new_colecao.append(new_item)

    return new_colecao


main_definitivo()