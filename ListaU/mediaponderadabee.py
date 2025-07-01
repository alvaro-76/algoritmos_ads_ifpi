
def main():
    numN = obter_n('')

    for _ in range(numN):
        n1 = 0
        n2 = 0
        n3 = 0
        n1, n2, n3 = map(float, input('').split())
        media = calcular_media_ponderada(n1,n2,n3)
        print(f'{media:.1f}')


def calcular_media_ponderada(n1,n2,n3):
    media = ((n1*2)+(n2*3)+(n3*5))/10

    return media


def obter_n(label):
    try:
        n = int(input(label))
    except:
        return obter_n(label)
    
    return n

main()