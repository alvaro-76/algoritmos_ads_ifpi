
def main():
    qtd_litros = float(input('Informe a quantidade de litros(L): '))
    combustivel = input('Informe o tipo de combustível(A-álcool//G-gasolina): ')
    combustivel = combustivel.lower()
    if combustivel != 'g' and combustivel != 'a':
        combustivel = pedir_combustivel(label='Informe o tipo de combustível: ')

    if combustivel == 'g':
        combustivel = 'gasolina'
        valor = calcular_gasolina(qtd_litros)
    elif combustivel == 'a':
        combustivel = 'álcool'
        valor = calcular_alcool(qtd_litros)

    print(f'Valor final de {qtd_litros} de {combustivel}: R${valor:.2f}')


def calcular_gasolina(qtd_litros):
    valor_litro = 2.50
    if qtd_litros <= 20:
        valor_litro *= 0.96
    elif qtd_litros > 20:
        valor_litro *= 0.94

    valor_final = valor_litro * qtd_litros
    return valor_final

def calcular_alcool(qtd_litros):
    valor_litro = 1.90
    if qtd_litros <= 20:
        valor_litro *= 0.97
    elif qtd_litros > 20:
        valor_litro *= 0.95

    valor_final = valor_litro * qtd_litros
    return valor_final


def pedir_combustivel(label): #recursividade para o tipo de combustível a ser pedido
    combustivel = input(label)
    if combustivel != 'g' and combustivel != 'a':
        return pedir_combustivel(label)
    
    return combustivel


main()