
def main():
    num = int(input('Informe o valor de N: '))
    soma = 0
    i = 1

    while i <= num:
        print(i)
        soma += i
        i += 1
    
    print(f'Soma de 1 até {num}: {soma}')

main()