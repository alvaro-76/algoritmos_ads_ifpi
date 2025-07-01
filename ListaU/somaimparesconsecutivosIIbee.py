
def main():
    numN = obter_n('')
    soma_impar = 0

    for _ in range(numN):
        numX, numY = map(int, input('').split())
        soma_impar = 0

        if numY < numX:
            numX, numY = numY, numX

        for i in range(numX+1, numY):
            if verificar_impar(i):
                soma_impar += i

        print(soma_impar)


def verificar_impar(n):
    if n%2 == 0:
        return False
    
    return True


def obter_n(label):
    try:
        n = int(input(label))
    except:
        return obter_n(label)
    
    return n


main()