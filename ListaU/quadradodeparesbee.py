
def main():
    numN = obter_N('')

    for i in range(1, numN + 1):
        if verificar_par(i):
            quadrado = i**2
            print(f'{i}^2 = {quadrado}')


def verificar_par(n):
    if n %2 != 0:
        return False
    
    return True


def obter_N(label):
    n = int(input(label))

    if n < 5 or n > 2000:
        return obter_N(label)
    
    return n

main()