import utils, vetor_funcionalidades, os, random, vetor_utils

def main():

    vetor = []

    menu = '''
    >>>PlayNumbers<<<
1 - Inicializar vetor numérico 
2 - Mostrar todos os valores
3 - Resetar vetor
4 - Ver quantidade de itens no vetor
5 - Ver menor e maior valores e suas posições
6 - Somatório dos valores
7 - Média dos valores
8 - Mostrar valores positivos e quantidade
9 - Mostar valores negativos e quantidade
10 - Atualizar valores
11 - Adicionar novos valores
12 - Remover itens por valor exato
13 - Remover por posição
14 - Editar valor específico por posição
15 - Salvar valores em arquivo
16 - Sair

Opção -> '''

    option = utils.obter_numero_positivo(menu)

    while option != 16:

        if option == 1:
            vetor = vetor_funcionalidades.inicializar_vetor_numerico()
            
        elif option == 2:
            vetor_utils.exibir_valores_lista(vetor)

        elif option == 3:
            vetor = vetor_utils.resetar_vetor()

        elif option == 4:
            qtd_itens = vetor_utils.exibir_qtd_itens(vetor)
            print(f'O vetor tem {qtd_itens} itens')
            
        elif option == 5:
            maior, menor, posicao_maior, posicao_menor = vetor_utils.maior_menor(vetor)
            print(f'O maior item do vetor é: [{maior}] na posição {posicao_maior}, o menor item do vetor é [{menor}] na posição {posicao_menor}')

        elif option == 6:
            somatorio_vetor = vetor_utils.somatorio(vetor)
            print(f'O somatório do vetor é igual a: {somatorio_vetor}')

        elif option == 7:
            media_vetor = vetor_utils.media(vetor)
            print(f'A média de valores no vetor é de {media_vetor:.1f}')

        elif option == 8:
            qtd_positivos, positivos = vetor_utils.exibir_positivos(vetor)
            print(f'O vetor possui {qtd_positivos} itens positivos, sendo eles: {positivos}')
            
        elif option == 9:
            qtd_negativos, negativos = vetor_utils.exibir_negativos(vetor)
            print(f'O vetor possui {qtd_negativos} itens negativos, sendo eles: {negativos}')

        elif option == 10:
            vetor = vetor_funcionalidades.atualizar_vetor(vetor)
            print(vetor)

        elif option == 11:
            vetor = vetor_funcionalidades.adicionar_itens(vetor)

        elif option == 12:
            vetor = vetor_funcionalidades.remover_itens_exatos(vetor)

        elif option == 13:
            vetor = vetor_funcionalidades.remover_itens_posicao(vetor)

        elif option == 14:
            vetor = vetor_funcionalidades.editar_valor_posicao(vetor)

        elif option == 15:
            vetor = vetor_funcionalidades.salvar_valores_arquivo(vetor)
        
        input('>continue')
        os.system('cls')
        option = utils.obter_numero_positivo(menu)
    
    print('Encerrando...')


main()