
def main():
    limite_superior = int(input('Informe o limite superior: '))
    limite_inferior = int(input('Informe o limite inferior: '))
    qtd_impar = 0
    qtd_par = 0
    qtd_primo = 0

    while limite_inferior <= limite_superior:
        if impar(limite_inferior):
            qtd_impar += 1
            print(f'{limite_inferior} é ímpar')
        elif par(limite_inferior):
            qtd_par += 1
            print(f'{limite_inferior} é par')

        if num_primo(limite_inferior):
            qtd_primo += 1
            print(f'[{limite_inferior} é primo]')

        limite_inferior += 1

    print(f'Números pares: {qtd_par} // Números ímpares: {qtd_impar} // Números primo: {qtd_primo}')


def impar(n):
    if n % 2 != 0:
        return True
    
    return False


def par(n):
    if n %2 == 0:
        return True
    
    return False


def num_primo(n):
    if n == 1:
        return False
    
    if n in (2, 3, 5, 7):
        return True
    
    if n %2 != 0 and n %3 != 0 and n %5 != 0 and n%7 != 0:
        return True
    
    return False


main()