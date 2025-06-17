
def main():
    qtd_num = int(input('Informe a quantidade de números a ser pedido: '))
    controle = 1
    soma = 0
    media = 0
    maior = None

    while controle <= qtd_num:
        n_termo = int(input(f'Informe o valor do {controle}º termo: '))
        soma += n_termo
        if maior == None or n_termo > maior:
            maior = n_termo
        controle += 1

    media = soma / qtd_num
    print(f'Soma dos n termos: {soma} // media: {media:.1f}')
    print(f'Maior termo da lista: {maior}')


main()