
def main():
    numN = obter_n('')

    for i in range(1, 11):
        print(f'{i} x {numN} = {i*numN}')


def obter_n(label):
    n = int(input(label))

    if n < 2 or n > 1000:
        return obter_n(label)
    
    return n


main()