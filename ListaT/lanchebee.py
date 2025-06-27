
def main():
    lanche, quantidade = map(int, input('').split())

    if lanche == 1:
        preco_lanche = 4.00
    if lanche == 2:
        preco_lanche = 4.50
    if lanche == 3:
        preco_lanche = 5.00
    if lanche == 4:
        preco_lanche = 2.00
    if lanche == 5:
        preco_lanche = 1.50

    valor = preco_lanche * quantidade
    print(f'Total: R$ {valor:.2f}')


main()