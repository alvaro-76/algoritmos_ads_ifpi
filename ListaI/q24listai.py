
def main():
    qtd_habitantes = int(input('Informe a quantidade de habitantes que serão analisados: '))
    controle = 1
    soma_salario = 0
    soma_filhos = 0
    salario_mil = 0

    while controle <= qtd_habitantes:
        salario = float(input(f'Informe o salário do {controle}º habitante: '))
        soma_salario += salario
        if salario <= 1000:
            salario_mil += 1

        qtd_filhos = int(input(f'Informe a quantidade de filhos do {controle}º habitante: ')) 
        soma_filhos += qtd_filhos

        controle += 1

    media_salario = soma_salario/qtd_habitantes
    media_filhos = soma_filhos/qtd_habitantes
    percent_salario_mil = (salario_mil*100)/qtd_habitantes

    print(f'Média salarial da população: R${media_salario:.2f} Média de filhos da população: {media_filhos:.2f}')
    print(f'Percentual de pessoas que ganham até R$1000: {percent_salario_mil:.2f}%')


main()