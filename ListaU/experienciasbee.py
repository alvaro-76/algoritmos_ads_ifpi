
def main():
    numN = int(input(''))
    qtd_cobaias = 0
    qtd_coelho = 0
    qtd_sapo = 0
    qtd_rato = 0

    for _ in range(numN):
        qtd, tipo = input().split()
        qtd = int(qtd)
        qtd_cobaias += qtd

        if tipo == 'S':
            qtd_sapo += qtd
        elif tipo == 'C':
            qtd_coelho += qtd
        elif tipo == 'R':
            qtd_rato += qtd

    percentual_rato = (qtd_rato*100)/qtd_cobaias
    percentual_sapo = (qtd_sapo*100)/qtd_cobaias
    percentual_coelho = (qtd_coelho*100)/qtd_cobaias

    print(f'Total: {qtd_cobaias} cobaias')
    print(f'Total de coelhos: {qtd_coelho}')
    print(f'Total de ratos: {qtd_rato}')
    print(f'Total de sapos: {qtd_sapo}')
    print(f'Percentual de coelhos: {percentual_coelho:.2f} %')
    print(f'Percentual de ratos: {percentual_rato:.2f} %')
    print(f'Percentual de sapos: {percentual_sapo:.2f} %')


main()