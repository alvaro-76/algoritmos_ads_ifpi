
def main():
    tipo_pagamento = 'normal'
    tipo_carne = input('Informe o tipo de carne que deseja: f-File // a-alcatra // p-picanha: ')
    tipo_carne = tipo_carne.lower()
    if tipo_carne != 'f' and tipo_carne != 'a' and tipo_carne != 'p':
        tipo_carne = pedir_tipo_carne(label='Informe o tipo de carne que deseja: ')
    qtd_carne = float(input('Informe a quantidade de carne que deseja comprar(kg): '))

    if tipo_carne == 'f':
        tipo_carne = 'filé'
        valor = calcular_file(qtd_carne)
    elif tipo_carne == 'a':
        tipo_carne = 'alcatra'
        valor = calcular_alcatra(qtd_carne)
    elif tipo_carne == 'p':
        tipo_carne = 'picanha'
        valor = calcular_picanha(qtd_carne)

    forma_pagamento = int(input('A compra será feita no cartão Tabajara ? 1-sim // 0-não: '))
    if forma_pagamento == 1:
        tipo_pagamento = 'cartão tabajara'
        valor_desconto = valor * 0.05
    else:
        valor_desconto = 0.00
    
    cupom_fiscal = f'''
        >>>CUPOM FISCAL<<<
    Tipo de carne: {tipo_carne}
    Quantidade(kg): {qtd_carne:.2f}kg
    Preço total: R${valor:.2f}
    Tipo de pagamento: {tipo_pagamento}
    Valor do desconto: R${valor_desconto:.2f}
    valor a pagar: R${(valor - valor_desconto):.2f}
'''
    print(cupom_fiscal)


def calcular_file(qtd_carne):
    valor_kg = 4.90
    if qtd_carne > 5.00:
        valor_kg = 5.80

    valor_final = qtd_carne * valor_kg
    return valor_final


def calcular_alcatra(qtd_carne):
    valor_kg = 5.90
    if qtd_carne > 5.00:
        valor_kg = 6.80

    valor_final = qtd_carne * valor_kg
    return valor_final


def calcular_picanha(qtd_carne):
    valor_kg = 6.90
    if qtd_carne > 5.00:
        valor_kg = 7.80

    valor_final = qtd_carne * valor_kg
    return valor_final


def pedir_tipo_carne(label):
    tipo_carne = input(label)
    if tipo_carne != 'f' and tipo_carne != 'a' and tipo_carne != 'p':
        return pedir_tipo_carne(label)
    
    return tipo_carne

main()