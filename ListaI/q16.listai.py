
def main():
    qtd_termos = int(input('Informe a quantidade de termos da sequência serão exibidos: '))
    controle = 1
    a = 0
    b = 1

    while controle <= qtd_termos:
        print(a)
        a,b = b, a+b
        controle += 1

main()