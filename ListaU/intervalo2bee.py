
def main():
    numN = int(input(''))
    qtd_in = 0
    qtd_out = 0

    for i in range(1, numN+1):
        valorX = int(input(''))
        if in_intervalo(valorX):
            qtd_in += 1
        else:
            qtd_out += 1

    print(f'{qtd_in} in')
    print(f'{qtd_out} out')


def in_intervalo(n):
    if 10 <= n <= 20:
        return True
    else:
        return False


main()