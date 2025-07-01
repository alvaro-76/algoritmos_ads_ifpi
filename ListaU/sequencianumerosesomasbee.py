
def main():
    while True:
        n, m = map(int, input('').split())
        if n <= 0 or m <= 0:
            break

        soma = 0

        if n > m:
            m, n = n, m
        
        sequencia = []
        for i in range(n, m+1):
            sequencia.append(i)
            soma += i

        print(*sequencia, f'Sum={soma}')


main()