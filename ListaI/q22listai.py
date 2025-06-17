
def main():
    qtd_fichas = int(input('Informe a quantidade de fichas que serão cadastradas: '))
    controle = 1
    mais_magro = None
    mais_gordo = None
    id_gordo = 0
    id_magro = 0


    while controle <= qtd_fichas:
        id_boi = int(input('Informe o número de identificação do boi: '))
        peso = float(input('Informe o peso(kg) do boi: '))

        if mais_magro == None or peso < mais_magro:
            mais_magro = peso
            id_gordo = id_boi

        if mais_gordo == None or peso > mais_gordo:
            mais_gordo = peso
            id_magro = id_boi

        controle += 1

    print(f'Mais magro: [{id_magro}][{mais_magro:.2f}kg] // Mais gordo: [{id_gordo}][{mais_gordo:.2f}kg]')


main()