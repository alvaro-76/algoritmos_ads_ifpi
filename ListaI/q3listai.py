
def main():
    varA = int(input('Informe o valor inicial da PA: '))
    razao = int(input('Informe a razão da PA: '))
    limite = int(input('Informe um número limite(só serão exibidos os valores menores que limite): '))

    prog_aritimetica(varA, razao, limite)


def prog_aritimetica(varA: int, razao: int, limite: int):
    print(f'Os valores menores que {limite} são:' , end= ' ')
    while varA < limite:
        print(f'[{varA}]', end= ' ')
        varA = varA + razao


main()