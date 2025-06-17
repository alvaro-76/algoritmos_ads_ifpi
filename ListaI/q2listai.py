
def main():
    num = int(input('Informe um número: '))
    numeros_pares(num)


def numeros_pares(num: int):
    i = 1
    print(f'Os números pares de 1 até {num} são:', end = ' ')
    while i <= num:
        if i % 2 == 0:
            print(i, end= ' ')
        i += 1


main()