
def main():
    num = int(input('Informe o valor de N: '))
    limite_superior = int(input('Informe o valor do limite superior: '))
    limite_inferior = int(input('Informe o valor do limite inferior: '))
    
    while limite_inferior <= limite_superior:
        if multiplo_num(num, limite_inferior):
            print(limite_inferior)

        limite_inferior += 1


def multiplo_num(num, limite_inf):
    if limite_inf % num == 0:
        return True
    
    return False


main()