
def main():
    num = int(input('Informe um número: '))
    contar_1_to_num(num)


def contar_1_to_num(num: int):
    i = 1
    while i <= num:
        print(i)
        i += 1


main()
    