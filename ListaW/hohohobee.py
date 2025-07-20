
def main():
    num = obter_entrada('')

    print(' '.join(['Ho']*(num - 1) + ["Ho!"]))


def obter_entrada(label):
    num = int(input(label))

    if num < 1 or num > 10**6:
        print('Entrada inválida')
        return obter_entrada(label)
    
    return num


main()