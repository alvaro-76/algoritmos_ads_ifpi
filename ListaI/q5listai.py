
def main():
    num = int(input('\nInforme um número para que seja calculado seu fatorial: '))
    fatorial(num)


def fatorial(num: int):
    num_origem = num
    fat = 1
    if num < 0:
        num = int(input('\nInsira números positivos: '))
        return fatorial(num)
        
    while num > 0:
        fat *= num 
        num -= 1
    print(f'O fatorial de {num_origem} é [{fat}]')


main()