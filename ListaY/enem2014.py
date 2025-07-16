import utils, vetor_funcionalidades, os

def main():

    arquivo = vetor_funcionalidades.load_arquivo('enem2014_nota_por_escola.txt')

    menu = '''
    Sugestões de consulta
1 - Top N Brasil(todas as áreas) 
2 - Top N Brasil por área
3 - Top N por estado
4 - Top N por estado e rede (pública ou privada)
5 - Media nacional por área
6 - Melhor escola por área e estado
7 - Lisa de escolas por estado ordenada por renda
8 - Busca escola específica por parte do nome
9 - Ranking ENEM por estado
10 - Ranking ENEM por região do país

0 - Sair

Opção -> '''

    option = utils.obter_numero(menu)

    while option != 0:

        if option == 1:
            n = utils.obter_numero_positivo('Informe quais N escolas deseja ver: ')
            resultado = vetor_funcionalidades.topn_brasil(arquivo, n)
            print(*resultado, sep='\n')

        elif option == 2:
            n = utils.obter_numero_positivo('Informe quais N escolas deseja ver: ')
            areas = vetor_funcionalidades.menu_areas()
            escolha_area= input(areas)
            resultado = vetor_funcionalidades.topn_brasil_area(arquivo, escolha_area, n)
            print(*resultado, sep='\n')

        elif option == 3:
            n = utils.obter_numero_positivo('Informe quais N escolas deseja ver: ')
            estado = input('Informe o estado(ex: PI, MA, etc): ').upper()
            resultado = vetor_funcionalidades.topn_estado(arquivo, estado, n)
            print(*resultado, sep='\n')

        elif option == 4:
            n = utils.obter_numero_positivo('Informe quais N escolas deseja ver: ')
            estado = input('Informe o estado(ex: PI, MA): ').upper()
            rede = input('Informe a rede: ').title()
            resultado = vetor_funcionalidades.top_estados_rede(arquivo, estado, rede, n)
            print(*resultado, sep='\n')

        elif option == 5:
            areas = vetor_funcionalidades.menu_areas()
            escolha_area = input(areas)
            resultado = vetor_funcionalidades.media_nacional_area(arquivo, escolha_area)
            print(f'Média: {resultado}')

        elif option == 6:
            areas = vetor_funcionalidades.menu_areas()
            escolha_area = input(areas)
            estado = input('Informe o estado: ').upper()
            resultado = vetor_funcionalidades.melhor_escola_area_estado(arquivo, escolha_area, estado)
            print(resultado)

        elif option == 7:
            estado =input('Informe o estado: ').upper()
            resultado = vetor_funcionalidades.ordenar_estado_renda(arquivo, estado)
            print(*resultado, sep='\n')

        elif option == 8:
            parte_nome = input('Informe qual parte do nome deseja procurar: ').upper()
            resultado = vetor_funcionalidades.procurar_nome(arquivo, parte_nome)
            print(*resultado, sep='\n')

        elif option == 9:
            estado = input('Informe o estado: ').upper()
            resultado = vetor_funcionalidades.ranking_enem_estado(arquivo, estado)
            print(*resultado, sep='\n')

        elif option == 10:
            n = utils.obter_numero_positivo('Informe as n escolas que deseja ver: ')
            estado = input('Informe o estado(consequentemente a região): ').upper()
            resultado = vetor_funcionalidades.ranking_enem_regiao(arquivo, estado, n)
            print(*resultado, sep='\n')

        input('continue...')
        os.system('cls')
        option = utils.obter_numero(menu)

    print('Encerrando...')


main()